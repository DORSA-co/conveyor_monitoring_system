# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 721)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 5, 0)
        self.BTN_toggle = QPushButton(self.frame_2)
        self.BTN_toggle.setObjectName(u"BTN_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_toggle.sizePolicy().hasHeightForWidth())
        self.BTN_toggle.setSizePolicy(sizePolicy)
        self.BTN_toggle.setMinimumSize(QSize(0, 40))
        self.BTN_toggle.setMaximumSize(QSize(60, 40))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.BTN_toggle.setFont(font)
        self.BTN_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_toggle.setLayoutDirection(Qt.LeftToRight)
        self.BTN_toggle.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);\n"
"border:None;\n"
"")
        icon = QIcon()
        icon.addFile(u"images_icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_toggle.setIcon(icon)
        self.BTN_toggle.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.BTN_toggle)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(110, 16777215))
        self.label_2.setPixmap(QPixmap(u"images_icon/whitew.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.helpButton = QPushButton(self.frame_2)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMinimumSize(QSize(28, 28))
        self.helpButton.setMaximumSize(QSize(28, 28))
        self.helpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../../../JJ/New folder/trainApp_oxin/UI/images/icons/icon_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon1)
        self.helpButton.setIconSize(QSize(17, 17))

        self.horizontalLayout.addWidget(self.helpButton)

        self.miniButton = QPushButton(self.frame_2)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setMinimumSize(QSize(28, 28))
        self.miniButton.setMaximumSize(QSize(28, 28))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../../JJ/New folder/trainApp_oxin/UI/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon2)
        self.miniButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.miniButton)

        self.maxiButton = QPushButton(self.frame_2)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setMinimumSize(QSize(28, 28))
        self.maxiButton.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maxiButton.setFont(font1)
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../../../JJ/New folder/trainApp_oxin/UI/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon3)
        self.maxiButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.maxiButton)

        self.closeButton = QPushButton(self.frame_2)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(28, 28))
        self.closeButton.setMaximumSize(QSize(28, 28))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"../../../JJ/New folder/trainApp_oxin/UI/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon4)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(70, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.BTN_toggle_2 = QPushButton(self.frame_4)
        self.BTN_toggle_2.setObjectName(u"BTN_toggle_2")
        sizePolicy.setHeightForWidth(self.BTN_toggle_2.sizePolicy().hasHeightForWidth())
        self.BTN_toggle_2.setSizePolicy(sizePolicy)
        self.BTN_toggle_2.setMinimumSize(QSize(0, 40))
        self.BTN_toggle_2.setMaximumSize(QSize(60, 40))
        self.BTN_toggle_2.setFont(font)
        self.BTN_toggle_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_toggle_2.setLayoutDirection(Qt.LeftToRight)
        self.BTN_toggle_2.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"images_icon/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_toggle_2.setIcon(icon5)
        self.BTN_toggle_2.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.BTN_toggle_2)

        self.BTN_toggle_3 = QPushButton(self.frame_4)
        self.BTN_toggle_3.setObjectName(u"BTN_toggle_3")
        sizePolicy.setHeightForWidth(self.BTN_toggle_3.sizePolicy().hasHeightForWidth())
        self.BTN_toggle_3.setSizePolicy(sizePolicy)
        self.BTN_toggle_3.setMinimumSize(QSize(0, 40))
        self.BTN_toggle_3.setMaximumSize(QSize(60, 40))
        self.BTN_toggle_3.setFont(font)
        self.BTN_toggle_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_toggle_3.setLayoutDirection(Qt.LeftToRight)
        self.BTN_toggle_3.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"images_icon/calibration.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_toggle_3.setIcon(icon6)
        self.BTN_toggle_3.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.BTN_toggle_3)

        self.BTN_toggle_4 = QPushButton(self.frame_4)
        self.BTN_toggle_4.setObjectName(u"BTN_toggle_4")
        sizePolicy.setHeightForWidth(self.BTN_toggle_4.sizePolicy().hasHeightForWidth())
        self.BTN_toggle_4.setSizePolicy(sizePolicy)
        self.BTN_toggle_4.setMinimumSize(QSize(0, 40))
        self.BTN_toggle_4.setMaximumSize(QSize(60, 40))
        self.BTN_toggle_4.setFont(font)
        self.BTN_toggle_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTN_toggle_4.setLayoutDirection(Qt.LeftToRight)
        self.BTN_toggle_4.setStyleSheet(u"background-image: url(:/icons/images/icons/t1.png);\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images_icon/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BTN_toggle_4.setIcon(icon7)
        self.BTN_toggle_4.setIconSize(QSize(35, 35))

        self.verticalLayout_2.addWidget(self.BTN_toggle_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamilies([u"MS Reference Sans Serif"])
        font2.setPointSize(15)
        self.label.setFont(font2)

        self.verticalLayout_3.addWidget(self.label)

        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 1000))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LBL_LiveHeatMap = QLabel(self.frame_7)
        self.LBL_LiveHeatMap.setObjectName(u"LBL_LiveHeatMap")
        self.LBL_LiveHeatMap.setMaximumSize(QSize(16777215, 1000))
        self.LBL_LiveHeatMap.setFrameShape(QFrame.Panel)
        self.LBL_LiveHeatMap.setFrameShadow(QFrame.Plain)
        self.LBL_LiveHeatMap.setLineWidth(2)

        self.horizontalLayout_4.addWidget(self.LBL_LiveHeatMap)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 1000))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LBL_rawmap = QLabel(self.frame_6)
        self.LBL_rawmap.setObjectName(u"LBL_rawmap")
        self.LBL_rawmap.setMaximumSize(QSize(16777215, 1000))
        self.LBL_rawmap.setFrameShape(QFrame.Panel)
        self.LBL_rawmap.setFrameShadow(QFrame.Plain)
        self.LBL_rawmap.setLineWidth(2)
        self.LBL_rawmap.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.LBL_rawmap)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.trend_chart_frame = QFrame(self.page_2)
        self.trend_chart_frame.setObjectName(u"trend_chart_frame")
        self.trend_chart_frame.setMinimumSize(QSize(900, 600))
        self.trend_chart_frame.setMaximumSize(QSize(16777215, 16777215))
        self.trend_chart_frame.setFrameShape(QFrame.StyledPanel)
        self.trend_chart_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.trend_chart_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addWidget(self.trend_chart_frame)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 10))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1053, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BTN_toggle.setText("")
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText("")
#if QT_CONFIG(tooltip)
        self.miniButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniButton.setText("")
#if QT_CONFIG(tooltip)
        self.maxiButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxiButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.BTN_toggle_2.setText("")
        self.BTN_toggle_3.setText("")
        self.BTN_toggle_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Conveyor Monitoring System", None))
        self.LBL_LiveHeatMap.setText("")
        self.LBL_rawmap.setText("")
    # retranslateUi

