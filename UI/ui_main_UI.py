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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1470, 608)
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
        icon.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(0, 0))
        self.minimize_btn.setMaximumSize(QSize(16777215, 16777215))
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
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

        self.BTN_calibration_setting = QPushButton(self.menubar_frame)
        self.BTN_calibration_setting.setObjectName(u"BTN_calibration_setting")
        self.BTN_calibration_setting.setMinimumSize(QSize(0, 0))
        self.BTN_calibration_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_calibration_setting.setFont(font1)
        self.BTN_calibration_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_calibration_setting.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/calibration_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_calibration_setting.setIcon(icon6)
        self.BTN_calibration_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_calibration_setting)

        self.BTN_general_setting = QPushButton(self.menubar_frame)
        self.BTN_general_setting.setObjectName(u"BTN_general_setting")
        self.BTN_general_setting.setMinimumSize(QSize(0, 0))
        self.BTN_general_setting.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_general_setting.setFont(font1)
        self.BTN_general_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_general_setting.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/general_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_general_setting.setIcon(icon7)
        self.BTN_general_setting.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_general_setting)

        self.BTN_history = QPushButton(self.menubar_frame)
        self.BTN_history.setObjectName(u"BTN_history")
        self.BTN_history.setMinimumSize(QSize(0, 0))
        self.BTN_history.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_history.setFont(font1)
        self.BTN_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_history.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/algorithm_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_history.setIcon(icon8)
        self.BTN_history.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.BTN_history)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.menubar_frame)

        self.main_frame = QFrame(self.middle)
        self.main_frame.setObjectName(u"main_frame")
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
        self.groupBox_9 = QGroupBox(self.frame_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font1)
        self.groupBox_9.setStyleSheet(u"QPushButton{\n"
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
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.dash_cam_connect_btn = QPushButton(self.groupBox_9)
        self.dash_cam_connect_btn.setObjectName(u"dash_cam_connect_btn")
        self.dash_cam_connect_btn.setEnabled(True)
        self.dash_cam_connect_btn.setMinimumSize(QSize(0, 35))
        self.dash_cam_connect_btn.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.dash_cam_connect_btn.setFont(font2)
        self.dash_cam_connect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_cam_connect_btn.setStyleSheet(u"QPushButton{\n"
"	border-right: 10px solid #F70000;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/camera_connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dash_cam_connect_btn.setIcon(icon9)
        self.dash_cam_connect_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.dash_cam_connect_btn)

        self.camera_setting_connect_btn_6 = QPushButton(self.groupBox_9)
        self.camera_setting_connect_btn_6.setObjectName(u"camera_setting_connect_btn_6")
        self.camera_setting_connect_btn_6.setEnabled(True)
        self.camera_setting_connect_btn_6.setMinimumSize(QSize(0, 35))
        self.camera_setting_connect_btn_6.setMaximumSize(QSize(16777215, 35))
        self.camera_setting_connect_btn_6.setFont(font2)
        self.camera_setting_connect_btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_setting_connect_btn_6.setStyleSheet(u"QPushButton{\n"
"	border-right: 10px solid #F70000;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/io_connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.camera_setting_connect_btn_6.setIcon(icon10)
        self.camera_setting_connect_btn_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.camera_setting_connect_btn_6)

        self.dash_run_btn = QPushButton(self.groupBox_9)
        self.dash_run_btn.setObjectName(u"dash_run_btn")
        self.dash_run_btn.setEnabled(False)
        self.dash_run_btn.setMinimumSize(QSize(0, 35))
        self.dash_run_btn.setMaximumSize(QSize(16777215, 35))
        self.dash_run_btn.setFont(font2)
        self.dash_run_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_run_btn.setStyleSheet(u"QPushButton{\n"
"	border-right: 10px solid #F70000;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/run_system.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dash_run_btn.setIcon(icon11)
        self.dash_run_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.dash_run_btn)


        self.verticalLayout_45.addWidget(self.groupBox_9)

        self.groupBox_11 = QGroupBox(self.frame_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font1)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_32 = QLabel(self.groupBox_11)
        self.label_32.setObjectName(u"label_32")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_32.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_32)

        self.label_33 = QLabel(self.groupBox_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_33)

        self.label_34 = QLabel(self.groupBox_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_34)


        self.horizontalLayout_14.addLayout(self.verticalLayout_4)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.dash_cams_indicator = QProgressBar(self.groupBox_11)
        self.dash_cams_indicator.setObjectName(u"dash_cams_indicator")
        self.dash_cams_indicator.setMinimumSize(QSize(30, 30))
        self.dash_cams_indicator.setMaximumSize(QSize(30, 30))
        self.dash_cams_indicator.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #F70000;\n"
"}\n"
"")
        self.dash_cams_indicator.setMaximum(100)
        self.dash_cams_indicator.setValue(100)
        self.dash_cams_indicator.setTextVisible(False)

        self.verticalLayout_43.addWidget(self.dash_cams_indicator)

        self.progressBar_5 = QProgressBar(self.groupBox_11)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setMinimumSize(QSize(30, 30))
        self.progressBar_5.setMaximumSize(QSize(30, 30))
        self.progressBar_5.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #F70000;\n"
"}\n"
"")
        self.progressBar_5.setMaximum(100)
        self.progressBar_5.setValue(100)
        self.progressBar_5.setTextVisible(False)

        self.verticalLayout_43.addWidget(self.progressBar_5)

        self.dash_operating_indicator = QProgressBar(self.groupBox_11)
        self.dash_operating_indicator.setObjectName(u"dash_operating_indicator")
        self.dash_operating_indicator.setMinimumSize(QSize(30, 30))
        self.dash_operating_indicator.setMaximumSize(QSize(30, 30))
        self.dash_operating_indicator.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #F70000;\n"
"}\n"
"")
        self.dash_operating_indicator.setMaximum(100)
        self.dash_operating_indicator.setValue(100)
        self.dash_operating_indicator.setTextVisible(False)

        self.verticalLayout_43.addWidget(self.dash_operating_indicator)


        self.horizontalLayout_14.addLayout(self.verticalLayout_43)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_35 = QLabel(self.groupBox_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_35)

        self.label_37 = QLabel(self.groupBox_11)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_37)

        self.label_36 = QLabel(self.groupBox_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_36)


        self.horizontalLayout_14.addLayout(self.verticalLayout_46)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.dash_detection_indicator = QProgressBar(self.groupBox_11)
        self.dash_detection_indicator.setObjectName(u"dash_detection_indicator")
        self.dash_detection_indicator.setMinimumSize(QSize(30, 30))
        self.dash_detection_indicator.setMaximumSize(QSize(30, 30))
        self.dash_detection_indicator.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #8D8D8D;\n"
"}\n"
"")
        self.dash_detection_indicator.setMaximum(100)
        self.dash_detection_indicator.setValue(100)
        self.dash_detection_indicator.setTextVisible(False)

        self.verticalLayout_47.addWidget(self.dash_detection_indicator)

        self.dash_lowwidth_indicator = QProgressBar(self.groupBox_11)
        self.dash_lowwidth_indicator.setObjectName(u"dash_lowwidth_indicator")
        self.dash_lowwidth_indicator.setMinimumSize(QSize(30, 30))
        self.dash_lowwidth_indicator.setMaximumSize(QSize(30, 30))
        self.dash_lowwidth_indicator.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #8D8D8D;\n"
"}\n"
"")
        self.dash_lowwidth_indicator.setMaximum(100)
        self.dash_lowwidth_indicator.setValue(100)
        self.dash_lowwidth_indicator.setTextVisible(False)

        self.verticalLayout_47.addWidget(self.dash_lowwidth_indicator)

        self.dash_highwidth_indicator = QProgressBar(self.groupBox_11)
        self.dash_highwidth_indicator.setObjectName(u"dash_highwidth_indicator")
        self.dash_highwidth_indicator.setMinimumSize(QSize(30, 30))
        self.dash_highwidth_indicator.setMaximumSize(QSize(30, 30))
        self.dash_highwidth_indicator.setStyleSheet(u"QProgressBar::chunk {\n"
"    background: #8D8D8D;\n"
"}\n"
"")
        self.dash_highwidth_indicator.setMaximum(100)
        self.dash_highwidth_indicator.setValue(100)
        self.dash_highwidth_indicator.setTextVisible(False)

        self.verticalLayout_47.addWidget(self.dash_highwidth_indicator)


        self.horizontalLayout_14.addLayout(self.verticalLayout_47)


        self.verticalLayout_45.addWidget(self.groupBox_11)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.groupBox.setMaximumSize(QSize(350, 16777215))
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.dash_coilid_lineedit = QLineEdit(self.groupBox)
        self.dash_coilid_lineedit.setObjectName(u"dash_coilid_lineedit")
        self.dash_coilid_lineedit.setMinimumSize(QSize(0, 30))
        self.dash_coilid_lineedit.setMaximumSize(QSize(16777215, 30))
        self.dash_coilid_lineedit.setFont(font3)
        self.dash_coilid_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.dash_coilid_lineedit)

        self.dash_coillength_lineedit = QLineEdit(self.groupBox)
        self.dash_coillength_lineedit.setObjectName(u"dash_coillength_lineedit")
        self.dash_coillength_lineedit.setMinimumSize(QSize(0, 30))
        self.dash_coillength_lineedit.setMaximumSize(QSize(16777215, 30))
        self.dash_coillength_lineedit.setFont(font3)
        self.dash_coillength_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.dash_coillength_lineedit)

        self.dash_coillthick_lineedit = QLineEdit(self.groupBox)
        self.dash_coillthick_lineedit.setObjectName(u"dash_coillthick_lineedit")
        self.dash_coillthick_lineedit.setMinimumSize(QSize(0, 30))
        self.dash_coillthick_lineedit.setMaximumSize(QSize(16777215, 30))
        self.dash_coillthick_lineedit.setFont(font3)
        self.dash_coillthick_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.dash_coillthick_lineedit)

        self.dash_setpoint_lineedit = QLineEdit(self.groupBox)
        self.dash_setpoint_lineedit.setObjectName(u"dash_setpoint_lineedit")
        self.dash_setpoint_lineedit.setMinimumSize(QSize(0, 30))
        self.dash_setpoint_lineedit.setMaximumSize(QSize(16777215, 30))
        self.dash_setpoint_lineedit.setFont(font3)
        self.dash_setpoint_lineedit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.dash_setpoint_lineedit)

        self.dash_thrs_spin = QDoubleSpinBox(self.groupBox)
        self.dash_thrs_spin.setObjectName(u"dash_thrs_spin")
        self.dash_thrs_spin.setMinimumSize(QSize(0, 30))
        self.dash_thrs_spin.setMaximumSize(QSize(16777215, 30))
        self.dash_thrs_spin.setFont(font3)
        self.dash_thrs_spin.setAlignment(Qt.AlignCenter)
        self.dash_thrs_spin.setMaximum(20.000000000000000)
        self.dash_thrs_spin.setSingleStep(0.010000000000000)
        self.dash_thrs_spin.setValue(1.000000000000000)

        self.verticalLayout_34.addWidget(self.dash_thrs_spin)


        self.gridLayout.addLayout(self.verticalLayout_34, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_46 = QLabel(self.groupBox)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 30))
        self.label_46.setMaximumSize(QSize(16777215, 30))
        self.label_46.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_46)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.groupBox)

        self.groupBox_15 = QGroupBox(self.frame_3)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(270, 0))
        self.groupBox_15.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_15.setFont(font1)
        self.groupBox_15.setStyleSheet(u"QPushButton{\n"
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
        self.gridLayout_2 = QGridLayout(self.groupBox_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_38 = QLabel(self.groupBox_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 0))
        self.label_38.setMaximumSize(QSize(16777215, 16777215))
        self.label_38.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_38)

        self.label_39 = QLabel(self.groupBox_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setMaximumSize(QSize(16777215, 16777215))
        self.label_39.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_39)

        self.label_40 = QLabel(self.groupBox_15)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 0))
        self.label_40.setMaximumSize(QSize(16777215, 16777215))
        self.label_40.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_40)

        self.label_41 = QLabel(self.groupBox_15)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(16777215, 16777215))
        self.label_41.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_41)


        self.gridLayout_2.addLayout(self.verticalLayout_33, 0, 0, 1, 1)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.dash_dev_width = QLabel(self.groupBox_15)
        self.dash_dev_width.setObjectName(u"dash_dev_width")
        self.dash_dev_width.setMinimumSize(QSize(0, 0))
        self.dash_dev_width.setMaximumSize(QSize(16777215, 16777215))
        self.dash_dev_width.setFont(font3)
        self.dash_dev_width.setFrameShape(QFrame.WinPanel)
        self.dash_dev_width.setFrameShadow(QFrame.Sunken)
        self.dash_dev_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.dash_dev_width)

        self.dash_avg_width = QLabel(self.groupBox_15)
        self.dash_avg_width.setObjectName(u"dash_avg_width")
        self.dash_avg_width.setMinimumSize(QSize(0, 0))
        self.dash_avg_width.setMaximumSize(QSize(16777215, 16777215))
        self.dash_avg_width.setFont(font3)
        self.dash_avg_width.setFrameShape(QFrame.WinPanel)
        self.dash_avg_width.setFrameShadow(QFrame.Sunken)
        self.dash_avg_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.dash_avg_width)

        self.dash_min_width = QLabel(self.groupBox_15)
        self.dash_min_width.setObjectName(u"dash_min_width")
        self.dash_min_width.setMinimumSize(QSize(0, 0))
        self.dash_min_width.setMaximumSize(QSize(16777215, 16777215))
        self.dash_min_width.setFont(font3)
        self.dash_min_width.setFrameShape(QFrame.WinPanel)
        self.dash_min_width.setFrameShadow(QFrame.Sunken)
        self.dash_min_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.dash_min_width)

        self.dash_max_width = QLabel(self.groupBox_15)
        self.dash_max_width.setObjectName(u"dash_max_width")
        self.dash_max_width.setMinimumSize(QSize(0, 0))
        self.dash_max_width.setMaximumSize(QSize(16777215, 16777215))
        self.dash_max_width.setFont(font3)
        self.dash_max_width.setFrameShape(QFrame.WinPanel)
        self.dash_max_width.setFrameShadow(QFrame.Sunken)
        self.dash_max_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.dash_max_width)


        self.gridLayout_2.addLayout(self.verticalLayout_50, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.groupBox_15)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.dash_show_visuals_btn = QPushButton(self.frame_2)
        self.dash_show_visuals_btn.setObjectName(u"dash_show_visuals_btn")
        self.dash_show_visuals_btn.setEnabled(True)
        self.dash_show_visuals_btn.setMinimumSize(QSize(0, 30))
        self.dash_show_visuals_btn.setMaximumSize(QSize(16777215, 30))
        self.dash_show_visuals_btn.setFont(font2)
        self.dash_show_visuals_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_show_visuals_btn.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/contours_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dash_show_visuals_btn.setIcon(icon12)
        self.dash_show_visuals_btn.setIconSize(QSize(18, 18))
        self.dash_show_visuals_btn.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.dash_show_visuals_btn)

        self.dash_show_chart_btn = QPushButton(self.frame_2)
        self.dash_show_chart_btn.setObjectName(u"dash_show_chart_btn")
        self.dash_show_chart_btn.setEnabled(True)
        self.dash_show_chart_btn.setMinimumSize(QSize(0, 30))
        self.dash_show_chart_btn.setMaximumSize(QSize(16777215, 30))
        self.dash_show_chart_btn.setFont(font2)
        self.dash_show_chart_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dash_show_chart_btn.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dash_show_chart_btn.setIcon(icon13)
        self.dash_show_chart_btn.setIconSize(QSize(18, 18))
        self.dash_show_chart_btn.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.dash_show_chart_btn)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 2)


        self.horizontalLayout_10.addWidget(self.groupBox_15)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(300, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.dash_curr_width = QLabel(self.groupBox_2)
        self.dash_curr_width.setObjectName(u"dash_curr_width")
        font4 = QFont()
        font4.setPointSize(50)
        font4.setBold(False)
        self.dash_curr_width.setFont(font4)
        self.dash_curr_width.setFrameShape(QFrame.WinPanel)
        self.dash_curr_width.setFrameShadow(QFrame.Sunken)
        self.dash_curr_width.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.dash_curr_width)


        self.horizontalLayout_10.addWidget(self.groupBox_2)


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

        self.BTN_scane_start = QPushButton(self.frame_7)
        self.BTN_scane_start.setObjectName(u"BTN_scane_start")
        self.BTN_scane_start.setEnabled(True)
        self.BTN_scane_start.setMinimumSize(QSize(0, 0))
        self.BTN_scane_start.setMaximumSize(QSize(16777215, 16777215))
        self.BTN_scane_start.setFont(font2)
        self.BTN_scane_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_scane_start.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u"images_icon/qr-code-scan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_scane_start.setIcon(icon14)
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
        icon15 = QIcon()
        icon15.addFile(u"images_icon/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_scane_stop.setIcon(icon15)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 267, 437))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gain_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.gain_label_2.setObjectName(u"gain_label_2")
        self.gain_label_2.setMinimumSize(QSize(0, 30))
        self.gain_label_2.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.gain_label_2.setFont(font5)

        self.verticalLayout_11.addWidget(self.gain_label_2)

        self.expo_label = QLabel(self.scrollAreaWidgetContents)
        self.expo_label.setObjectName(u"expo_label")
        self.expo_label.setMinimumSize(QSize(0, 30))
        self.expo_label.setMaximumSize(QSize(16777215, 30))
        self.expo_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.expo_label)

        self.gain_label = QLabel(self.scrollAreaWidgetContents)
        self.gain_label.setObjectName(u"gain_label")
        self.gain_label.setMinimumSize(QSize(0, 30))
        self.gain_label.setMaximumSize(QSize(16777215, 30))
        self.gain_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.gain_label)

        self.width_label = QLabel(self.scrollAreaWidgetContents)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setMinimumSize(QSize(0, 30))
        self.width_label.setMaximumSize(QSize(16777215, 30))
        self.width_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.width_label)

        self.height_label = QLabel(self.scrollAreaWidgetContents)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setMinimumSize(QSize(0, 30))
        self.height_label.setMaximumSize(QSize(16777215, 30))
        self.height_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.height_label)

        self.offsetx_label = QLabel(self.scrollAreaWidgetContents)
        self.offsetx_label.setObjectName(u"offsetx_label")
        self.offsetx_label.setMinimumSize(QSize(0, 30))
        self.offsetx_label.setMaximumSize(QSize(16777215, 30))
        self.offsetx_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.offsetx_label)

        self.offsety_label = QLabel(self.scrollAreaWidgetContents)
        self.offsety_label.setObjectName(u"offsety_label")
        self.offsety_label.setMinimumSize(QSize(0, 30))
        self.offsety_label.setMaximumSize(QSize(16777215, 30))
        self.offsety_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.offsety_label)

        self.trigger_label = QLabel(self.scrollAreaWidgetContents)
        self.trigger_label.setObjectName(u"trigger_label")
        self.trigger_label.setMinimumSize(QSize(0, 30))
        self.trigger_label.setMaximumSize(QSize(16777215, 30))
        self.trigger_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.trigger_label)

        self.maxbuffer_label = QLabel(self.scrollAreaWidgetContents)
        self.maxbuffer_label.setObjectName(u"maxbuffer_label")
        self.maxbuffer_label.setMinimumSize(QSize(0, 30))
        self.maxbuffer_label.setMaximumSize(QSize(16777215, 30))
        self.maxbuffer_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.maxbuffer_label)

        self.packetdelay_label = QLabel(self.scrollAreaWidgetContents)
        self.packetdelay_label.setObjectName(u"packetdelay_label")
        self.packetdelay_label.setMinimumSize(QSize(0, 30))
        self.packetdelay_label.setMaximumSize(QSize(16777215, 30))
        self.packetdelay_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.packetdelay_label)

        self.packetsize_label = QLabel(self.scrollAreaWidgetContents)
        self.packetsize_label.setObjectName(u"packetsize_label")
        self.packetsize_label.setMinimumSize(QSize(0, 30))
        self.packetsize_label.setMaximumSize(QSize(16777215, 30))
        self.packetsize_label.setFont(font5)

        self.verticalLayout_11.addWidget(self.packetsize_label)

        self.transmissiondelay_label = QLabel(self.scrollAreaWidgetContents)
        self.transmissiondelay_label.setObjectName(u"transmissiondelay_label")
        self.transmissiondelay_label.setMinimumSize(QSize(0, 30))
        self.transmissiondelay_label.setMaximumSize(QSize(16777215, 30))
        self.transmissiondelay_label.setFont(font5)

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
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.serial_number_combo.setFont(font6)
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
        icon16 = QIcon()
        icon16.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_refresh_available_cams_btn.setIcon(icon16)

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
        self.expo_spinbox.setFont(font6)
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
        self.gain_spinbox.setFont(font6)
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
        self.width_spinbox.setFont(font6)
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
        self.height_spinbox.setFont(font6)
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
        self.offsetx_spinbox.setFont(font6)
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
        self.offsety_spinbox.setFont(font6)
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
        self.trigger_combo.setFont(font6)
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
        self.maxbuffer_spinbox.setFont(font6)
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
        self.packetdelay_spinbox.setFont(font6)
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
        self.packetsize_spinbox.setFont(font6)
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
        self.transmissiondelay_spinbox.setFont(font6)
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
        icon17 = QIcon()
        icon17.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/apply_params.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_setting_apply.setIcon(icon17)
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
        icon18 = QIcon()
        icon18.addFile(u"images_icon/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_camera_connect.setIcon(icon18)
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
        self.BTN_camera_disconnect.setIcon(icon15)
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
        self.gain_label_4.setFont(font5)

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
        self.gain_label_3.setFont(font5)

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
        self.gain_label_5.setFont(font5)

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
        self.gain_label_6.setFont(font5)

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
        self.groupBox_6 = QGroupBox(self.history)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(310, 16777215))
        self.groupBox_6.setFont(font1)
        self.groupBox_6.setStyleSheet(u"QPushButton{\n"
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
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_2 = QScrollArea(self.groupBox_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setFrameShadow(QFrame.Raised)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 267, 330))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setPointSize(10)
        self.label_16.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_16)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_14)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_15)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 30))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_21)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_26)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 30))
        self.label_28.setMaximumSize(QSize(16777215, 30))
        self.label_28.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_28)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 30))
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_29)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 30))
        self.label_30.setMaximumSize(QSize(16777215, 30))
        self.label_30.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_30)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setMaximumSize(QSize(16777215, 30))
        self.label_27.setFont(font7)

        self.verticalLayout_23.addWidget(self.label_27)


        self.horizontalLayout_8.addLayout(self.verticalLayout_23)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.algo_sett_algo_combo = QComboBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_algo_combo.setObjectName(u"algo_sett_algo_combo")
        self.algo_sett_algo_combo.setMinimumSize(QSize(0, 30))
        self.algo_sett_algo_combo.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_algo_combo.setFont(font7)

        self.verticalLayout_32.addWidget(self.algo_sett_algo_combo)

        self.algo_sett_type_combo = QComboBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_type_combo.addItem("")
        self.algo_sett_type_combo.addItem("")
        self.algo_sett_type_combo.setObjectName(u"algo_sett_type_combo")
        self.algo_sett_type_combo.setMinimumSize(QSize(0, 30))
        self.algo_sett_type_combo.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_type_combo.setFont(font7)

        self.verticalLayout_32.addWidget(self.algo_sett_type_combo)

        self.algo_sett_thrs_spin = QSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_thrs_spin.setObjectName(u"algo_sett_thrs_spin")
        self.algo_sett_thrs_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_thrs_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_thrs_spin.setFont(font7)
        self.algo_sett_thrs_spin.setMaximum(255)
        self.algo_sett_thrs_spin.setValue(100)

        self.verticalLayout_32.addWidget(self.algo_sett_thrs_spin)

        self.algo_sett_blur_ksize_spin = QSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_blur_ksize_spin.setObjectName(u"algo_sett_blur_ksize_spin")
        self.algo_sett_blur_ksize_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_blur_ksize_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_blur_ksize_spin.setFont(font7)
        self.algo_sett_blur_ksize_spin.setMinimum(3)
        self.algo_sett_blur_ksize_spin.setMaximum(21)
        self.algo_sett_blur_ksize_spin.setSingleStep(2)
        self.algo_sett_blur_ksize_spin.setValue(3)

        self.verticalLayout_32.addWidget(self.algo_sett_blur_ksize_spin)

        self.algo_sett_ksize_spin = QSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_ksize_spin.setObjectName(u"algo_sett_ksize_spin")
        self.algo_sett_ksize_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_ksize_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_ksize_spin.setFont(font7)
        self.algo_sett_ksize_spin.setMinimum(3)
        self.algo_sett_ksize_spin.setMaximum(21)
        self.algo_sett_ksize_spin.setSingleStep(2)
        self.algo_sett_ksize_spin.setValue(3)

        self.verticalLayout_32.addWidget(self.algo_sett_ksize_spin)

        self.algo_sett_baseline_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_baseline_spin.setObjectName(u"algo_sett_baseline_spin")
        self.algo_sett_baseline_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_baseline_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_baseline_spin.setFont(font7)
        self.algo_sett_baseline_spin.setMinimum(0.000000000000000)
        self.algo_sett_baseline_spin.setMaximum(500.000000000000000)
        self.algo_sett_baseline_spin.setSingleStep(0.010000000000000)
        self.algo_sett_baseline_spin.setValue(90.000000000000000)

        self.verticalLayout_32.addWidget(self.algo_sett_baseline_spin)

        self.algo_sett_pxsize_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_pxsize_spin.setObjectName(u"algo_sett_pxsize_spin")
        self.algo_sett_pxsize_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_pxsize_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_pxsize_spin.setFont(font7)
        self.algo_sett_pxsize_spin.setMinimum(0.000000000000000)
        self.algo_sett_pxsize_spin.setMaximum(10.000000000000000)
        self.algo_sett_pxsize_spin.setSingleStep(0.010000000000000)
        self.algo_sett_pxsize_spin.setValue(5.860000000000000)

        self.verticalLayout_32.addWidget(self.algo_sett_pxsize_spin)

        self.algo_sett_focal_spin = QSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_focal_spin.setObjectName(u"algo_sett_focal_spin")
        self.algo_sett_focal_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_focal_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_focal_spin.setFont(font7)
        self.algo_sett_focal_spin.setMinimum(0)
        self.algo_sett_focal_spin.setMaximum(100)
        self.algo_sett_focal_spin.setSingleStep(1)
        self.algo_sett_focal_spin.setValue(12)

        self.verticalLayout_32.addWidget(self.algo_sett_focal_spin)

        self.algo_sett_widthoffset_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.algo_sett_widthoffset_spin.setObjectName(u"algo_sett_widthoffset_spin")
        self.algo_sett_widthoffset_spin.setMinimumSize(QSize(0, 30))
        self.algo_sett_widthoffset_spin.setMaximumSize(QSize(16777215, 30))
        self.algo_sett_widthoffset_spin.setFont(font7)
        self.algo_sett_widthoffset_spin.setMinimum(-5.000000000000000)
        self.algo_sett_widthoffset_spin.setMaximum(5.000000000000000)
        self.algo_sett_widthoffset_spin.setSingleStep(0.010000000000000)
        self.algo_sett_widthoffset_spin.setValue(0.000000000000000)

        self.verticalLayout_32.addWidget(self.algo_sett_widthoffset_spin)


        self.horizontalLayout_8.addLayout(self.verticalLayout_32)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_22.addWidget(self.scrollArea_2)

        self.algo_sett_apply_btn = QPushButton(self.groupBox_6)
        self.algo_sett_apply_btn.setObjectName(u"algo_sett_apply_btn")
        self.algo_sett_apply_btn.setMinimumSize(QSize(0, 35))
        self.algo_sett_apply_btn.setMaximumSize(QSize(16777215, 35))
        self.algo_sett_apply_btn.setFont(font2)
        self.algo_sett_apply_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_sett_apply_btn.setStyleSheet(u"")
        self.algo_sett_apply_btn.setIcon(icon17)
        self.algo_sett_apply_btn.setIconSize(QSize(16, 16))

        self.verticalLayout_22.addWidget(self.algo_sett_apply_btn)


        self.horizontalLayout_9.addWidget(self.groupBox_6)

        self.groupBox_13 = QGroupBox(self.history)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFont(font1)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_36.setSpacing(5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(10, 10, 10, 10)
        self.sett_cam_control_frame_2 = QFrame(self.groupBox_13)
        self.sett_cam_control_frame_2.setObjectName(u"sett_cam_control_frame_2")
        self.sett_cam_control_frame_2.setEnabled(True)
        self.sett_cam_control_frame_2.setMinimumSize(QSize(0, 40))
        self.sett_cam_control_frame_2.setMaximumSize(QSize(16777215, 40))
        self.sett_cam_control_frame_2.setStyleSheet(u"QPushButton{\n"
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
        self.sett_cam_control_frame_2.setFrameShape(QFrame.Box)
        self.sett_cam_control_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.sett_cam_control_frame_2)
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(10, 0, 10, 0)
        self.algo_setting_connect_camera_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_connect_camera_btn.setObjectName(u"algo_setting_connect_camera_btn")
        self.algo_setting_connect_camera_btn.setEnabled(True)
        self.algo_setting_connect_camera_btn.setMinimumSize(QSize(0, 0))
        self.algo_setting_connect_camera_btn.setMaximumSize(QSize(16777215, 16777215))
        self.algo_setting_connect_camera_btn.setFont(font2)
        self.algo_setting_connect_camera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_setting_connect_camera_btn.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/camera_disconnected.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_connect_camera_btn.setIcon(icon19)
        self.algo_setting_connect_camera_btn.setIconSize(QSize(60, 22))

        self.horizontalLayout_52.addWidget(self.algo_setting_connect_camera_btn)

        self.line_9 = QFrame(self.sett_cam_control_frame_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMaximumSize(QSize(16777215, 25))
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_52.addWidget(self.line_9)

        self.algo_setting_save_results_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_save_results_btn.setObjectName(u"algo_setting_save_results_btn")
        self.algo_setting_save_results_btn.setEnabled(True)
        self.algo_setting_save_results_btn.setMinimumSize(QSize(0, 0))
        self.algo_setting_save_results_btn.setFont(font2)
        self.algo_setting_save_results_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_setting_save_results_btn.setStyleSheet(u"")
        icon20 = QIcon()
        icon20.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_save_results_btn.setIcon(icon20)
        self.algo_setting_save_results_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_52.addWidget(self.algo_setting_save_results_btn)

        self.algo_setting_single_run_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_single_run_btn.setObjectName(u"algo_setting_single_run_btn")
        self.algo_setting_single_run_btn.setEnabled(True)
        self.algo_setting_single_run_btn.setMinimumSize(QSize(0, 0))
        self.algo_setting_single_run_btn.setFont(font2)
        self.algo_setting_single_run_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_setting_single_run_btn.setStyleSheet(u"")
        icon21 = QIcon()
        icon21.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_single_run_btn.setIcon(icon21)
        self.algo_setting_single_run_btn.setIconSize(QSize(21, 21))

        self.horizontalLayout_52.addWidget(self.algo_setting_single_run_btn)

        self.algo_setting_cont_run_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_cont_run_btn.setObjectName(u"algo_setting_cont_run_btn")
        self.algo_setting_cont_run_btn.setEnabled(True)
        self.algo_setting_cont_run_btn.setMinimumSize(QSize(0, 0))
        self.algo_setting_cont_run_btn.setFont(font2)
        self.algo_setting_cont_run_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_setting_cont_run_btn.setStyleSheet(u"QPushButton{\n"
"	padding: 0px;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/play_cont.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_cont_run_btn.setIcon(icon22)
        self.algo_setting_cont_run_btn.setIconSize(QSize(35, 32))

        self.horizontalLayout_52.addWidget(self.algo_setting_cont_run_btn)

        self.algo_setting_stop_run_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_stop_run_btn.setObjectName(u"algo_setting_stop_run_btn")
        self.algo_setting_stop_run_btn.setEnabled(True)
        self.algo_setting_stop_run_btn.setMinimumSize(QSize(0, 0))
        self.algo_setting_stop_run_btn.setFont(font2)
        self.algo_setting_stop_run_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon23 = QIcon()
        icon23.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_stop_run_btn.setIcon(icon23)
        self.algo_setting_stop_run_btn.setIconSize(QSize(21, 21))

        self.horizontalLayout_52.addWidget(self.algo_setting_stop_run_btn)

        self.line_7 = QFrame(self.sett_cam_control_frame_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 25))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_52.addWidget(self.line_7)

        self.algo_sett_res_zoomin = QPushButton(self.sett_cam_control_frame_2)
        self.algo_sett_res_zoomin.setObjectName(u"algo_sett_res_zoomin")
        self.algo_sett_res_zoomin.setEnabled(True)
        self.algo_sett_res_zoomin.setMinimumSize(QSize(0, 0))
        self.algo_sett_res_zoomin.setFont(font2)
        self.algo_sett_res_zoomin.setCursor(QCursor(Qt.PointingHandCursor))
        icon24 = QIcon()
        icon24.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_sett_res_zoomin.setIcon(icon24)
        self.algo_sett_res_zoomin.setIconSize(QSize(21, 21))

        self.horizontalLayout_52.addWidget(self.algo_sett_res_zoomin)

        self.algo_sett_res_zoomout = QPushButton(self.sett_cam_control_frame_2)
        self.algo_sett_res_zoomout.setObjectName(u"algo_sett_res_zoomout")
        self.algo_sett_res_zoomout.setEnabled(True)
        self.algo_sett_res_zoomout.setMinimumSize(QSize(0, 0))
        self.algo_sett_res_zoomout.setFont(font2)
        self.algo_sett_res_zoomout.setCursor(QCursor(Qt.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_sett_res_zoomout.setIcon(icon25)
        self.algo_sett_res_zoomout.setIconSize(QSize(21, 21))

        self.horizontalLayout_52.addWidget(self.algo_sett_res_zoomout)

        self.algo_sett_res_strech = QPushButton(self.sett_cam_control_frame_2)
        self.algo_sett_res_strech.setObjectName(u"algo_sett_res_strech")
        self.algo_sett_res_strech.setEnabled(True)
        self.algo_sett_res_strech.setMinimumSize(QSize(0, 0))
        self.algo_sett_res_strech.setFont(font2)
        self.algo_sett_res_strech.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/zoom-strech.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_sett_res_strech.setIcon(icon26)
        self.algo_sett_res_strech.setIconSize(QSize(20, 20))

        self.horizontalLayout_52.addWidget(self.algo_sett_res_strech)

        self.line_8 = QFrame(self.sett_cam_control_frame_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(16777215, 25))
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_52.addWidget(self.line_8)

        self.algo_setting_cnts_btn = QPushButton(self.sett_cam_control_frame_2)
        self.algo_setting_cnts_btn.setObjectName(u"algo_setting_cnts_btn")
        self.algo_setting_cnts_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.algo_setting_cnts_btn.setStyleSheet(u"QPushButton:checked {\n"
"	background:#a3a3a3;\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u"C:/Users/Dorsa-Admin/.designer/backup/Icons/contours.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algo_setting_cnts_btn.setIcon(icon27)
        self.algo_setting_cnts_btn.setIconSize(QSize(20, 20))
        self.algo_setting_cnts_btn.setCheckable(True)

        self.horizontalLayout_52.addWidget(self.algo_setting_cnts_btn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_9)


        self.verticalLayout_36.addWidget(self.sett_cam_control_frame_2)

        self.algo_sett_result_frame = QFrame(self.groupBox_13)
        self.algo_sett_result_frame.setObjectName(u"algo_sett_result_frame")
        self.algo_sett_result_frame.setFrameShape(QFrame.WinPanel)
        self.algo_sett_result_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_37 = QVBoxLayout(self.algo_sett_result_frame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_12 = QLabel(self.algo_sett_result_frame)
        self.label_12.setObjectName(u"label_12")
        font8 = QFont()
        font8.setPointSize(81)
        self.label_12.setFont(font8)

        self.verticalLayout_38.addWidget(self.label_12)


        self.verticalLayout_37.addLayout(self.verticalLayout_38)


        self.verticalLayout_36.addWidget(self.algo_sett_result_frame)

        self.frame_78 = QFrame(self.groupBox_13)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 40))
        self.frame_78.setMaximumSize(QSize(16777215, 40))
        self.frame_78.setFrameShape(QFrame.Box)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.gain_label_9 = QLabel(self.frame_78)
        self.gain_label_9.setObjectName(u"gain_label_9")
        self.gain_label_9.setMinimumSize(QSize(0, 0))
        self.gain_label_9.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_9.setFont(font5)

        self.horizontalLayout_36.addWidget(self.gain_label_9)

        self.sett_algo_width = QLabel(self.frame_78)
        self.sett_algo_width.setObjectName(u"sett_algo_width")
        self.sett_algo_width.setMinimumSize(QSize(0, 30))
        self.sett_algo_width.setMaximumSize(QSize(16777215, 30))
        self.sett_algo_width.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_algo_width.setFrameShape(QFrame.Panel)
        self.sett_algo_width.setFrameShadow(QFrame.Sunken)
        self.sett_algo_width.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.sett_algo_width)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.gain_label_8 = QLabel(self.frame_78)
        self.gain_label_8.setObjectName(u"gain_label_8")
        self.gain_label_8.setMinimumSize(QSize(0, 0))
        self.gain_label_8.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_8.setFont(font5)

        self.horizontalLayout_35.addWidget(self.gain_label_8)

        self.sett_algo_fps = QLabel(self.frame_78)
        self.sett_algo_fps.setObjectName(u"sett_algo_fps")
        self.sett_algo_fps.setMinimumSize(QSize(0, 30))
        self.sett_algo_fps.setMaximumSize(QSize(16777215, 30))
        self.sett_algo_fps.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_algo_fps.setFrameShape(QFrame.Panel)
        self.sett_algo_fps.setFrameShadow(QFrame.Sunken)
        self.sett_algo_fps.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.sett_algo_fps)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.gain_label_10 = QLabel(self.frame_78)
        self.gain_label_10.setObjectName(u"gain_label_10")
        self.gain_label_10.setMinimumSize(QSize(0, 0))
        self.gain_label_10.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_10.setFont(font5)

        self.horizontalLayout_37.addWidget(self.gain_label_10)

        self.sett_algo_errors = QLabel(self.frame_78)
        self.sett_algo_errors.setObjectName(u"sett_algo_errors")
        self.sett_algo_errors.setMinimumSize(QSize(0, 30))
        self.sett_algo_errors.setMaximumSize(QSize(16777215, 30))
        self.sett_algo_errors.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_algo_errors.setFrameShape(QFrame.Panel)
        self.sett_algo_errors.setFrameShadow(QFrame.Sunken)
        self.sett_algo_errors.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.sett_algo_errors)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.gain_label_11 = QLabel(self.frame_78)
        self.gain_label_11.setObjectName(u"gain_label_11")
        self.gain_label_11.setMinimumSize(QSize(0, 0))
        self.gain_label_11.setMaximumSize(QSize(16777215, 16777215))
        self.gain_label_11.setFont(font5)

        self.horizontalLayout_38.addWidget(self.gain_label_11)

        self.sett_algo_grabbing_errors = QLabel(self.frame_78)
        self.sett_algo_grabbing_errors.setObjectName(u"sett_algo_grabbing_errors")
        self.sett_algo_grabbing_errors.setMinimumSize(QSize(0, 30))
        self.sett_algo_grabbing_errors.setMaximumSize(QSize(16777215, 30))
        self.sett_algo_grabbing_errors.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.sett_algo_grabbing_errors.setFrameShape(QFrame.Panel)
        self.sett_algo_grabbing_errors.setFrameShadow(QFrame.Sunken)
        self.sett_algo_grabbing_errors.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.sett_algo_grabbing_errors)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_38)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_10)


        self.verticalLayout_36.addWidget(self.frame_78)


        self.horizontalLayout_9.addWidget(self.groupBox_13)

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
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 286, 321))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.LBL_laserDTH = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_laserDTH.setObjectName(u"LBL_laserDTH")
        self.LBL_laserDTH.setMinimumSize(QSize(0, 30))
        self.LBL_laserDTH.setMaximumSize(QSize(16777215, 30))
        self.LBL_laserDTH.setFont(font7)

        self.verticalLayout_17.addWidget(self.LBL_laserDTH)

        self.LBL_norm = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_norm.setObjectName(u"LBL_norm")
        self.LBL_norm.setMinimumSize(QSize(0, 30))
        self.LBL_norm.setMaximumSize(QSize(16777215, 30))
        self.LBL_norm.setFont(font7)

        self.verticalLayout_17.addWidget(self.LBL_norm)

        self.LBL_th1 = QLabel(self.scrollAreaWidgetContents_4)
        self.LBL_th1.setObjectName(u"LBL_th1")
        self.LBL_th1.setMinimumSize(QSize(0, 30))
        self.LBL_th1.setMaximumSize(QSize(16777215, 30))
        self.LBL_th1.setFont(font7)

        self.verticalLayout_17.addWidget(self.LBL_th1)

        self.L = QLabel(self.scrollAreaWidgetContents_4)
        self.L.setObjectName(u"L")
        self.L.setMinimumSize(QSize(0, 30))
        self.L.setMaximumSize(QSize(16777215, 30))
        self.L.setFont(font7)

        self.verticalLayout_17.addWidget(self.L)


        self.horizontalLayout_12.addLayout(self.verticalLayout_17)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.spinBox_laserDTH = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_laserDTH.setObjectName(u"spinBox_laserDTH")
        self.spinBox_laserDTH.setMinimumSize(QSize(0, 30))
        self.spinBox_laserDTH.setMaximumSize(QSize(16777215, 30))
        self.spinBox_laserDTH.setFont(font7)
        self.spinBox_laserDTH.setMinimum(5.000000000000000)
        self.spinBox_laserDTH.setMaximum(500.000000000000000)
        self.spinBox_laserDTH.setSingleStep(0.010000000000000)
        self.spinBox_laserDTH.setValue(40.000000000000000)

        self.verticalLayout_20.addWidget(self.spinBox_laserDTH)

        self.spinBox_norm = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.spinBox_norm.setObjectName(u"spinBox_norm")
        self.spinBox_norm.setMinimumSize(QSize(0, 30))
        self.spinBox_norm.setMaximumSize(QSize(16777215, 30))
        self.spinBox_norm.setFont(font7)
        self.spinBox_norm.setMinimum(5.000000000000000)
        self.spinBox_norm.setMaximum(500.000000000000000)
        self.spinBox_norm.setSingleStep(0.010000000000000)
        self.spinBox_norm.setValue(40.000000000000000)

        self.verticalLayout_20.addWidget(self.spinBox_norm)

        self.calib_sett_rect_dist_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.calib_sett_rect_dist_spin.setObjectName(u"calib_sett_rect_dist_spin")
        self.calib_sett_rect_dist_spin.setMinimumSize(QSize(0, 30))
        self.calib_sett_rect_dist_spin.setMaximumSize(QSize(16777215, 30))
        self.calib_sett_rect_dist_spin.setFont(font7)
        self.calib_sett_rect_dist_spin.setMinimum(5.000000000000000)
        self.calib_sett_rect_dist_spin.setMaximum(500.000000000000000)
        self.calib_sett_rect_dist_spin.setSingleStep(0.010000000000000)
        self.calib_sett_rect_dist_spin.setValue(50.000000000000000)

        self.verticalLayout_20.addWidget(self.calib_sett_rect_dist_spin)

        self.calib_sett_baseline_spin = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.calib_sett_baseline_spin.setObjectName(u"calib_sett_baseline_spin")
        self.calib_sett_baseline_spin.setMinimumSize(QSize(0, 30))
        self.calib_sett_baseline_spin.setMaximumSize(QSize(16777215, 30))
        self.calib_sett_baseline_spin.setFont(font7)
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
        self.BTN_algo_param_setting.setIcon(icon17)
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
        self.BTN_laser_detector_connect.setIcon(icon18)
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
        self.BTN_laser_detector_disconnect.setIcon(icon15)
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
        font9 = QFont()
        font9.setPointSize(11)
        self.msg_label.setFont(font9)
        self.msg_label.setFrameShape(QFrame.WinPanel)
        self.msg_label.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.msg_label)


        self.horizontalLayout_5.addWidget(self.message)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.status_frame)


        self.verticalLayout.addWidget(self.middle)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 25))
        self.footer.setMaximumSize(QSize(16777215, 25))
        self.footer.setStyleSheet(u"background: #2C313A;")
        self.footer.setFrameShape(QFrame.WinPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.footer)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 10, 0)

        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


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
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"System Setup", None))
#if QT_CONFIG(tooltip)
        self.dash_cam_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Camera</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dash_cam_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Open Cameras", None))
#if QT_CONFIG(tooltip)
        self.camera_setting_connect_btn_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Camera</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.camera_setting_connect_btn_6.setText(QCoreApplication.translate("MainWindow", u"Open I/O", None))
#if QT_CONFIG(tooltip)
        self.dash_run_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Camera</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dash_run_btn.setText(QCoreApplication.translate("MainWindow", u"Run System", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"System Status", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Cameras Ready", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"I/O Ready", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"System Operating", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Coil Detected", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Width Low Threshold", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Width High Threshold", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Coil Parameters", None))
        self.dash_coilid_lineedit.setText("")
        self.dash_coillthick_lineedit.setText("")
        self.dash_setpoint_lineedit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coil ID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Length (mm)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Thickness (mm)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Width Setpoint (mm)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"High/Low Threshold (mm)", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Width Statistics", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Width Deviation (mm)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Width Average (mm)", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Minimum Width (mm)", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Maximum Width (mm)", None))
        self.dash_dev_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dash_avg_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dash_min_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dash_max_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.dash_show_visuals_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show All Edges</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dash_show_visuals_btn.setText(QCoreApplication.translate("MainWindow", u"Visual Results", None))
#if QT_CONFIG(tooltip)
        self.dash_show_chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show All Edges</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dash_show_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Trend Chart", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Current Width (mm)", None))
        self.dash_curr_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
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
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Algorithm Parameters", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Edge Detection Type", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Gray Threshold Value", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Blur Kernel Size", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Kernel Size", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Baseline (mm)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pixel Size (\u00b5m)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Focal Length (mm)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Width Offset (mm)", None))
        self.algo_sett_type_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.algo_sett_type_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Edge Detection", None))

#if QT_CONFIG(tooltip)
        self.algo_sett_apply_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Apply/Save Parameters</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_sett_apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply/Save Parameters", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Live Results", None))
#if QT_CONFIG(tooltip)
        self.algo_setting_connect_camera_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Open Cameras</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_connect_camera_btn.setText("")
#if QT_CONFIG(tooltip)
        self.algo_setting_save_results_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Save Results</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_save_results_btn.setText("")
#if QT_CONFIG(tooltip)
        self.algo_setting_single_run_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Single Run</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_single_run_btn.setText("")
#if QT_CONFIG(tooltip)
        self.algo_setting_cont_run_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Continuous Run</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_cont_run_btn.setText("")
#if QT_CONFIG(tooltip)
        self.algo_setting_stop_run_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Stop</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_stop_run_btn.setText("")
#if QT_CONFIG(tooltip)
        self.algo_sett_res_zoomin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Zoom In</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_sett_res_zoomin.setText("")
#if QT_CONFIG(tooltip)
        self.algo_sett_res_zoomout.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Zoom Out</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_sett_res_zoomout.setText("")
#if QT_CONFIG(tooltip)
        self.algo_sett_res_strech.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400;\">Zoom to Fit</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_sett_res_strech.setText("")
#if QT_CONFIG(tooltip)
        self.algo_setting_cnts_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Show All Edges</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.algo_setting_cnts_btn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.gain_label_9.setText(QCoreApplication.translate("MainWindow", u"Measured Width", None))
        self.sett_algo_width.setText("")
        self.gain_label_8.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.sett_algo_fps.setText("")
        self.gain_label_10.setText(QCoreApplication.translate("MainWindow", u"Algorithm Errors", None))
        self.sett_algo_errors.setText("")
        self.gain_label_11.setText(QCoreApplication.translate("MainWindow", u"Frame Grabbing Errors", None))
        self.sett_algo_grabbing_errors.setText("")
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

