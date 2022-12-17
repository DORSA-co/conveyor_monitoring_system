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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1315, 577)
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
"QPushButton:hover {\n"
" background: #a3a3a3;\n"
" }")
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
        icon.addFile(u"icons/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.menu_btn)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
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
        self.horizontalLayout_13.setSpacing(5)
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
        icon1.addFile(u"../../trainApp_oxin/UI/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"../../trainApp_oxin/UI/images/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.close_btn.setIcon(icon)
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
        self.menubar_frame.setMinimumSize(QSize(0, 0))
        self.menubar_frame.setMaximumSize(QSize(16777215, 60))
        self.menubar_frame.setStyleSheet(u"QFrame{\n"
"	background: #CBCBCB;\n"
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
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_dashboard.setIcon(icon3)
        self.BTN_dashboard.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_dashboard)

        self.BTN_camera_setting = QPushButton(self.menubar_frame)
        self.BTN_camera_setting.setObjectName(u"BTN_camera_setting")
        self.BTN_camera_setting.setMinimumSize(QSize(0, 0))
        self.BTN_camera_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_setting.setFont(font1)
        self.BTN_camera_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_setting.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/camera_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_setting.setIcon(icon4)
        self.BTN_camera_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_camera_setting)

        self.BTN_calibration_setting = QPushButton(self.menubar_frame)
        self.BTN_calibration_setting.setObjectName(u"BTN_calibration_setting")
        self.BTN_calibration_setting.setMinimumSize(QSize(0, 0))
        self.BTN_calibration_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_calibration_setting.setFont(font1)
        self.BTN_calibration_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_calibration_setting.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/calibration_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_calibration_setting.setIcon(icon5)
        self.BTN_calibration_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_calibration_setting)

        self.BTN_general_setting = QPushButton(self.menubar_frame)
        self.BTN_general_setting.setObjectName(u"BTN_general_setting")
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
        self.general_setting = QWidget()
        self.general_setting.setObjectName(u"general_setting")
        self.verticalLayout_35 = QVBoxLayout(self.general_setting)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.frame_3 = QFrame(self.general_setting)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 250))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(500, 0))
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_4)
        self.verticalLayout_45.setSpacing(10)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.frame_4)


        self.verticalLayout_35.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.general_setting)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.horizontalLayout_7 = QHBoxLayout(self.Dashboard)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.Dashboard)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.close_btn_2 = QPushButton(self.frame_7)
        self.close_btn_2.setObjectName(u"close_btn_2")
        self.close_btn_2.setMinimumSize(QSize(0, 0))
        self.close_btn_2.setMaximumSize(QSize(16777215, 16777215))
        self.close_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn_2.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #F70000;\n"
" }")
        icon8 = QIcon()
        icon8.addFile(u"../../trainApp_oxin/UI/images/icons/person2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn_2.setIcon(icon8)
        self.close_btn_2.setIconSize(QSize(15, 15))

        self.verticalLayout_7.addWidget(self.close_btn_2)

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
        self.BTN_scane_start.setIcon(icon)
        self.BTN_scane_start.setIconSize(QSize(30, 35))

        self.verticalLayout_7.addWidget(self.BTN_scane_start)

        self.BTN_scane_stop = QPushButton(self.frame_7)
        self.BTN_scane_stop.setObjectName(u"BTN_scane_stop")
        self.BTN_scane_stop.setEnabled(True)
        self.BTN_scane_stop.setMinimumSize(QSize(0, 0))
        self.BTN_scane_stop.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_scane_stop.setFont(font2)
        self.BTN_scane_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_scane_stop.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"icons/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_scane_stop.setIcon(icon9)
        self.BTN_scane_stop.setIconSize(QSize(30, 35))

        self.verticalLayout_7.addWidget(self.BTN_scane_stop)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.Dashboard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.LBL_live_camera = QLabel(self.frame_6)
        self.LBL_live_camera.setObjectName(u"LBL_live_camera")
        self.LBL_live_camera.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.LBL_live_camera)


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
        self.frame_12.setMaximumSize(QSize(310, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.setting_camera_params_gb = QGroupBox(self.frame_12)
        self.setting_camera_params_gb.setObjectName(u"setting_camera_params_gb")
        self.setting_camera_params_gb.setEnabled(True)
        self.setting_camera_params_gb.setMaximumSize(QSize(16777215, 16777215))
        self.setting_camera_params_gb.setFont(font1)
        self.setting_camera_params_gb.setStyleSheet(u"QPushButton{\n"
"	background: #2C313A;\n"
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
"	background: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.setting_camera_params_gb)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.sett_cam_scrollArea = QScrollArea(self.setting_camera_params_gb)
        self.sett_cam_scrollArea.setObjectName(u"sett_cam_scrollArea")
        self.sett_cam_scrollArea.setEnabled(True)
        self.sett_cam_scrollArea.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.sett_cam_scrollArea.setFrameShape(QFrame.Box)
        self.sett_cam_scrollArea.setFrameShadow(QFrame.Raised)
        self.sett_cam_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 240, 437))
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
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_refresh_available_cams_btn.setIcon(icon10)

        self.horizontalLayout_22.addWidget(self.setting_refresh_available_cams_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.expo_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.expo_spinbox.setObjectName(u"expo_spinbox")
        self.expo_spinbox.setEnabled(True)
        self.expo_spinbox.setMinimumSize(QSize(0, 30))
        self.expo_spinbox.setMaximumSize(QSize(16777215, 30))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.width_spinbox.setPalette(palette2)
        self.width_spinbox.setFont(font4)
        self.width_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.width_spinbox.setAlignment(Qt.AlignCenter)
        self.width_spinbox.setMinimum(0)
        self.width_spinbox.setMaximum(1920)
        self.width_spinbox.setSingleStep(1)
        self.width_spinbox.setValue(1920)

        self.verticalLayout_12.addWidget(self.width_spinbox)

        self.height_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.height_spinbox.setObjectName(u"height_spinbox")
        self.height_spinbox.setEnabled(True)
        self.height_spinbox.setMinimumSize(QSize(0, 30))
        self.height_spinbox.setMaximumSize(QSize(16777215, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.offsetx_spinbox.setPalette(palette4)
        self.offsetx_spinbox.setFont(font4)
        self.offsetx_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.offsetx_spinbox.setAlignment(Qt.AlignCenter)
        self.offsetx_spinbox.setMaximum(1920)
        self.offsetx_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.offsetx_spinbox)

        self.offsety_spinbox = QSpinBox(self.scrollAreaWidgetContents)
        self.offsety_spinbox.setObjectName(u"offsety_spinbox")
        self.offsety_spinbox.setEnabled(True)
        self.offsety_spinbox.setMinimumSize(QSize(0, 30))
        self.offsety_spinbox.setMaximumSize(QSize(16777215, 30))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette6.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette7.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette8.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette8.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
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
        palette9.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette9.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.transmissiondelay_spinbox.setPalette(palette9)
        self.transmissiondelay_spinbox.setFont(font4)
        self.transmissiondelay_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.transmissiondelay_spinbox.setAlignment(Qt.AlignCenter)
        self.transmissiondelay_spinbox.setMaximum(10000)
        self.transmissiondelay_spinbox.setSingleStep(1)

        self.verticalLayout_12.addWidget(self.transmissiondelay_spinbox)


        self.horizontalLayout_20.addLayout(self.verticalLayout_12)

        self.sett_cam_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.sett_cam_scrollArea)

        self.BTN_camera_setting_apply = QPushButton(self.setting_camera_params_gb)
        self.BTN_camera_setting_apply.setObjectName(u"BTN_camera_setting_apply")
        self.BTN_camera_setting_apply.setMinimumSize(QSize(0, 35))
        self.BTN_camera_setting_apply.setFont(font2)
        self.BTN_camera_setting_apply.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_setting_apply.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/apply_params.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_setting_apply.setIcon(icon11)
        self.BTN_camera_setting_apply.setIconSize(QSize(16, 16))

        self.verticalLayout_10.addWidget(self.BTN_camera_setting_apply)


        self.verticalLayout_13.addWidget(self.setting_camera_params_gb)


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
        self.BTN_camera_connect = QPushButton(self.sett_cam_control_frame)
        self.BTN_camera_connect.setObjectName(u"BTN_camera_connect")
        self.BTN_camera_connect.setEnabled(True)
        self.BTN_camera_connect.setMinimumSize(QSize(0, 0))
        self.BTN_camera_connect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_connect.setFont(font2)
        self.BTN_camera_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_connect.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u"images_icon/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_connect.setIcon(icon12)
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
        self.BTN_camera_disconnect.setEnabled(True)
        self.BTN_camera_disconnect.setMinimumSize(QSize(0, 0))
        self.BTN_camera_disconnect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_camera_disconnect.setFont(font2)
        self.BTN_camera_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_camera_disconnect.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u"images_icon/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_disconnect.setIcon(icon13)
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
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LBL_live_camera_for_setting_image_quality = QLabel(self.sett_shot_frame)
        self.LBL_live_camera_for_setting_image_quality.setObjectName(u"LBL_live_camera_for_setting_image_quality")
        self.LBL_live_camera_for_setting_image_quality.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.LBL_live_camera_for_setting_image_quality)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


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
        self.stackedWidget.addWidget(self.history)
        self.calibration_settings = QWidget()
        self.calibration_settings.setObjectName(u"calibration_settings")
        self.horizontalLayout_15 = QHBoxLayout(self.calibration_settings)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.groupBox_7 = QGroupBox(self.calibration_settings)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 0))
        self.groupBox_7.setMaximumSize(QSize(310, 16777215))
        self.groupBox_7.setFont(font1)
        self.groupBox_7.setStyleSheet(u"QPushButton{\n"
"	background: #2C313A;\n"
"	color: white;\n"
"	padding: 5px;\n"
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
"	background: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_3 = QScrollArea(self.groupBox_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.Panel)
        self.scrollArea_3.setFrameShadow(QFrame.Raised)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 234, 158))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.LBL_laserDTH = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_laserDTH.setObjectName(u"LBL_laserDTH")
        self.LBL_laserDTH.setMinimumSize(QSize(0, 30))
        self.LBL_laserDTH.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(10)
        self.LBL_laserDTH.setFont(font5)

        self.verticalLayout_17.addWidget(self.LBL_laserDTH)

        self.LBL_norm = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_norm.setObjectName(u"LBL_norm")
        self.LBL_norm.setMinimumSize(QSize(0, 30))
        self.LBL_norm.setMaximumSize(QSize(16777215, 30))
        self.LBL_norm.setFont(font5)

        self.verticalLayout_17.addWidget(self.LBL_norm)

        self.LBL_th1 = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_th1.setObjectName(u"LBL_th1")
        self.LBL_th1.setMinimumSize(QSize(0, 30))
        self.LBL_th1.setMaximumSize(QSize(16777215, 30))
        self.LBL_th1.setFont(font5)

        self.verticalLayout_17.addWidget(self.LBL_th1)

        self.L = QLabel(self.scrollAreaWidgetContents_4)
        self.L.setObjectName(u"L")
        self.L.setMinimumSize(QSize(0, 30))
        self.L.setMaximumSize(QSize(16777215, 30))
        self.L.setFont(font5)

        self.verticalLayout_17.addWidget(self.L)


        self.horizontalLayout_12.addLayout(self.verticalLayout_17)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.spinBox_laserDTH = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_laserDTH.setObjectName(u"spinBox_laserDTH")
        self.spinBox_laserDTH.setMinimumSize(QSize(0, 30))
        self.spinBox_laserDTH.setMaximumSize(QSize(16777215, 30))
        self.spinBox_laserDTH.setFont(font5)
        self.spinBox_laserDTH.setMinimum(5.000000000000000)
        self.spinBox_laserDTH.setMaximum(500.000000000000000)
        self.spinBox_laserDTH.setSingleStep(0.010000000000000)
        self.spinBox_laserDTH.setValue(40.000000000000000)

        self.verticalLayout_20.addWidget(self.spinBox_laserDTH)

        self.spinBox_norm = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_norm.setObjectName(u"spinBox_norm")
        self.spinBox_norm.setMinimumSize(QSize(0, 30))
        self.spinBox_norm.setMaximumSize(QSize(16777215, 30))
        self.spinBox_norm.setFont(font5)
        self.spinBox_norm.setMinimum(5.000000000000000)
        self.spinBox_norm.setMaximum(500.000000000000000)
        self.spinBox_norm.setSingleStep(0.010000000000000)
        self.spinBox_norm.setValue(40.000000000000000)

        self.verticalLayout_20.addWidget(self.spinBox_norm)

        self.calib_sett_rect_dist_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.calib_sett_rect_dist_spin.setObjectName(u"calib_sett_rect_dist_spin")
        self.calib_sett_rect_dist_spin.setMinimumSize(QSize(0, 30))
        self.calib_sett_rect_dist_spin.setMaximumSize(QSize(16777215, 30))
        self.calib_sett_rect_dist_spin.setFont(font5)
        self.calib_sett_rect_dist_spin.setMinimum(5.000000000000000)
        self.calib_sett_rect_dist_spin.setMaximum(500.000000000000000)
        self.calib_sett_rect_dist_spin.setSingleStep(0.010000000000000)
        self.calib_sett_rect_dist_spin.setValue(50.000000000000000)

        self.verticalLayout_20.addWidget(self.calib_sett_rect_dist_spin)

        self.calib_sett_baseline_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.calib_sett_baseline_spin.setObjectName(u"calib_sett_baseline_spin")
        self.calib_sett_baseline_spin.setMinimumSize(QSize(0, 30))
        self.calib_sett_baseline_spin.setMaximumSize(QSize(16777215, 30))
        self.calib_sett_baseline_spin.setFont(font5)
        self.calib_sett_baseline_spin.setMinimum(5.000000000000000)
        self.calib_sett_baseline_spin.setMaximum(1500.000000000000000)
        self.calib_sett_baseline_spin.setSingleStep(0.010000000000000)
        self.calib_sett_baseline_spin.setValue(630.000000000000000)

        self.verticalLayout_20.addWidget(self.calib_sett_baseline_spin)


        self.horizontalLayout_12.addLayout(self.verticalLayout_20)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_16.addWidget(self.scrollArea_3)

        self.BTN_algo_param_setting = QPushButton(self.groupBox_7)
        self.BTN_algo_param_setting.setObjectName(u"BTN_algo_param_setting")
        self.BTN_algo_param_setting.setMinimumSize(QSize(0, 35))
        self.BTN_algo_param_setting.setMaximumSize(QSize(16777215, 35))
        self.BTN_algo_param_setting.setFont(font2)
        self.BTN_algo_param_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_algo_param_setting.setStyleSheet(u"")
        self.BTN_algo_param_setting.setIcon(icon11)
        self.BTN_algo_param_setting.setIconSize(QSize(16, 16))

        self.verticalLayout_16.addWidget(self.BTN_algo_param_setting)


        self.horizontalLayout_15.addWidget(self.groupBox_7)

        self.groupBox_14 = QGroupBox(self.calibration_settings)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setFont(font1)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.sett_cam_control_frame_3 = QFrame(self.groupBox_14)
        self.sett_cam_control_frame_3.setObjectName(u"sett_cam_control_frame_3")
        self.sett_cam_control_frame_3.setEnabled(True)
        self.sett_cam_control_frame_3.setMinimumSize(QSize(0, 40))
        self.sett_cam_control_frame_3.setMaximumSize(QSize(16777215, 40))
        self.sett_cam_control_frame_3.setStyleSheet(u"QPushButton{\n"
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
        self.sett_cam_control_frame_3.setFrameShape(QFrame.Box)
        self.sett_cam_control_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.sett_cam_control_frame_3)
        self.horizontalLayout_54.setSpacing(10)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(10, 0, 10, 0)
        self.BTN_laser_detector_connect = QPushButton(self.sett_cam_control_frame_3)
        self.BTN_laser_detector_connect.setObjectName(u"BTN_laser_detector_connect")
        self.BTN_laser_detector_connect.setEnabled(True)
        self.BTN_laser_detector_connect.setMinimumSize(QSize(0, 0))
        self.BTN_laser_detector_connect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_laser_detector_connect.setFont(font2)
        self.BTN_laser_detector_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_laser_detector_connect.setStyleSheet(u"")
        self.BTN_laser_detector_connect.setIcon(icon12)
        self.BTN_laser_detector_connect.setIconSize(QSize(35, 35))

        self.horizontalLayout_54.addWidget(self.BTN_laser_detector_connect)

        self.line_17 = QFrame(self.sett_cam_control_frame_3)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setMaximumSize(QSize(16777215, 25))
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_54.addWidget(self.line_17)

        self.BTN_laser_detector_disconnect = QPushButton(self.sett_cam_control_frame_3)
        self.BTN_laser_detector_disconnect.setObjectName(u"BTN_laser_detector_disconnect")
        self.BTN_laser_detector_disconnect.setEnabled(True)
        self.BTN_laser_detector_disconnect.setMinimumSize(QSize(0, 0))
        self.BTN_laser_detector_disconnect.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_laser_detector_disconnect.setFont(font2)
        self.BTN_laser_detector_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_laser_detector_disconnect.setStyleSheet(u"")
        self.BTN_laser_detector_disconnect.setIcon(icon13)
        self.BTN_laser_detector_disconnect.setIconSize(QSize(35, 35))

        self.horizontalLayout_54.addWidget(self.BTN_laser_detector_disconnect)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_11)


        self.verticalLayout_21.addWidget(self.sett_cam_control_frame_3)

        self.calib_sett_result_frame = QFrame(self.groupBox_14)
        self.calib_sett_result_frame.setObjectName(u"calib_sett_result_frame")
        self.calib_sett_result_frame.setFrameShape(QFrame.WinPanel)
        self.calib_sett_result_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_24 = QVBoxLayout(self.calib_sett_result_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.LBL_area_laser_detected = QLabel(self.calib_sett_result_frame)
        self.LBL_area_laser_detected.setObjectName(u"LBL_area_laser_detected")
        self.LBL_area_laser_detected.setScaledContents(True)

        self.verticalLayout_25.addWidget(self.LBL_area_laser_detected)


        self.verticalLayout_24.addLayout(self.verticalLayout_25)


        self.verticalLayout_21.addWidget(self.calib_sett_result_frame)

        self.calib_sett_result_frame_2 = QFrame(self.groupBox_14)
        self.calib_sett_result_frame_2.setObjectName(u"calib_sett_result_frame_2")
        self.calib_sett_result_frame_2.setFrameShape(QFrame.WinPanel)
        self.calib_sett_result_frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_28 = QVBoxLayout(self.calib_sett_result_frame_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.LBL_line_laser_detected = QLabel(self.calib_sett_result_frame_2)
        self.LBL_line_laser_detected.setObjectName(u"LBL_line_laser_detected")
        self.LBL_line_laser_detected.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.LBL_line_laser_detected)


        self.verticalLayout_28.addLayout(self.verticalLayout_29)


        self.verticalLayout_21.addWidget(self.calib_sett_result_frame_2)


        self.horizontalLayout_15.addWidget(self.groupBox_14)

        self.stackedWidget.addWidget(self.calibration_settings)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.main_frame)

        self.status_frame = QFrame(self.middle)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setMinimumSize(QSize(0, 60))
        self.status_frame.setMaximumSize(QSize(16777215, 60))
        self.status_frame.setStyleSheet(u" background: #CBCBCB;")
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

        self.stackedWidget.setCurrentIndex(1)


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
        self.BTN_calibration_setting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Calibration Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_calibration_setting.setText(QCoreApplication.translate("MainWindow", u"Calibration Settings", None))
#if QT_CONFIG(tooltip)
        self.BTN_general_setting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">General Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_general_setting.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
#if QT_CONFIG(tooltip)
        self.BTN_history.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Algorithm Settings</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
#if QT_CONFIG(tooltip)
        self.close_btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn_2.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_scane_start.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_scane_start.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_scane_stop.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_scane_stop.setText("")
        self.LBL_live_camera.setText("")
        self.setting_camera_params_gb.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
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
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Camera Live", None))
#if QT_CONFIG(tooltip)
        self.BTN_camera_connect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_connect.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_camera_disconnect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_camera_disconnect.setText("")
        self.LBL_live_camera_for_setting_image_quality.setText("")
        self.gain_label_4.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0C)", None))
        self.sett_cam_temp.setText("")
        self.gain_label_3.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.sett_cam_fps.setText("")
        self.gain_label_5.setText(QCoreApplication.translate("MainWindow", u"Image Size", None))
        self.sett_cam_size.setText("")
        self.gain_label_6.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.sett_cam_errors.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Parameters", None))
        self.LBL_laserDTH.setText(QCoreApplication.translate("MainWindow", u"laser detector threshold", None))
        self.LBL_norm.setText(QCoreApplication.translate("MainWindow", u"mean level value(norm)", None))
        self.LBL_th1.setText(QCoreApplication.translate("MainWindow", u"threshold_1", None))
        self.L.setText(QCoreApplication.translate("MainWindow", u"threshold_2", None))
#if QT_CONFIG(tooltip)
        self.BTN_algo_param_setting.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Apply/Save Parameters</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_algo_param_setting.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Live Results", None))
#if QT_CONFIG(tooltip)
        self.BTN_laser_detector_connect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_laser_detector_connect.setText("")
#if QT_CONFIG(tooltip)
        self.BTN_laser_detector_disconnect.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BTN_laser_detector_disconnect.setText("")
        self.LBL_area_laser_detected.setText("")
        self.LBL_line_laser_detected.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.msg_label.setText("")
    # retranslateUi

