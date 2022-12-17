# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 629)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setCursor(QCursor(Qt.OpenHandCursor))
        self.header.setStyleSheet(u"QFrame{\n"
"	background: #0C508B;\n"
"}\n"
"\n"
"")
        self.header.setFrameShape(QFrame.WinPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.menu_btn = QPushButton(self.header)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(30, 30))
        self.menu_btn.setMaximumSize(QSize(30, 30))
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images_icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(28, 29))

        self.horizontalLayout_4.addWidget(self.menu_btn)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(110, 16777215))
        self.label.setPixmap(QPixmap(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/dorsa_white.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background:white")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.minimize_btn = QPushButton(self.frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(0, 0))
        self.minimize_btn.setMaximumSize(QSize(16777215, 16777215))
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(0, 0))
        self.maximize_btn.setMaximumSize(QSize(16777215, 16777215))
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximize_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/cil-rectangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 0))
        self.close_btn.setMaximumSize(QSize(16777215, 16777215))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #F70000;\n"
" }")
        icon3 = QIcon()
        icon3.addFile(u"icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.close_btn)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.header)

        self.middle = QFrame(self.centralwidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setFrameShape(QFrame.NoFrame)
        self.middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.middle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menubar_frame = QFrame(self.middle)
        self.menubar_frame.setObjectName(u"menubar_frame")
        self.menubar_frame.setMinimumSize(QSize(0, 44))
        self.menubar_frame.setMaximumSize(QSize(16777215, 44))
        self.menubar_frame.setStyleSheet(u"QFrame{\n"
"	background:#4649FF;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.menubar_frame.setFrameShape(QFrame.NoFrame)
        self.menubar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menubar_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.BTN_dashboard = QPushButton(self.menubar_frame)
        self.BTN_dashboard.setObjectName(u"BTN_dashboard")
        self.BTN_dashboard.setMinimumSize(QSize(0, 0))
        self.BTN_dashboard.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.BTN_dashboard.setFont(font1)
        self.BTN_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_dashboard.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_dashboard.setIcon(icon4)
        self.BTN_dashboard.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_dashboard)

        self.BTN_camera_setting = QPushButton(self.menubar_frame)
        self.BTN_camera_setting.setObjectName(u"BTN_camera_setting")
        self.BTN_camera_setting.setMinimumSize(QSize(0, 0))
        self.BTN_camera_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_setting.setFont(font1)
        self.BTN_camera_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_setting.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/camera_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_setting.setIcon(icon5)
        self.BTN_camera_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_camera_setting)

        self.BTN_general_setting = QPushButton(self.menubar_frame)
        self.BTN_general_setting.setObjectName(u"BTN_general_setting")
        self.BTN_general_setting.setEnabled(False)
        self.BTN_general_setting.setMinimumSize(QSize(0, 0))
        self.BTN_general_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_general_setting.setFont(font1)
        self.BTN_general_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_general_setting.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/general_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_general_setting.setIcon(icon6)
        self.BTN_general_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_general_setting)

        self.BTN_history = QPushButton(self.menubar_frame)
        self.BTN_history.setObjectName(u"BTN_history")
        self.BTN_history.setMinimumSize(QSize(0, 0))
        self.BTN_history.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_history.setFont(font1)
        self.BTN_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_history.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/algorithm_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_history.setIcon(icon7)
        self.BTN_history.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_history)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.menubar_frame)

        self.main_frame = QFrame(self.middle)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(1, 1))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #8BBCCC;")
        self.general_setting = QWidget()
        self.general_setting.setObjectName(u"general_setting")
        self.verticalLayout_35 = QVBoxLayout(self.general_setting)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.general_setting)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider)

        self.spinBox = QSpinBox(self.frame_4)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_15.addWidget(self.spinBox)


        self.verticalLayout_35.addWidget(self.frame_4)

        self.frame_17 = QFrame(self.general_setting)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.horizontalSlider_3 = QSlider(self.frame_17)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.horizontalSlider_3)

        self.spinBox_2 = QSpinBox(self.frame_17)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_16.addWidget(self.spinBox_2)


        self.verticalLayout_35.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.general_setting)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.horizontalSlider_4 = QSlider(self.frame_18)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.horizontalSlider_4)

        self.spinBox_3 = QSpinBox(self.frame_18)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_17.addWidget(self.spinBox_3)


        self.verticalLayout_35.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.general_setting)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.horizontalSlider_5 = QSlider(self.frame_19)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.horizontalLayout_18.addWidget(self.horizontalSlider_5)

        self.spinBox_4 = QSpinBox(self.frame_19)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.horizontalLayout_18.addWidget(self.spinBox_4)


        self.verticalLayout_35.addWidget(self.frame_19)

        self.frame_3 = QFrame(self.general_setting)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 250))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_35.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.general_setting)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.horizontalLayout_7 = QHBoxLayout(self.Dashboard)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.Dashboard)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_live_btn = QPushButton(self.frame_7)
        self.camera_live_btn.setObjectName(u"camera_live_btn")
        self.camera_live_btn.setMinimumSize(QSize(0, 22))
        self.camera_live_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"images_icon/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera_live_btn.setIcon(icon8)
        self.camera_live_btn.setIconSize(QSize(47, 16))

        self.verticalLayout_7.addWidget(self.camera_live_btn)

        self.BTN_scane_start = QPushButton(self.frame_7)
        self.BTN_scane_start.setObjectName(u"BTN_scane_start")
        self.BTN_scane_start.setEnabled(True)
        self.BTN_scane_start.setMinimumSize(QSize(0, 0))
        self.BTN_scane_start.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.BTN_scane_start.setFont(font2)
        self.BTN_scane_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_scane_start.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"icons/scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_scane_start.setIcon(icon9)
        self.BTN_scane_start.setIconSize(QSize(30, 35))

        self.verticalLayout_7.addWidget(self.BTN_scane_start)

        self.BTN_scan_stop = QPushButton(self.frame_7)
        self.BTN_scan_stop.setObjectName(u"BTN_scan_stop")
        self.BTN_scan_stop.setEnabled(False)
        self.BTN_scan_stop.setMinimumSize(QSize(0, 0))
        self.BTN_scan_stop.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_scan_stop.setFont(font2)
        self.BTN_scan_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_scan_stop.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u"icons/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_scan_stop.setIcon(icon10)
        self.BTN_scan_stop.setIconSize(QSize(30, 35))

        self.verticalLayout_7.addWidget(self.BTN_scan_stop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.line_2 = QFrame(self.Dashboard)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.frame_6 = QFrame(self.Dashboard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 21)
        self.scrollArea = QScrollArea(self.frame_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 763, 227))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.LBL_live_camera = QLabel(self.scrollAreaWidgetContents_2)
        self.LBL_live_camera.setObjectName(u"LBL_live_camera")
        self.LBL_live_camera.setFrameShape(QFrame.Box)
        self.LBL_live_camera.setScaledContents(False)

        self.verticalLayout_10.addWidget(self.LBL_live_camera)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.frame_79 = QFrame(self.frame_6)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 200))
        self.frame_79.setFrameShape(QFrame.Panel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.defects_prev_btn = QPushButton(self.frame_79)
        self.defects_prev_btn.setObjectName(u"defects_prev_btn")
        self.defects_prev_btn.setEnabled(True)
        self.defects_prev_btn.setMinimumSize(QSize(30, 30))
        self.defects_prev_btn.setMaximumSize(QSize(30, 30))
        self.defects_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.defects_prev_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        icon11 = QIcon()
        icon11.addFile(u"images_icon/arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defects_prev_btn.setIcon(icon11)
        self.defects_prev_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.defects_prev_btn)

        self.defects_list_slider_frame = QLabel(self.frame_79)
        self.defects_list_slider_frame.setObjectName(u"defects_list_slider_frame")
        self.defects_list_slider_frame.setFrameShape(QFrame.Panel)
        self.defects_list_slider_frame.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.defects_list_slider_frame)

        self.defects_next_btn = QPushButton(self.frame_79)
        self.defects_next_btn.setObjectName(u"defects_next_btn")
        self.defects_next_btn.setEnabled(True)
        self.defects_next_btn.setMinimumSize(QSize(30, 30))
        self.defects_next_btn.setMaximumSize(QSize(30, 30))
        self.defects_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.defects_next_btn.setStyleSheet(u"background-color:Transparent;\n"
"border:Transparent")
        icon12 = QIcon()
        icon12.addFile(u"images_icon/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defects_next_btn.setIcon(icon12)
        self.defects_next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.defects_next_btn)


        self.verticalLayout_9.addWidget(self.frame_79)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.Dashboard)
        self.camera_settings = QWidget()
        self.camera_settings.setObjectName(u"camera_settings")
        self.horizontalLayout_24 = QHBoxLayout(self.camera_settings)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.frame_12 = QFrame(self.camera_settings)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(310, 0))
        self.frame_12.setMaximumSize(QSize(310, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 30)
        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.frame_9)

        self.tabWidget = QTabWidget(self.frame_12)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sett_cam_scrollArea = QScrollArea(self.tab)
        self.sett_cam_scrollArea.setObjectName(u"sett_cam_scrollArea")
        self.sett_cam_scrollArea.setEnabled(True)
        self.sett_cam_scrollArea.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.sett_cam_scrollArea.setFrameShape(QFrame.Box)
        self.sett_cam_scrollArea.setFrameShadow(QFrame.Raised)
        self.sett_cam_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 244, 437))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gain_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.gain_label_2.setObjectName(u"gain_label_2")
        self.gain_label_2.setMinimumSize(QSize(0, 30))
        self.gain_label_2.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.gain_label_2.setFont(font3)

        self.verticalLayout_11.addWidget(self.gain_label_2)

        self.expo_label = QLabel(self.scrollAreaWidgetContents)
        self.expo_label.setObjectName(u"expo_label")
        self.expo_label.setMinimumSize(QSize(0, 30))
        self.expo_label.setMaximumSize(QSize(16777215, 30))
        self.expo_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.expo_label)

        self.gain_label = QLabel(self.scrollAreaWidgetContents)
        self.gain_label.setObjectName(u"gain_label")
        self.gain_label.setMinimumSize(QSize(0, 30))
        self.gain_label.setMaximumSize(QSize(16777215, 30))
        self.gain_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.gain_label)

        self.width_label = QLabel(self.scrollAreaWidgetContents)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setMinimumSize(QSize(0, 30))
        self.width_label.setMaximumSize(QSize(16777215, 30))
        self.width_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.width_label)

        self.height_label = QLabel(self.scrollAreaWidgetContents)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setMinimumSize(QSize(0, 30))
        self.height_label.setMaximumSize(QSize(16777215, 30))
        self.height_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.height_label)

        self.offsetx_label = QLabel(self.scrollAreaWidgetContents)
        self.offsetx_label.setObjectName(u"offsetx_label")
        self.offsetx_label.setMinimumSize(QSize(0, 30))
        self.offsetx_label.setMaximumSize(QSize(16777215, 30))
        self.offsetx_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.offsetx_label)

        self.offsety_label = QLabel(self.scrollAreaWidgetContents)
        self.offsety_label.setObjectName(u"offsety_label")
        self.offsety_label.setMinimumSize(QSize(0, 30))
        self.offsety_label.setMaximumSize(QSize(16777215, 30))
        self.offsety_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.offsety_label)

        self.trigger_label = QLabel(self.scrollAreaWidgetContents)
        self.trigger_label.setObjectName(u"trigger_label")
        self.trigger_label.setMinimumSize(QSize(0, 30))
        self.trigger_label.setMaximumSize(QSize(16777215, 30))
        self.trigger_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.trigger_label)

        self.maxbuffer_label = QLabel(self.scrollAreaWidgetContents)
        self.maxbuffer_label.setObjectName(u"maxbuffer_label")
        self.maxbuffer_label.setMinimumSize(QSize(0, 30))
        self.maxbuffer_label.setMaximumSize(QSize(16777215, 30))
        self.maxbuffer_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.maxbuffer_label)

        self.packetdelay_label = QLabel(self.scrollAreaWidgetContents)
        self.packetdelay_label.setObjectName(u"packetdelay_label")
        self.packetdelay_label.setMinimumSize(QSize(0, 30))
        self.packetdelay_label.setMaximumSize(QSize(16777215, 30))
        self.packetdelay_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.packetdelay_label)

        self.packetsize_label = QLabel(self.scrollAreaWidgetContents)
        self.packetsize_label.setObjectName(u"packetsize_label")
        self.packetsize_label.setMinimumSize(QSize(0, 30))
        self.packetsize_label.setMaximumSize(QSize(16777215, 30))
        self.packetsize_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.packetsize_label)

        self.transmissiondelay_label = QLabel(self.scrollAreaWidgetContents)
        self.transmissiondelay_label.setObjectName(u"transmissiondelay_label")
        self.transmissiondelay_label.setMinimumSize(QSize(0, 30))
        self.transmissiondelay_label.setMaximumSize(QSize(16777215, 30))
        self.transmissiondelay_label.setFont(font3)

        self.verticalLayout_11.addWidget(self.transmissiondelay_label)


        self.horizontalLayout_20.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.serial_number_combo = QComboBox(self.scrollAreaWidgetContents)
        self.serial_number_combo.setObjectName(u"serial_number_combo")
        self.serial_number_combo.setEnabled(True)
        self.serial_number_combo.setMinimumSize(QSize(0, 30))
        self.serial_number_combo.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.serial_number_combo.setFont(font4)
        self.serial_number_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.serial_number_combo)

        self.setting_refresh_available_cams_btn = QPushButton(self.scrollAreaWidgetContents)
        self.setting_refresh_available_cams_btn.setObjectName(u"setting_refresh_available_cams_btn")
        self.setting_refresh_available_cams_btn.setMinimumSize(QSize(0, 30))
        self.setting_refresh_available_cams_btn.setMaximumSize(QSize(22, 30))
        self.setting_refresh_available_cams_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_refresh_available_cams_btn.setStyleSheet(u"QPushButton{\n"
"	background: #E1E1E1;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background:#a3a3a3;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../icons/refresh(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_refresh_available_cams_btn.setIcon(icon13)

        self.horizontalLayout_22.addWidget(self.setting_refresh_available_cams_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.expo_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setEnabled(True)
        self.expo_spinbox.setMinimumSize(QSize(0, 30))
        self.expo_spinbox.setMaximumSize(QSize(16777215, 30))
        palette = QPalette()
        brush = QBrush(QColor(139, 188, 204, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush3 = QBrush(QColor(0, 120, 215, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.expo_spinbox.setPalette(palette)
        self.expo_spinbox.setFont(font4)
        self.expo_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.expo_spinbox.setAlignment(Qt.AlignCenter)
        self.expo_spinbox.setMaximum(20000)
        self.expo_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.expo_spinbox)

        self.gain_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.gain_spinbox.setObjectName(u"gain_spinbox")
        self.gain_spinbox.setEnabled(True)
        self.gain_spinbox.setMinimumSize(QSize(0, 30))
        self.gain_spinbox.setMaximumSize(QSize(16777215, 30))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.gain_spinbox.setPalette(palette1)
        self.gain_spinbox.setFont(font4)
        self.gain_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.gain_spinbox.setAlignment(Qt.AlignCenter)
        self.gain_spinbox.setMinimum(0)
        self.gain_spinbox.setMaximum(300)
        self.gain_spinbox.setSingleStep(1)
        self.gain_spinbox.setValue(300)

        self.verticalLayout_12.addWidget(self.gain_spinbox)

        self.width_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.width_spinbox.setObjectName(u"width_spinbox")
        self.width_spinbox.setEnabled(True)
        self.width_spinbox.setMinimumSize(QSize(0, 30))
        self.width_spinbox.setMaximumSize(QSize(16777215, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.width_spinbox.setPalette(palette2)
        self.width_spinbox.setFont(font4)
        self.width_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.width_spinbox.setAlignment(Qt.AlignCenter)
        self.width_spinbox.setMinimum(0)
        self.width_spinbox.setMaximum(3840)
        self.width_spinbox.setSingleStep(1)
        self.width_spinbox.setValue(1920)

        self.verticalLayout_12.addWidget(self.width_spinbox)

        self.height_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setEnabled(True)
        self.height_spinbox.setMinimumSize(QSize(0, 30))
        self.height_spinbox.setMaximumSize(QSize(16777215, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.height_spinbox.setPalette(palette3)
        self.height_spinbox.setFont(font4)
        self.height_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.height_spinbox.setAlignment(Qt.AlignCenter)
        self.height_spinbox.setMinimum(0)
        self.height_spinbox.setMaximum(1200)
        self.height_spinbox.setSingleStep(1)
        self.height_spinbox.setValue(1200)

        self.verticalLayout_12.addWidget(self.height_spinbox)

        self.offsetx_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.offsetx_spinbox.setObjectName(u"offsetx_spinbox")
        self.offsetx_spinbox.setEnabled(True)
        self.offsetx_spinbox.setMinimumSize(QSize(0, 30))
        self.offsetx_spinbox.setMaximumSize(QSize(16777215, 30))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.offsetx_spinbox.setPalette(palette4)
        self.offsetx_spinbox.setFont(font4)
        self.offsetx_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsetx_spinbox.setAlignment(Qt.AlignCenter)
        self.offsetx_spinbox.setMaximum(1920)
        self.offsetx_spinbox.setSingleStep(4)

        self.verticalLayout_12.addWidget(self.offsetx_spinbox)

        self.offsety_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setEnabled(True)
        self.offsety_spinbox.setMinimumSize(QSize(0, 30))
        self.offsety_spinbox.setMaximumSize(QSize(16777215, 30))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.offsety_spinbox.setPalette(palette5)
        self.offsety_spinbox.setFont(font4)
        self.offsety_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsety_spinbox.setAlignment(Qt.AlignCenter)
        self.offsety_spinbox.setMaximum(1200)
        self.offsety_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.offsety_spinbox)

        self.trigger_combo = QComboBox(self.scrollAreaWidgetContents)
        self.trigger_combo.addItem("")
        self.trigger_combo.addItem("")
        self.trigger_combo.addItem("")
        self.trigger_combo.setObjectName(u"trigger_combo")
        self.trigger_combo.setEnabled(True)
        self.trigger_combo.setMinimumSize(QSize(0, 30))
        self.trigger_combo.setMaximumSize(QSize(16777215, 30))
        self.trigger_combo.setFont(font4)
        self.trigger_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.trigger_combo.setLayoutDirection(Qt.LeftToRight)
        self.trigger_combo.setStyleSheet(u"")
        self.trigger_combo.setEditable(False)

        self.verticalLayout_12.addWidget(self.trigger_combo)

        self.maxbuffer_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.maxbuffer_spinbox.setObjectName(u"maxbuffer_spinbox")
        self.maxbuffer_spinbox.setEnabled(True)
        self.maxbuffer_spinbox.setMinimumSize(QSize(0, 30))
        self.maxbuffer_spinbox.setMaximumSize(QSize(16777215, 30))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.maxbuffer_spinbox.setPalette(palette6)
        self.maxbuffer_spinbox.setFont(font4)
        self.maxbuffer_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxbuffer_spinbox.setAlignment(Qt.AlignCenter)
        self.maxbuffer_spinbox.setMaximum(10000)
        self.maxbuffer_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.maxbuffer_spinbox)

        self.packetdelay_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.packetdelay_spinbox.setObjectName(u"packetdelay_spinbox")
        self.packetdelay_spinbox.setEnabled(True)
        self.packetdelay_spinbox.setMinimumSize(QSize(0, 30))
        self.packetdelay_spinbox.setMaximumSize(QSize(16777215, 30))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.packetdelay_spinbox.setPalette(palette7)
        self.packetdelay_spinbox.setFont(font4)
        self.packetdelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetdelay_spinbox.setAlignment(Qt.AlignCenter)
        self.packetdelay_spinbox.setMaximum(10000)
        self.packetdelay_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.packetdelay_spinbox)

        self.packetsize_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.packetsize_spinbox.setObjectName(u"packetsize_spinbox")
        self.packetsize_spinbox.setEnabled(True)
        self.packetsize_spinbox.setMinimumSize(QSize(0, 30))
        self.packetsize_spinbox.setMaximumSize(QSize(16777215, 30))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette8.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.packetsize_spinbox.setPalette(palette8)
        self.packetsize_spinbox.setFont(font4)
        self.packetsize_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.packetsize_spinbox.setAlignment(Qt.AlignCenter)
        self.packetsize_spinbox.setMaximum(10000)
        self.packetsize_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.packetsize_spinbox)

        self.transmissiondelay_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.transmissiondelay_spinbox.setObjectName(u"transmissiondelay_spinbox")
        self.transmissiondelay_spinbox.setEnabled(True)
        self.transmissiondelay_spinbox.setMinimumSize(QSize(0, 30))
        self.transmissiondelay_spinbox.setMaximumSize(QSize(16777215, 30))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette9.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Highlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        self.transmissiondelay_spinbox.setPalette(palette9)
        self.transmissiondelay_spinbox.setFont(font4)
        self.transmissiondelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.transmissiondelay_spinbox.setAlignment(Qt.AlignCenter)
        self.transmissiondelay_spinbox.setMaximum(10000)
        self.transmissiondelay_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.transmissiondelay_spinbox)


        self.horizontalLayout_20.addLayout(self.verticalLayout_12)

        self.sett_cam_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.sett_cam_scrollArea)

        self.BTN_camera_setting_apply = QPushButton(self.tab)
        self.BTN_camera_setting_apply.setObjectName(u"BTN_camera_setting_apply")
        self.BTN_camera_setting_apply.setMinimumSize(QSize(0, 35))
        self.BTN_camera_setting_apply.setFont(font2)
        self.BTN_camera_setting_apply.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_setting_apply.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/apply_params.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_setting_apply.setIcon(icon14)
        self.BTN_camera_setting_apply.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.BTN_camera_setting_apply)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.tab_2)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.Panel)
        self.scrollArea_4.setFrameShadow(QFrame.Raised)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 302, 158))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_20 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(17, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_20)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.checkBox_th_1 = QCheckBox(self.frame_20)
        self.checkBox_th_1.setObjectName(u"checkBox_th_1")

        self.verticalLayout_29.addWidget(self.checkBox_th_1)

        self.checkBox_th_2 = QCheckBox(self.frame_20)
        self.checkBox_th_2.setObjectName(u"checkBox_th_2")

        self.verticalLayout_29.addWidget(self.checkBox_th_2)

        self.checkBox_median_1 = QCheckBox(self.frame_20)
        self.checkBox_median_1.setObjectName(u"checkBox_median_1")

        self.verticalLayout_29.addWidget(self.checkBox_median_1)

        self.checkBox_median_2 = QCheckBox(self.frame_20)
        self.checkBox_median_2.setObjectName(u"checkBox_median_2")

        self.verticalLayout_29.addWidget(self.checkBox_median_2)


        self.horizontalLayout_14.addWidget(self.frame_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.LBL_laserDTH_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.LBL_laserDTH_2.setObjectName(u"LBL_laserDTH_2")
        self.LBL_laserDTH_2.setMinimumSize(QSize(0, 30))
        self.LBL_laserDTH_2.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(10)
        self.LBL_laserDTH_2.setFont(font5)

        self.verticalLayout_19.addWidget(self.LBL_laserDTH_2)

        self.L_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.L_2.setObjectName(u"L_2")
        self.L_2.setMinimumSize(QSize(0, 30))
        self.L_2.setMaximumSize(QSize(16777215, 30))
        self.L_2.setFont(font5)

        self.verticalLayout_19.addWidget(self.L_2)

        self.LBL_norm_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.LBL_norm_2.setObjectName(u"LBL_norm_2")
        self.LBL_norm_2.setMinimumSize(QSize(0, 30))
        self.LBL_norm_2.setMaximumSize(QSize(16777215, 30))
        self.LBL_norm_2.setFont(font5)

        self.verticalLayout_19.addWidget(self.LBL_norm_2)

        self.LBL_th1_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.LBL_th1_2.setObjectName(u"LBL_th1_2")
        self.LBL_th1_2.setMinimumSize(QSize(0, 30))
        self.LBL_th1_2.setMaximumSize(QSize(16777215, 30))
        self.LBL_th1_2.setFont(font5)

        self.verticalLayout_19.addWidget(self.LBL_th1_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_19)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalSlider_2 = QSlider(self.scrollAreaWidgetContents_5)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.horizontalSlider_2)

        self.horizontalSlider_8 = QSlider(self.scrollAreaWidgetContents_5)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.horizontalSlider_8)

        self.horizontalSlider_6 = QSlider(self.scrollAreaWidgetContents_5)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.horizontalSlider_6)

        self.horizontalSlider_7 = QSlider(self.scrollAreaWidgetContents_5)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.horizontalSlider_7)


        self.horizontalLayout_14.addLayout(self.verticalLayout_23)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.spinBox_laserDTH_2 = QSpinBox(self.scrollAreaWidgetContents_5)
        self.spinBox_laserDTH_2.setObjectName(u"spinBox_laserDTH_2")

        self.verticalLayout_22.addWidget(self.spinBox_laserDTH_2)

        self.threshold_2_spin = QSpinBox(self.scrollAreaWidgetContents_5)
        self.threshold_2_spin.setObjectName(u"threshold_2_spin")

        self.verticalLayout_22.addWidget(self.threshold_2_spin)

        self.median_1_spin = QSpinBox(self.scrollAreaWidgetContents_5)
        self.median_1_spin.setObjectName(u"median_1_spin")
        self.median_1_spin.setMinimum(1)
        self.median_1_spin.setSingleStep(2)

        self.verticalLayout_22.addWidget(self.median_1_spin)

        self.median_2_spin = QSpinBox(self.scrollAreaWidgetContents_5)
        self.median_2_spin.setObjectName(u"median_2_spin")
        self.median_2_spin.setMinimum(1)
        self.median_2_spin.setSingleStep(2)

        self.verticalLayout_22.addWidget(self.median_2_spin)


        self.horizontalLayout_14.addLayout(self.verticalLayout_22)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_8.addWidget(self.scrollArea_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.spinBox_f_r = QSpinBox(self.frame_8)
        self.spinBox_f_r.setObjectName(u"spinBox_f_r")

        self.horizontalLayout_6.addWidget(self.spinBox_f_r)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.tab_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.spinBox_l_s = QSpinBox(self.frame_10)
        self.spinBox_l_s.setObjectName(u"spinBox_l_s")

        self.horizontalLayout_8.addWidget(self.spinBox_l_s)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.label_width_p_value = QLabel(self.frame_11)
        self.label_width_p_value.setObjectName(u"label_width_p_value")
        self.label_width_p_value.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_11.addWidget(self.label_width_p_value)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_11.addWidget(self.label_7)

        self.spinBox_pixel_value = QSpinBox(self.frame_11)
        self.spinBox_pixel_value.setObjectName(u"spinBox_pixel_value")

        self.horizontalLayout_11.addWidget(self.spinBox_pixel_value)

        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_11.addWidget(self.label_9)

        self.label_pixel_value = QLabel(self.frame_11)
        self.label_pixel_value.setObjectName(u"label_pixel_value")
        self.label_pixel_value.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_11.addWidget(self.label_pixel_value)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.brn_set_calib_parms = QPushButton(self.tab_2)
        self.brn_set_calib_parms.setObjectName(u"brn_set_calib_parms")
        self.brn_set_calib_parms.setMinimumSize(QSize(0, 35))
        self.brn_set_calib_parms.setMaximumSize(QSize(16777215, 35))
        self.brn_set_calib_parms.setFont(font2)
        self.brn_set_calib_parms.setCursor(QCursor(Qt.PointingHandCursor))
        self.brn_set_calib_parms.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.brn_set_calib_parms.setIcon(icon14)
        self.brn_set_calib_parms.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.brn_set_calib_parms)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_13.addWidget(self.tabWidget)


        self.horizontalLayout_24.addWidget(self.frame_12)

        self.groupBox_8 = QGroupBox(self.camera_settings)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font1)
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_44.setSpacing(5)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(10, 10, 10, 10)
        self.sett_cam_control_frame = QFrame(self.groupBox_8)
        self.sett_cam_control_frame.setObjectName(u"sett_cam_control_frame")
        self.sett_cam_control_frame.setEnabled(True)
        self.sett_cam_control_frame.setMinimumSize(QSize(0, 40))
        self.sett_cam_control_frame.setMaximumSize(QSize(16777215, 40))
        self.sett_cam_control_frame.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.sett_cam_control_frame.setFrameShape(QFrame.Box)
        self.sett_cam_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.sett_cam_control_frame)
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(10, 0, 10, 0)
        self.camera_calib_btn = QPushButton(self.sett_cam_control_frame)
        self.camera_calib_btn.setObjectName(u"camera_calib_btn")
        self.camera_calib_btn.setEnabled(True)
        self.camera_calib_btn.setMinimumSize(QSize(0, 0))
        self.camera_calib_btn.setMaximumSize(QSize(16777215, 16777215))
        self.camera_calib_btn.setFont(font2)
        self.camera_calib_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_calib_btn.setStyleSheet(u"")
        self.camera_calib_btn.setIcon(icon8)
        self.camera_calib_btn.setIconSize(QSize(51, 48))

        self.horizontalLayout_51.addWidget(self.camera_calib_btn)

        self.line_18 = QFrame(self.sett_cam_control_frame)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setMaximumSize(QSize(16777215, 25))
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_51.addWidget(self.line_18)

        self.BTN_camera_connect = QPushButton(self.sett_cam_control_frame)
        self.BTN_camera_connect.setObjectName(u"BTN_camera_connect")
        self.BTN_camera_connect.setEnabled(False)
        self.BTN_camera_connect.setMinimumSize(QSize(0, 0))
        self.BTN_camera_connect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_connect.setFont(font2)
        self.BTN_camera_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_connect.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u"images_icon/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_connect.setIcon(icon15)
        self.BTN_camera_connect.setIconSize(QSize(35, 35))

        self.horizontalLayout_51.addWidget(self.BTN_camera_connect)

        self.line_16 = QFrame(self.sett_cam_control_frame)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setMaximumSize(QSize(16777215, 25))
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_51.addWidget(self.line_16)

        self.BTN_camera_disconnect = QPushButton(self.sett_cam_control_frame)
        self.BTN_camera_disconnect.setObjectName(u"BTN_camera_disconnect")
        self.BTN_camera_disconnect.setEnabled(False)
        self.BTN_camera_disconnect.setMinimumSize(QSize(0, 0))
        self.BTN_camera_disconnect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_disconnect.setFont(font2)
        self.BTN_camera_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_disconnect.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u"images_icon/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_disconnect.setIcon(icon16)
        self.BTN_camera_disconnect.setIconSize(QSize(35, 35))

        self.horizontalLayout_51.addWidget(self.BTN_camera_disconnect)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_8)


        self.verticalLayout_44.addWidget(self.sett_cam_control_frame)

        self.sett_shot_frame = QFrame(self.groupBox_8)
        self.sett_shot_frame.setObjectName(u"sett_shot_frame")
        self.sett_shot_frame.setMinimumSize(QSize(0, 0))
        self.sett_shot_frame.setMaximumSize(QSize(16777215, 16777215))
        self.sett_shot_frame.setFrameShape(QFrame.WinPanel)
        self.sett_shot_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_15 = QVBoxLayout(self.sett_shot_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.sett_shot_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LBL_live_camera_for_setting_image_quality = QLabel(self.frame_2)
        self.LBL_live_camera_for_setting_image_quality.setObjectName(u"LBL_live_camera_for_setting_image_quality")
        self.LBL_live_camera_for_setting_image_quality.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.LBL_live_camera_for_setting_image_quality)


        self.verticalLayout_4.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addWidget(self.frame_2)

        self.calib_sett_result_frame_3 = QFrame(self.sett_shot_frame)
        self.calib_sett_result_frame_3.setObjectName(u"calib_sett_result_frame_3")
        self.calib_sett_result_frame_3.setFrameShape(QFrame.WinPanel)
        self.calib_sett_result_frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_26 = QVBoxLayout(self.calib_sett_result_frame_3)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.LBL_area_laser_detected_2 = QLabel(self.calib_sett_result_frame_3)
        self.LBL_area_laser_detected_2.setObjectName(u"LBL_area_laser_detected_2")
        self.LBL_area_laser_detected_2.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.LBL_area_laser_detected_2)


        self.verticalLayout_26.addLayout(self.verticalLayout_27)


        self.verticalLayout_15.addWidget(self.calib_sett_result_frame_3)

        self.calib_sett_result_frame_4 = QFrame(self.sett_shot_frame)
        self.calib_sett_result_frame_4.setObjectName(u"calib_sett_result_frame_4")
        self.calib_sett_result_frame_4.setFrameShape(QFrame.WinPanel)
        self.calib_sett_result_frame_4.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_30 = QVBoxLayout(self.calib_sett_result_frame_4)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.LBL_line_laser_detected_2 = QLabel(self.calib_sett_result_frame_4)
        self.LBL_line_laser_detected_2.setObjectName(u"LBL_line_laser_detected_2")
        self.LBL_line_laser_detected_2.setScaledContents(True)

        self.verticalLayout_31.addWidget(self.LBL_line_laser_detected_2)


        self.verticalLayout_30.addLayout(self.verticalLayout_31)


        self.verticalLayout_15.addWidget(self.calib_sett_result_frame_4)


        self.verticalLayout_44.addWidget(self.sett_shot_frame)

        self.frame_77 = QFrame(self.groupBox_8)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 40))
        self.frame_77.setMaximumSize(QSize(16777215, 40))
        self.frame_77.setFrameShape(QFrame.Box)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_50.setSpacing(10)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.gain_label_4 = QLabel(self.frame_77)
        self.gain_label_4.setObjectName(u"gain_label_4")
        self.gain_label_4.setMinimumSize(QSize(0, 0))
        self.gain_label_4.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_4.setFont(font3)

        self.horizontalLayout_23.addWidget(self.gain_label_4)

        self.sett_cam_temp = QLabel(self.frame_77)
        self.sett_cam_temp.setObjectName(u"sett_cam_temp")
        self.sett_cam_temp.setMinimumSize(QSize(0, 30))
        self.sett_cam_temp.setMaximumSize(QSize(16777215, 30))
        self.sett_cam_temp.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_cam_temp.setFrameShape(QFrame.Panel)
        self.sett_cam_temp.setFrameShadow(QFrame.Sunken)
        self.sett_cam_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.sett_cam_temp)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.gain_label_3 = QLabel(self.frame_77)
        self.gain_label_3.setObjectName(u"gain_label_3")
        self.gain_label_3.setMinimumSize(QSize(0, 0))
        self.gain_label_3.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_3.setFont(font3)

        self.horizontalLayout_19.addWidget(self.gain_label_3)

        self.sett_cam_fps = QLabel(self.frame_77)
        self.sett_cam_fps.setObjectName(u"sett_cam_fps")
        self.sett_cam_fps.setMinimumSize(QSize(0, 30))
        self.sett_cam_fps.setMaximumSize(QSize(16777215, 30))
        self.sett_cam_fps.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_cam_fps.setFrameShape(QFrame.Panel)
        self.sett_cam_fps.setFrameShadow(QFrame.Sunken)
        self.sett_cam_fps.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.sett_cam_fps)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.gain_label_5 = QLabel(self.frame_77)
        self.gain_label_5.setObjectName(u"gain_label_5")
        self.gain_label_5.setMinimumSize(QSize(0, 0))
        self.gain_label_5.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_5.setFont(font3)

        self.horizontalLayout_21.addWidget(self.gain_label_5)

        self.sett_cam_size = QLabel(self.frame_77)
        self.sett_cam_size.setObjectName(u"sett_cam_size")
        self.sett_cam_size.setMinimumSize(QSize(0, 30))
        self.sett_cam_size.setMaximumSize(QSize(16777215, 30))
        self.sett_cam_size.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_cam_size.setFrameShape(QFrame.Panel)
        self.sett_cam_size.setFrameShadow(QFrame.Sunken)
        self.sett_cam_size.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.sett_cam_size)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.gain_label_6 = QLabel(self.frame_77)
        self.gain_label_6.setObjectName(u"gain_label_6")
        self.gain_label_6.setMinimumSize(QSize(0, 0))
        self.gain_label_6.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_6.setFont(font3)

        self.horizontalLayout_25.addWidget(self.gain_label_6)

        self.sett_cam_errors = QLabel(self.frame_77)
        self.sett_cam_errors.setObjectName(u"sett_cam_errors")
        self.sett_cam_errors.setMinimumSize(QSize(0, 30))
        self.sett_cam_errors.setMaximumSize(QSize(16777215, 30))
        self.sett_cam_errors.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_cam_errors.setFrameShape(QFrame.Panel)
        self.sett_cam_errors.setFrameShadow(QFrame.Sunken)
        self.sett_cam_errors.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.sett_cam_errors)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_5)


        self.verticalLayout_44.addWidget(self.frame_77)


        self.horizontalLayout_24.addWidget(self.groupBox_8)

        self.stackedWidget.addWidget(self.camera_settings)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.horizontalLayout_9 = QHBoxLayout(self.history)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.frame_13 = QFrame(self.history)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(300, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_refresh_history = QPushButton(self.frame_13)
        self.btn_refresh_history.setObjectName(u"btn_refresh_history")
        icon17 = QIcon()
        icon17.addFile(u"images_icon/refresh(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_history.setIcon(icon17)

        self.verticalLayout_16.addWidget(self.btn_refresh_history, 0, Qt.AlignRight)

        self.scrollArea_2 = QScrollArea(self.frame_13)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 278, 411))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_16.addWidget(self.scrollArea_2)


        self.horizontalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.history)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lineEdit_load_path = QLineEdit(self.frame_16)
        self.lineEdit_load_path.setObjectName(u"lineEdit_load_path")

        self.horizontalLayout_12.addWidget(self.lineEdit_load_path)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.scrollArea_3 = QScrollArea(self.frame_14)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 498, 366))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_17.addWidget(self.scrollArea_3)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.label_8)


        self.verticalLayout_17.addWidget(self.frame_15)


        self.horizontalLayout_9.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.history)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main_frame)

        self.status_frame = QFrame(self.middle)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setMinimumSize(QSize(0, 60))
        self.status_frame.setMaximumSize(QSize(16777215, 60))
        self.status_frame.setStyleSheet(u"QFrame{\n"
"	background:#0C508B;\n"
"}")
        self.status_frame.setFrameShape(QFrame.NoFrame)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.message = QFrame(self.status_frame)
        self.message.setObjectName(u"message")
        self.message.setMinimumSize(QSize(0, 0))
        self.message.setMaximumSize(QSize(16777215, 16777215))
        self.message.setFrameShape(QFrame.StyledPanel)
        self.message.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.message)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.message)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.msg_label = QLabel(self.message)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setMinimumSize(QSize(700, 40))
        self.msg_label.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setPointSize(11)
        self.msg_label.setFont(font6)
        self.msg_label.setFrameShape(QFrame.WinPanel)
        self.msg_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.msg_label)


        self.horizontalLayout_5.addWidget(self.message)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.status_frame)


        self.verticalLayout.addWidget(self.middle)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.width_spinbox.valueChanged.connect(self.label_width_p_value.setText)
        self.width_spinbox.textChanged.connect(self.label_width_p_value.setText)
        self.horizontalSlider.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider_3.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.horizontalSlider_3.setValue)
        self.horizontalSlider_4.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged.connect(self.horizontalSlider_4.setValue)
        self.horizontalSlider_5.valueChanged.connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged.connect(self.horizontalSlider_5.setValue)
        self.horizontalSlider_2.valueChanged.connect(self.spinBox_laserDTH_2.setValue)
        self.spinBox_laserDTH_2.valueChanged.connect(self.horizontalSlider_2.setValue)
        self.horizontalSlider_6.valueChanged.connect(self.median_1_spin.setValue)
        self.median_1_spin.valueChanged.connect(self.horizontalSlider_6.setValue)
        self.horizontalSlider_7.valueChanged.connect(self.median_2_spin.setValue)
        self.median_2_spin.valueChanged.connect(self.horizontalSlider_7.setValue)
        self.horizontalSlider_8.valueChanged.connect(self.threshold_2_spin.setValue)
        self.threshold_2_spin.valueChanged.connect(self.horizontalSlider_8.setValue)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Main Menu</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Online Conveyor Monitoring System", None))
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_dashboard.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Dashboard</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.BTN_camera_setting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Camera Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_setting.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
#if QT_CONFIG(tooltip)
        self.BTN_general_setting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">General Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_general_setting.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
#if QT_CONFIG(tooltip)
        self.BTN_history.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Algorithm Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Laser detector", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.camera_live_btn.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_scane_start.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_scane_start.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_scan_stop.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_scan_stop.setText("")
        self.LBL_live_camera.setText("")
        self.defects_prev_btn.setText("")
        self.defects_list_slider_frame.setText("")
        self.defects_next_btn.setText("")
        self.gain_label_2.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.expo_label.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.gain_label.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.offsetx_label.setText(QCoreApplication.translate("MainWindow", u"Offset X", None))
        self.offsety_label.setText(QCoreApplication.translate("MainWindow", u"Offset Y", None))
        self.trigger_label.setText(QCoreApplication.translate("MainWindow", u"Trigger Mode", None))
        self.maxbuffer_label.setText(QCoreApplication.translate("MainWindow", u"Max Buffer", None))
        self.packetdelay_label.setText(QCoreApplication.translate("MainWindow", u"Packet Delay", None))
        self.packetsize_label.setText(QCoreApplication.translate("MainWindow", u"Packet Size", None))
        self.transmissiondelay_label.setText(QCoreApplication.translate("MainWindow", u"Transmision Delay", None))
#if QT_CONFIG(tooltip)
        self.serial_number_combo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Serial Number</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.setting_refresh_available_cams_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Refresh Available Cameras</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.setting_refresh_available_cams_btn.setText("")
#if QT_CONFIG(tooltip)
        self.expo_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Exposure</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gain_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Gain</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.width_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Width</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.height_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Height</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.offsetx_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Offset X</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.offsety_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Offset Y</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.trigger_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Off", None))
        self.trigger_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"On: Software", None))
        self.trigger_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"On: Hardware", None))

#if QT_CONFIG(tooltip)
        self.trigger_combo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Trigger Mode</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.maxbuffer_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Max Buffer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.packetdelay_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Packet Delay</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.packetsize_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Packet Size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.transmissiondelay_spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Transmision Delay</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.BTN_camera_setting_apply.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Apply/Save Parameters</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_setting_apply.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Camera Parameters", None))
        self.checkBox_th_1.setText("")
        self.checkBox_th_2.setText("")
        self.checkBox_median_1.setText("")
        self.checkBox_median_2.setText("")
        self.LBL_laserDTH_2.setText(QCoreApplication.translate("MainWindow", u"laser detector threshold", None))
        self.L_2.setText(QCoreApplication.translate("MainWindow", u"threshold_2", None))
        self.LBL_norm_2.setText(QCoreApplication.translate("MainWindow", u"median_1", None))
        self.LBL_th1_2.setText(QCoreApplication.translate("MainWindow", u"median_2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Frame Rate :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Line Speed :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pixel value :", None))
        self.label_width_p_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_pixel_value.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Px/cm", None))
#if QT_CONFIG(tooltip)
        self.brn_set_calib_parms.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Apply/Save Parameters</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.brn_set_calib_parms.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Calibration Parameters", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Camera Live", None))
#if QT_CONFIG(tooltip)
        self.camera_calib_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.camera_calib_btn.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_camera_connect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_connect.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_camera_disconnect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_disconnect.setText("")
        self.LBL_live_camera_for_setting_image_quality.setText("")
        self.LBL_area_laser_detected_2.setText("")
        self.LBL_line_laser_detected_2.setText("")
        self.gain_label_4.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0C)", None))
        self.sett_cam_temp.setText("")
        self.gain_label_3.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.sett_cam_fps.setText("")
        self.gain_label_5.setText(QCoreApplication.translate("MainWindow", u"Image Size", None))
        self.sett_cam_size.setText("")
        self.gain_label_6.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.sett_cam_errors.setText("")
        self.btn_refresh_history.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Loaded Path : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.msg_label.setText("")
    # retranslateUi

