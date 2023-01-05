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


ui, _ = loadUiType("UI/popup_window.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
NO_IMAGE = cv2.imread(r"UI\images_icon\no_image.png")
default_details = {
    "date": "-",
    "loc": "-",
    "area": "-",
    "type": "-",
    "p": "-",
    "depth": "-",
}
DEBUG_UI = False


class UI_popup_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0
    _i_ = -1
    temp_image_folder = os.listdir(r"images\Newfolder3")

    def __init__(self):
        """
        create init variables
        """

        super(UI_popup_window, self).__init__()
        self.ui = ui
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self._old_pos = None
        self.pos_ = self.pos()
        self.update_image_details()

    def mousePressEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): left or right click for drag window
        Returns: None
        """
        if event.button() == QtCore.Qt.LeftButton:
            if event.position().y() <= self.header.height():
                self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): release Event for update drag window
        Returns: None
        """
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): when click and move mouse for drag window
        Returns: None
        """

        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        if not self.isMaximized():
            self.move(self.pos() + delta)

    def activate_(self):
        """main butoons connect -- exit , minize , maximize, help --"""
        self.close_btn.clicked.connect(self.close_win)
        self.minimize_btn.clicked.connect(self.minimize)
        self.maximize_btn.clicked.connect(self.maxmize_minimize)

    def minimize(self):
        """Minimize winodw"""
        self.showMinimized()

    def close_win(self):
        """Close window"""
        self.close()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        if self.isMaximized():

            self.showNormal()
        else:
            self.showMaximized()

    def set_image_label(self, label_name, img):
        """set imnage in input label"""
        if len(img.shape) != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(
            img.data, w, h, bytes_per_line, sQImage.Format_RGB888
        )
        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def update_image_details(self, image=NO_IMAGE, details=default_details):

        try:
            self.update_details(details=details)
        except:
            self.update_details(details=default_details)
        try:
            self.set_image_label(self.label_image, image)
        except:
            self.set_image_label(self.label_image, NO_IMAGE)

    def update_details(self, details):
        pass
        # self.label_loc.setText(details["loc"])
        # self.label_area.setText(details["area"])
        # self.label_type.setText(details["type"])
        # self.label_p.setText(details["p"])
        # self.label_depth.setText(details["depth"])
        # self.label_date.setText(details["date"])

    def set_and_update_schematic(self, mask, id, postion):
        self.set_image_label(self.label_image, mask)
        self.LBL_segment_ID_value.setText(str(id))
        self.LBL_segment_position_value.setText(str(postion))


if __name__ == "__main__":
    app = QApplication()
    win = UI_popup_window()
    win.show()
    sys.exit(app.exec())
