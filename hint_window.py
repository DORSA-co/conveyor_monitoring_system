import sys
import cv2
import numpy as np
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
import PySide6.QtGui as PG
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PyQt5.QtGui import QPainter
from PySide6.QtWidgets import QMessageBox as sQMessageBox
from PySide6.QtGui import QPixmap as sQPixmap
from PySide6.QtGui import QIcon as sQIcon
from PySide6.QtGui import QIntValidator as sQIntValidator
from PySide6 import QtCore as sQtCore
from PySide6.QtCore import QObject, QThread, Signal
from functools import partial


ui, _ = loadUiType("UI\defect_hint.ui")
os.environ["QT_FONT_DPI"] = "96"


class UI_hint_window(QMainWindow, ui):
    def __init__(self):
        """
        create init variables
        """

        super(UI_hint_window, self).__init__()
        self.ui = ui
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None
        self.pos_ = self.pos()

        self.detail_of_segment = {}
        self.detail_of_segment["defects_depth_list"] = []
        self.detail_of_segment["defects_type_list"] = []
        self.detail_of_segment["defects_area_list"] = []
        self.detail_of_segment["defects_ypixel_list"] = []
        self.detail_of_segment["defects_xpixel_list"] = []
        # self.detail_of_segment["defects_boundbox_list"] = []
        self.detail_of_segment["defects_position_list"] = []

    def rest_detail_info(self):
        self.detail_of_segment = {}
        self.detail_of_segment["defects_depth_list"] = []
        self.detail_of_segment["defects_type_list"] = []
        self.detail_of_segment["defects_area_list"] = []
        self.detail_of_segment["defects_ypixel_list"] = []
        self.detail_of_segment["defects_xpixel_list"] = []
        # self.detail_of_segment["defects_boundbox_list"] = []
        self.detail_of_segment["defects_position_list"] = []

    def load_detail(self, annotation, path):

        detail = annotation.read(path)
        self.detail_of_segment["defects_ypixel_list"] = detail["defects_ypixel_list"]
        self.detail_of_segment["defects_xpixel_list"] = detail["defects_xpixel_list"]
        # self.detail_of_segment["defects_boundbox_list"] = detail[
        #     "defects_boundbox_list"
        # ]
        self.detail_of_segment["defects_position_list"] = detail[
            "defects_position_list"
        ]

        self.detail_of_segment["defects_depth_list"] = detail["defects_depth_list"]
        self.detail_of_segment["defects_type_list"] = detail["defects_type_list"]
        self.detail_of_segment["defects_area_list"] = detail["defects_area_list"]

    def get_detail_of_segment_info(self, key):
        return self.detail_of_segment[key]


if __name__ == "__main__":
    app = QApplication()
    win = UI_hint_window()
    win.show()
    sys.exit(app.exec())
