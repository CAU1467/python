# import detectron2
# from detectron2.utils.logger import setup_logger
# setup_logger()

# # common libraries
# import numpy as np
# import os, json, cv2, random
# import matplotlib.pyplot as plt
# %matplotlib inline

# # detectron2 utilities
# from detectron2 import model_zoo
# from detectron2.engine import DefaultPredictor
# from detectron2.config import get_cfg
# from detectron2.utils.visualizer import Visualizer
# from detectron2.data import MetadataCatalog, DatasetCatalog
# from detectron2.structures import BoxMode

import os

import torch,gc
import sys
 
import detectron2.utils.comm as comm
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultTrainer, default_argument_parser, default_setup, launch
from detectron2.evaluation import (
#     CityscapesEvaluator,
    COCOEvaluator,
    DatasetEvaluators,
    LVISEvaluator,
    verify_results,
)
 
from detectron2.projects.point_rend import add_pointrend_config
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.datasets.coco import load_coco_json
from detectron2.data.datasets import register_coco_instances
import pycocotools

sys.argv = ['']


#声明类别，尽量保持
CLASS_NAMES =["_background_","fodder"]
 
TRAIN_PATH = r"/kaggle/input/img-annotation/img"
VAL_PATH = r"/kaggle/input/img-annotation/img"

TRAIN_JSON = r"/kaggle/working/img_coco/train.json"
VAL_JSON = r"/kaggle/working/img_coco/val.json" 

# 声明数据集的子集
PREDEFINED_SPLITS_DATASET = {
    "train": (TRAIN_PATH, TRAIN_JSON),
    "val": (VAL_PATH, VAL_JSON),
}
 
# 注册数据集和元数据
def plain_register_dataset():
    #训练集
    register_coco_instances("train", {}, TRAIN_JSON, TRAIN_PATH)
 
    #验证/测试集
    register_coco_instances("val", {}, VAL_JSON, VAL_PATH)
 
 
class Trainer(DefaultTrainer):
    """
    We use the "DefaultTrainer" which contains a number pre-defined logic for
    standard training workflow. They may not work for you, especially if you
    are working on a new research project. In that case you can use the cleaner
    "SimpleTrainer", or write your own training loop.
    """
 
    @classmethod
    def build_evaluator(cls, cfg, dataset_name, output_folder=None):
        """
        Create evaluator(s) for a given dataset.
        This uses the special metadata "evaluator_type" associated with each builtin dataset.
        For your own dataset, you can simply create an evaluator manually in your
        script and do not have to worry about the hacky if-else logic here.
        """
        if output_folder is None:
            output_folder = os.path.join(cfg.OUTPUT_DIR, "inference")
        evaluator_list = []
        evaluator_type = MetadataCatalog.get(dataset_name).evaluator_type
        if evaluator_type == "lvis":
            return LVISEvaluator(dataset_name, cfg, True, output_folder)
        if evaluator_type == "coco":
            return COCOEvaluator(dataset_name, cfg, True, output_folder)
#         if evaluator_type == "cityscapes":
#             assert (
#                 torch.cuda.device_count() >= comm.get_rank()
#             ), "CityscapesEvaluator currently do not work with multiple machines."
#             return CityscapesEvaluator(dataset_name)
        if len(evaluator_list) == 0:
            raise NotImplementedError(
                "no Evaluator for the dataset {} with the type {}".format(
                    dataset_name, evaluator_type
                )
            )
        if len(evaluator_list) == 1:
            return evaluator_list[0]
        return DatasetEvaluators(evaluator_list)
    
def setup(args):
    """
    Create configs and perform basic setups.
    """
    cfg = get_cfg()
    add_pointrend_config(cfg)
    args.config_file = r"/kaggle/working/detectron2/projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco.yaml"
    cfg.merge_from_file(args.config_file)   # 从config file 覆盖配置
#     cfg.merge_from_list(args.opts)          # 从CLI参数 覆盖配置
#     cfg.MODEL.DEVICE = "cuda"
    # 更改配置参数
    cfg.DATASETS.TRAIN = ("train",) # 训练数据集名称
    cfg.DATASETS.TEST = ("val",)
    cfg.DATALOADER.NUM_WORKERS = 1  # 单线程
    #cfg.INPUT.CROP.ENABLED = True
    cfg.INPUT.MAX_SIZE_TRAIN = 3840 # 训练图片输入的最大尺寸
    cfg.INPUT.MAX_SIZE_TEST  = 3840 # 测试数据输入的最大尺寸
    cfg.INPUT.MIN_SIZE_TRAIN = (3840, 3840) # 训练图片输入的最小尺寸，可以设定为多尺度训练
    cfg.INPUT.MIN_SIZE_TEST  = 3840
    #cfg.INPUT.MIN_SIZE_TRAIN_SAMPLING，其存在两种配置，分别为 choice 与 range ：
    # range 让图像的短边从 512-768随机选择
    #choice ： 把输入图像转化为指定的，有限的几种图片大小进行训练，即短边只能为 512或者768
    cfg.INPUT.MIN_SIZE_TRAIN_SAMPLING = 'range'
    cfg.OUTPUT_DIR = '/kaggle/working/output'
    cfg.MODEL.RETINANET.NUM_CLASSES = 2  # 类别数+1（因为有background）
    #cfg.MODEL.WEIGHTS="/home/yourstorePath/.pth"
    cfg.MODEL.WEIGHTS = r"/kaggle/input/model-final-edd263pkl/model_final_edd263.pkl"    # 预训练模型权重
    cfg.SOLVER.IMS_PER_BATCH = 2  # batch_size=2; iters_in_one_epoch = dataset_imgs/batch_size
#     cfg.MODEL.DEVICE = "cuda"
    # 根据训练数据总数目以及batch_size，计算出每个epoch需要的迭代次数
    #9000为你的训练数据的总数目，可自定义
    ITERS_IN_ONE_EPOCH = int(44 / cfg.SOLVER.IMS_PER_BATCH)
 
    # 指定最大迭代次数
    cfg.SOLVER.MAX_ITER = (ITERS_IN_ONE_EPOCH * 12) - 1 # 12 epochs，
    # 初始学习率
    cfg.SOLVER.BASE_LR = 0.002
    # 优化器动能
    cfg.SOLVER.MOMENTUM = 0.9
    #权重衰减
    cfg.SOLVER.WEIGHT_DECAY = 0.0001
    cfg.SOLVER.WEIGHT_DECAY_NORM = 0.0
    # 学习率衰减倍数
    cfg.SOLVER.GAMMA = 0.1
    # 迭代到指定次数，学习率进行衰减
    cfg.SOLVER.STEPS = (7000,)
    # 在训练之前，会做一个热身运动，学习率慢慢增加初始学习率
    cfg.SOLVER.WARMUP_FACTOR = 1.0 / 1000
    # 热身迭代次数
    cfg.SOLVER.WARMUP_ITERS = 1000
 
    cfg.SOLVER.WARMUP_METHOD = "linear"
    # 保存模型文件的命名数据减1
    cfg.SOLVER.CHECKPOINT_PERIOD = ITERS_IN_ONE_EPOCH - 1
 
    # 迭代到指定次数，进行一次评估
    cfg.TEST.EVAL_PERIOD = ITERS_IN_ONE_EPOCH
    #cfg.TEST.EVAL_PERIOD = 100
 
    #cfg.merge_from_file(args.config_file)
    #cfg.merge_from_list(args.opts)
    cfg.freeze()
    
#     default_setup(cfg, args)
    return cfg
    
def main(args):
#     DatasetCatalog.clear()
#     plain_register_dataset()
    cfg = setup(args)
    model = Trainer.build_model(cfg)
    model = torch.nn.DataParallel(model)
    DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
        cfg.MODEL.WEIGHTS, resume=False
    )
#     res = Trainer.test(cfg, model)
#         if comm.is_main_process():
#             verify_results(cfg, res)
#         return res
 
    trainer = Trainer(cfg)
    trainer.resume_or_load(resume=False)
    return trainer.train()

 

args = default_argument_parser().parse_args()
# args.num_gpus = 2
#     args = {'config_file':'','opts':'[]',}
print("Command Line Args:",args)
    
# main(args)
launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )