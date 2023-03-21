# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        #MainWindow.resize(1259, 768)
        MainWindow.setFixedSize(1259, 768)
        MainWindow.setMouseTracking(True)
        icon = QIcon()
        iconThemeName = u"camera-video"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1271, 741))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-10, -20, 911, 731))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(211, 215, 207);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(186, 189, 182);\n"
"background-color: rgb(211, 215, 207);")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(211, 215, 207);")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(211, 215, 207);")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(900, 0, 361, 711))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_launch = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_launch.setObjectName(u"pushButton_launch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_launch.sizePolicy().hasHeightForWidth())
        self.pushButton_launch.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_launch)

        self.pushButton_start = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy1.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_start)

        self.pushButton_view_result = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_view_result.setObjectName(u"pushButton_view_result")
        sizePolicy1.setHeightForWidth(self.pushButton_view_result.sizePolicy().hasHeightForWidth())
        self.pushButton_view_result.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_view_result)

        self.pushButton_close = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy1.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_close)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-color: rgb(138, 226, 52);")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_3 = QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 841, 721))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(211, 215, 207);")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(211, 215, 207);")

        self.verticalLayout_3.addWidget(self.label_5)

        self.verticalLayoutWidget_4 = QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(840, 0, 411, 701))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_navigation_close = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_navigation_close.setObjectName(u"pushButton_navigation_close")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_navigation_close.sizePolicy().hasHeightForWidth())
        self.pushButton_navigation_close.setSizePolicy(sizePolicy3)
        self.pushButton_navigation_close.setMinimumSize(QSize(0, 100))

        self.verticalLayout_4.addWidget(self.pushButton_navigation_close)

        self.pushButton_view_road = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_view_road.setObjectName(u"pushButton_view_road")
        self.pushButton_view_road.setMinimumSize(QSize(0, 100))

        self.verticalLayout_4.addWidget(self.pushButton_view_road)

        self.pushButton = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))

        self.verticalLayout_4.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableView = QTableView(self.tab_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 1031, 711))
        self.verticalLayoutWidget_5 = QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(1030, 170, 231, 521))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_display_table = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_display_table.setObjectName(u"pushButton_display_table")
        sizePolicy3.setHeightForWidth(self.pushButton_display_table.sizePolicy().hasHeightForWidth())
        self.pushButton_display_table.setSizePolicy(sizePolicy3)
        self.pushButton_display_table.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.pushButton_display_table)

        self.pushButton_choose_table = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_choose_table.setObjectName(u"pushButton_choose_table")
        self.pushButton_choose_table.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.pushButton_choose_table)

        self.pushButton_clear = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.pushButton_clear)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1259, 32))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton_launch.setText(QCoreApplication.translate("MainWindow", u"LAUNCH", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_view_result.setText(QCoreApplication.translate("MainWindow", u"VIEW_RESULT", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Detection", None))
        self.label_6.setText("")
        self.label_5.setText("")
        self.pushButton_navigation_close.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.pushButton_view_road.setText(QCoreApplication.translate("MainWindow", u"VIEW_ROAD", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CONTINUE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.pushButton_display_table.setText(QCoreApplication.translate("MainWindow", u"DISPLAY TABLE", None))
        self.pushButton_choose_table.setText(QCoreApplication.translate("MainWindow", u"CHOOSE TABLE", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"CLEAR ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

