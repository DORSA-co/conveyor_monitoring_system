import sys
import cv2, random
import numpy as np
import threading, datetime
from datetime import datetime
import time
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
from utils.heatmap import heatmap
from utils.laserScaner import ProfileMeter
from utils.camera_connection import Collector
from backend.database import dataBase
from utils.move_on_list import moveOnList, moveOnImagrList
from utils.slider import (
    create_image_slider_on_ui,
    update_defect_images_on_ui,
    set_image_to_ui_slider_full_path,
    set_label_style,
    update_imagesslider_on_ui,
)
from functools import partial
from popup_window import UI_popup_window
from utils.json_modules import Annotation
from backend import date_module


WIDTH = 3840
SHOW_BOUND = 900
PATH_DEFECT_SPLIT = r"defect_split"
NO_IMAGE = cv2.imread(r"UI\images_icon\no_image.png")
image_open_camera = "UI\images_icon\camera_connected.png"
image_close_camera = "UI\images_icon\camera_disconnected.png"
segments_info = r"segments_info"

ui, _ = loadUiType("UI/main_UI.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SOME FLAGES
DEBUG_UI = False
WRITE = False
GET_LIVE_PICTURE = False

# algo param:
mean_index = 10
weights = np.zeros((mean_index, WIDTH))
weights[0 : mean_index // 3, :] = 1
weights[mean_index // 3 : 2 * (mean_index // 3)] = 10
weights[2 * (mean_index // 3), :] = 20
stack_row = np.zeros((mean_index, WIDTH))


limited_deviation_from_base = 30
disputed_pixel_threshold = 10
final_output_medianBlur_kernel = 5
final_output_threshold_kernel = 240
# _______________________________________________


def moving_average(a, n=50):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return (ret[n - 1 :] / n).astype("uint32")


def average_moveing_contour(cnt):

    x = moving_average(cnt[:, 0, 0])
    y = moving_average(cnt[:, 0, 1])
    return x, y


class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0

    # ______________temp vars for image loading________________________
    image_index = 0
    image_path = r"images\Newfolder3"
    temp_image_folder = os.listdir(image_path)
    # ______________temp vars for image loading________________________

    def __init__(self):
        """
        create init variables
        """

        super(UI_main_window, self).__init__()
        self.ui = ui
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.statusBar().setMaximumHeight(5)

        # algo parameter
        self.laser_detector_threshold = 1
        self.laser_detector_medianBlur_kernel = 5

        self.create_path = True
        if not os.path.exists(PATH_DEFECT_SPLIT):
            os.mkdir(PATH_DEFECT_SPLIT)

        # popup window
        self.popup_window_obj = UI_popup_window()

        # database obj
        self.db = dataBase()
        self.eror_img = 0
        self.camera = None

        self.qimage = QImage(
            NO_IMAGE, NO_IMAGE.shape[1], NO_IMAGE.shape[0], QImage.Format_RGB888
        )
        self.pixmap = QPixmap(self.qimage)
        self.pixmap = self.pixmap.scaled(
            NO_IMAGE.shape[0], NO_IMAGE.shape[1], Qt.KeepAspectRatio
        )

        self.current_segment = np.ones((SHOW_BOUND, WIDTH, 3), np.uint8) * 255

        # speed parameter###################################################
        self.pixel_size = 0.00647  # cm
        self.Vpps = 120 / 13.5  # pixel per secend
        self.fps = 47.7
        self.tpf = 1 / 47.7  # time per frame =1/fps
        self.rate = 30  # int(v*tpf)#pixel per frame
        self.speed_rate = 100 / (self.rate * 14 * self.fps)  # cm per frame
        self.belt_height = 10000

        # position param................................
        self.num_frames = 0
        self.process_flag = False
        self.frame_per_roll = 500
        self.index_of_scanning_segment = -1
        self.index_slider = 0
        self.segment_index = 0
        self.frame_pre_segment = 30
        self.image_pre_row = 6
        self.first_point = 0
        self.update_step = int(SHOW_BOUND // self.rate)
        self.last_point = self.update_step

        # camera setting##############################
        self.laod_camera_parms()
        self.load_camera_calibration()
        # algo tool setting
        self.widget_connector()
        self.profile = ProfileMeter()
        self.mask = heatmap(WIDTH, chanel=1)
        self.z_heatmap = heatmap(WIDTH, chanel=1, creat_total_32=True)

        self._old_pos = None
        self.pos_ = self.pos()
        # camera connection
        self.live_flag = False
        self.detect_flag = False

        self.set_image_label(self.LBL_live_camera, NO_IMAGE)

        self.timer_live = QTimer(self)
        self.timer_live.timeout.connect(self.set_live_image)

        self.timer_live_detect = QTimer(self)
        self.timer_live_detect.timeout.connect(self.surface_scanning)

        # self.timer_save_segment_schematic = QTimer(self)
        # self.timer_save_segment_schematic.timeout.connect(self.save_segment_schematic)

        # _____________________________should check_____________________________
        self.save_defect_images_list_name_file = []
        self.save_defect_images_list = []
        self.timer_save_defect_images = QTimer(self)
        self.timer_save_defect_images.timeout.connect(self.write_defect_images)

        self.defect_slider_show = QTimer(self)
        self.defect_slider_show.timeout.connect(self.UpDate_Slider)
        self.current_image_list = []
        self.json_list = []
        # __________________________________________________________

        self.segment_path = []
        self.create_segment_slider()
        self.segment_name = "segment"
        self.segment_image_list = moveOnImagrList(
            sub_directory=segments_info,
        )
        self.segment_image_list.add(self.segment_path, self.segment_name)
        self.segment_image_list_next_func = self.segment_image_list.build_next_func(
            name=self.segment_name
        )
        self.segment_image_list_prev_func = self.segment_image_list.build_prev_func(
            name=self.segment_name
        )
        update_imagesslider_on_ui(ui_obj=self)
        self.defects_prev_btn_3.clicked.connect(
            partial(lambda: update_imagesslider_on_ui(ui_obj=self, prevornext="prev"))
        )
        self.defects_next_btn_3.clicked.connect(
            partial(lambda: update_imagesslider_on_ui(ui_obj=self, prevornext="next"))
        )

        self.width_spinbox.valueChanged.connect(self.update_pixel_value)
        self.spinBox_pixel_value.valueChanged.connect(self.update_pixel_value)
        self.BTN_history.clicked.connect(self.load_history)

        self.segment_detail_list = {}

        self.expo_spinbox.valueChanged.connect(
            lambda: self.update_camera_parms("exposure")
        )
        self.gain_spinbox.valueChanged.connect(lambda: self.update_camera_parms("gain"))
        self.offsetx_spinbox.valueChanged.connect(
            lambda: self.update_camera_parms("offsetx")
        )
        self.offsety_spinbox.valueChanged.connect(
            lambda: self.update_camera_parms("offsety")
        )

    def update_camera_parms(self, parm):
        if parm == "exposure":
            try:
                self.camera.update_exposure(self.expo_spinbox.value())
            except:
                pass
        elif parm == "gain":
            try:
                self.camera.upadte_gain(self.gain_spinbox.value())
            except:
                pass
        elif parm == "offsetx":
            try:
                self.camera.update_offsetx(self.offsetx_spinbox.value())
            except:
                pass

        elif parm == "offsety":
            try:
                self.camera.update_offsety(self.offsety_spinbox.value())
            except:
                pass

    # ___________________________________________segment handling part
    def create_segment_slider(self):

        i = 0
        self.segment_annotation = Annotation()
        image_per_row = self.image_pre_row
        frame_longitudinal_precision = self.frame_per_roll // self.frame_pre_segment
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(frame_longitudinal_precision):

            segment_shematic = np.ones((224, 224, 3), np.uint8)
            segment_shematic[:, :, 0] = 225
            segment_shematic[:, :, 1] = 230
            segment_shematic[:, :, 2] = 237
            segment_shematic = cv2.cvtColor(segment_shematic, cv2.COLOR_RGB2BGR)

            color_put_text = (0, 80, 0)
            thickness = 1

            ranges = "{}".format(i * self.frame_pre_segment)
            temp = cv2.putText(
                segment_shematic,
                ranges,
                (80, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color_put_text,
                thickness,
            )
            ranges = "{}".format((i + 1) * self.frame_pre_segment)
            temp = cv2.putText(
                segment_shematic,
                ranges,
                (80, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color_put_text,
                thickness,
            )
            if not (os.path.exists(os.path.join(segments_info, str(i)))):
                os.mkdir(os.path.join(segments_info, str(i)))
                cv2.imwrite(os.path.join(segments_info, str(i), str(i) + ".jpg"), temp)
            self.segment_path.append(
                os.path.join(segments_info, str(i), str(i) + ".jpg")
            )

        if (self.frame_per_roll % self.frame_pre_segment) != 0:
            ranges = "{}".format((i + 1) * self.frame_pre_segment)
            segment_shematic = np.ones((224, 224, 3), np.uint8)
            segment_shematic[:, :, 0] = 225
            segment_shematic[:, :, 1] = 230
            segment_shematic[:, :, 2] = 237
            segment_shematic = cv2.cvtColor(segment_shematic, cv2.COLOR_RGB2BGR)
            temp = cv2.putText(
                segment_shematic,
                ranges,
                (100, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                4,
            )
            temp = cv2.putText(
                segment_shematic,
                str(self.frame_per_roll),
                (100, 170),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                4,
            )
            if not (os.path.exists(os.path.join(segments_info, str(i + 1)))):
                os.mkdir(os.path.join(segments_info, str(i + 1)))
                cv2.imwrite(
                    os.path.join(segments_info, str(i + 1), str(i + 1) + ".jpg"), temp
                )
            self.segment_path.append(
                os.path.join(segments_info, str(i + 1), str(i + 1) + ".jpg")
            )
        if frame_longitudinal_precision <= image_per_row:
            image_per_row = frame_longitudinal_precision
        self.slider = create_image_slider_on_ui(
            ui_obj=self,
            db_obj=self.db,
            frame_obj=self.segment_list_slider_frame,
            prefix="segment",
            image_per_row=image_per_row,
        )

    def update_pixel_value(self):

        val = int(self.label_width_p_value.text()) / self.spinBox_pixel_value.value()
        self.label_pixel_value.setText(str(round(val, 1)))

    def create_folder(self):
        """this function used to creat folder for saveing recoeds

        Returns
        -------
        str
            path of folder,that created
        """
        x = datetime.now()
        path_part = x.strftime("%Y-%m-%d-%H-%M-%S")
        path = os.path.join(PATH_DEFECT_SPLIT, path_part)

        if self.create_path == True:

            if not os.path.exists(path):
                os.mkdir(path)
                self.create_path = False
                try:
                    print("Directory '% s' created" % self.path)
                except:
                    print("eror")

            self.create_path = False
            self.path = path

        return self.path

    def set_laser_detector_threshold(self):
        self.laser_detector_threshold = float(self.spinBox_laserDTH_2.value())
        # print(self.laser_detector_threshold)

    def create_slider(self):

        self.slider = create_image_slider_on_ui(
            ui_obj=self,
            db_obj=self.db,
            frame_obj=self.defects_list_slider_frame,
            prefix="defect",
            image_per_row=6,
        )

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        """open/close left menu animation
        Args:
            enable (bool): open/close menu with animation or not
        """
        width = self.menubar_frame.height()
        maxExtend = 60
        standard = 0
        if enable:

            if width == 0:
                widthExtended = maxExtend

            else:

                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.menubar_frame, b"minimumHeight")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

            print("end")

        else:
            if width == 0:
                self.menubar_frame.setMinimumHeight(44)
                self.menubar_frame.setMaximumHeight(44)
            else:
                self.menubar_frame.setMinimumHeight(0)
                self.menubar_frame.setMaximumHeight(0)

        # self.logger.create_new_log(message="Left menu open/close.")

    def mousePressEvent(self, event):
        """
        get mouse event in UI

        Args:
            event (event): left or right click for drag window
        Returns: None
        """
        if event.button() == QtCore.Qt.LeftButton:
            if event.position().y() <= self.menubar_frame.height():
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
        sys.exit()

    def maxmize_minimize(self):
        """Maximize or Minimize window"""
        if self.isMaximized():
            self.frame_80.setFixedHeight(150)
            self.showNormal()
        else:
            self.frame_80.setFixedHeight(260)

            self.showMaximized()

    def set_warning(self, label_name, text, level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        # print('set_warning')
        if text != None:

            if level == 1:
                label_name.setText(" " + text + " ")
                label_name.setStyleSheet(
                    # "color : #20a740"
                    "background-color:#3D8361;color : #20a740;border-radius:2px;color:white"
                )

            if level == 2:
                label_name.setText(" Warning: " + text)
                label_name.setStyleSheet(
                    # "color : #FDFFA9"
                    "background-color:#3D8361;color : #FDFFA9;border-radius:2px;color:black"
                )

            if level >= 3:
                label_name.setText(" ERROR : " + text)
                label_name.setStyleSheet(
                    # "color : #D9534F"
                    "background-color:#3D8361;color : #D9534F;border-radius:2px;color:black"
                )
            QTimer.singleShot(2000, lambda: self.set_warning(label_name, None))
            # threading.Timer(2, self.set_warning, args=(None, name)).start()

        else:
            label_name.setText("")
            label_name.setStyleSheet("background-color: #3D8361;")

    def set_image_label(self, label_name, img):
        """set imnage in input label

        Parameters
        ----------
        label_name :label OBJ???
            object of label that ,you wnat to set image on it
        img : np.ndarray
            the image that you wnat to set it on label
        """

        img = img.astype(np.uint8)
        if len(img.shape) != 3:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(
            img.data, w, h, bytes_per_line, sQImage.Format_RGB888
        )
        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def camera_loading(self):
        self.collector = Collector(serial_number="24350354", list_devices_mode=True)
        self.serial_list = self.collector.serialnumber()
        self.serial_number_combo.addItems(self.serial_list)

        if self.serial_list != []:

            self.camera_setting()
            self.set_warning(
                label_name=self.msg_label,
                text="Camera Connected Succussfully",
            )
            return True

        else:
            self.set_warning(
                label_name=self.msg_label,
                text="NO CAMERAS CONNECTS AVALABLE WITH,STANDAED PROTOCOL",
            )
            return False

    def laod_camera_parms(self):

        parms = self.db.load_parms("cameras")

        # serial_number = self.serial_number_combo.currentText()
        self.expo_spinbox.setValue(int(parms["exposure"]))
        self.gain_spinbox.setValue(parms["gain"])
        self.width_spinbox.setValue(parms["width"])
        self.label_width_p_value.setText(str(parms["width"]))
        self.height_spinbox.setValue(parms["height"])
        self.offsetx_spinbox.setValue(parms["offset_x"])
        self.offsety_spinbox.setValue(parms["offset_y"])
        # self.trigger_combo.currentText(parms[''])
        # self.maxbuffer_spinbox.setValue(parms[''])
        self.packetdelay_spinbox.setValue(parms["inter_packet_delay"])
        self.packetsize_spinbox.setValue(parms["packet_size"])
        self.transmissiondelay_spinbox.setValue(parms["frame_tran_delay"])

    def pre_load_camera_setting(self):
        serial_number = self.serial_number_combo.currentText()
        exposure = int(self.expo_spinbox.value())
        gain = int(self.gain_spinbox.value())
        width = int(self.width_spinbox.value())
        height = int(self.height_spinbox.value())
        offsetx = int(self.offsetx_spinbox.value())
        offsrty = int(self.offsety_spinbox.value())
        trigger = self.trigger_combo.currentText()
        max_buffer = int(self.maxbuffer_spinbox.value())
        delay_packet = int(self.packetdelay_spinbox.value())
        packet_size = int(self.packetsize_spinbox.value())
        frame_transmission_delay = int(self.transmissiondelay_spinbox.value())
        try:
            if self.camera and self.camera.camera.IsGrabbing():
                self.camera.stop_grabbing()
        except:
            pass

        # try:

        # except:
        #     pass

        #   update_database
        parms = {
            "gain": gain,
            "exposure": exposure,
            "inter_packet_delay": delay_packet,
            "width": width,
            "height": height,
            "packet_size": packet_size,
            "frame_tran_delay": frame_transmission_delay,
            "sn": serial_number,
            "offset_x": offsetx,
            "offset_y": offsrty,
        }
        self.db.update_camera_parms(table_name="cameras", id_number=0, parms=parms)

    def camera_setting(self):
        serial_number = self.serial_number_combo.currentText()
        exposure = int(self.expo_spinbox.value())
        gain = int(self.gain_spinbox.value())
        width = int(self.width_spinbox.value())
        height = int(self.height_spinbox.value())
        offsetx = int(self.offsetx_spinbox.value())
        offsrty = int(self.offsety_spinbox.value())
        trigger = self.trigger_combo.currentText()
        max_buffer = int(self.maxbuffer_spinbox.value())
        delay_packet = int(self.packetdelay_spinbox.value())
        packet_size = int(self.packetsize_spinbox.value())
        frame_transmission_delay = int(self.transmissiondelay_spinbox.value())
        try:
            if self.camera and self.camera.camera.IsGrabbing():
                self.camera.stop_grabbing()
        except:
            pass
        self.camera = Collector(
            serial_number=serial_number,
            gain=gain,
            exposure=exposure,
            max_buffer=max_buffer,
            trigger=trigger,
            delay_packet=delay_packet,
            packet_size=packet_size,
            frame_transmission_delay=frame_transmission_delay,
            width=width,
            height=height,
            offet_x=offsetx,
            offset_y=offsrty,
            manual=False,
            list_devices_mode=False,
        )
        # try:

        # except:
        #     pass

        #   update_database
        parms = {
            "gain": gain,
            "exposure": exposure,
            "inter_packet_delay": delay_packet,
            "width": width,
            "height": height,
            "packet_size": packet_size,
            "frame_tran_delay": frame_transmission_delay,
            "sn": serial_number,
            "offset_x": offsetx,
            "offset_y": offsrty,
        }
        self.db.update_camera_parms(table_name="cameras", id_number=0, parms=parms)

        # self.camera.start_grabbing()

    def set_live_image(self):

        try:
            if GET_LIVE_PICTURE:
                status, img = self.camera.getPictures()
            else:
                status = True
                if self.image_index == len(self.temp_image_folder):
                    self.image_index = 0

                img = cv2.imread(
                    os.path.join(
                        self.image_path, self.temp_image_folder[self.image_index]
                    )
                )
                self.image_index += 1

            if status:
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                laser_mask = self.profile.laser_detetctor(
                    gray_img, self.laser_detector_threshold
                )
                pts = self.profile.extract_points_mean(laser_mask)
                mean_img = self.profile.pts2img(pts, laser_mask.shape)

                self.set_image_label(
                    self.LBL_live_camera_for_setting_image_quality, img
                )
                self.set_image_label(self.LBL_area_laser_detected_2, laser_mask)
                self.set_image_label(self.LBL_line_laser_detected_2, mean_img)
                self.sett_cam_fps.setText(
                    str(round(self.camera.camera.ResultingFrameRate.GetValue(), 2))
                )
                h, w, _ = img.shape
                self.sett_cam_size.setText(str(h) + " x " + str(w))
            else:
                self.eror_img += 1
                self.sett_cam_errors.setText(str(self.eror_img))
                self.sett_cam_size.setText("-")

        except:
            self.set_image_label(
                self.LBL_live_camera_for_setting_image_quality, NO_IMAGE
            )
            self.set_image_label(self.LBL_area_laser_detected_2, NO_IMAGE)
            self.set_image_label(self.LBL_line_laser_detected_2, NO_IMAGE)

    def mask_gen(self, frame):
        """algo function,indicate err on belt

        Parameters
        ----------
        frame : np.ndarray
            frame .......

        Returns
        -------
        _type_
            _description_
        """

        # indicate laser zone of image
        laser_mask = self.profile.laser_detetctor(
            frame,
            thresh=self.laser_detector_threshold,
            medianBlur_kernel=self.laser_detector_medianBlur_kernel,
        )

        if DEBUG_UI:
            cv2.imshow("laser_mask", laser_mask)

        # get x-y-z cordinations from laser mask
        pts = self.profile.extract_points_mean(laser_mask)
        self.profile.save_points(pts)
        xyz_current = self.profile.get_cloudPoints_current()

        # ___________________________ extracts each Z pivots_______________________________#
        row = np.zeros(WIDTH, dtype=np.uint32)
        row[xyz_current[:, 0]] = xyz_current[:, 2]
        # z-pivot capture
        z_row_array = np.array((row), dtype=np.uint32)
        self.z_heatmap.optimiezedAdd_32_bits(z_row_array, colormap=None)
        z_pivots = self.z_heatmap.getmatrix_32_bit(self.rate)
        # z_pivots_h = self.z_heatmap.getmatrix_32_bit_h(self.rate)
        # self.set_image_label(self.LBL_live_camera_2, z_pivots_h)
        # self.set_image_label(self.LBL_live_camera, z_pivots)
        # if DEBUG_UI:
        # cv2.imshow("z pivots", z_pivots)
        # _____________________________
        # self.z_heatmap.optimiezedAdd_32_bits(mask, colormap=None)
        # x = self.z_heatmap.getmatrix_32_bit_h(self.rate)
        # _____________________________

        # detecting err algo
        row_temp = np.ones(WIDTH) * 255
        # capture first base line for calculating mean base
        if self.num_frames < mean_index:
            temp = np.array((255 * (row / row.max())), dtype=np.uint8)
            self.mask.optimiezedAdd(temp, colormap=None)
            stack_row[self.num_frames, :] = row
        else:
            # now has base mean
            base = np.average(stack_row, axis=0, weights=weights)
            row_temp[np.where((row - base) > limited_deviation_from_base)] = 0
            mask = np.array((255 * row_temp / row_temp.max()), dtype=np.uint8)

            # make defect zone more obvious
            locs = np.where(mask < 10)[0]
            for k, _ in enumerate(locs[:-2]):
                if locs[k + 1] - locs[k] < 170:
                    mask[locs[k] : locs[k + 1]] = 0
            self.mask.optimiezedAdd(mask, colormap=None)

            # update stack_row for calculating new base
            stack_row[0 : mean_index - 1, :] = stack_row[1:mean_index, :]
            stack_row[mean_index - 1, :] = row

        # get final image
        out_mask = self.mask.getImage(int(SHOW_BOUND / self.rate), self.rate)
        # out_mask_h = self.mask.get_hImage(int(SHOW_BOUND / self.rate), self.rate)
        out_mask = cv2.medianBlur(out_mask, final_output_medianBlur_kernel)
        _, dst = cv2.threshold(
            out_mask, final_output_threshold_kernel, 255, cv2.THRESH_BINARY_INV
        )
        if DEBUG_UI:
            cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
            cv2.imshow("dst", dst)
            cv2.waitKey(1)
        return dst, z_pivots

    def surface_scanning(self):
        """this function get live frame ,and pass the frame to the algo for processing"""
        try:
            if GET_LIVE_PICTURE:
                # get live picture from camera(truly)
                status, frame = self.camera.getPictures()
            else:
                # get live picture artificially
                status = True
                if self.image_index == len(self.temp_image_folder):
                    self.image_index = 0

                frame = cv2.imread(
                    os.path.join(
                        self.image_path, self.temp_image_folder[self.image_index]
                    )
                )

                self.image_index += 1

            if DEBUG_UI:
                cv2.imshow("faaaaaaaaaaaaaaaaaaaaaaaaa", frame)
                cv2.waitKey(1)

            self.num_frames += 1
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        except:
            self.timer_live_detect.stop()
            status = False
            print("in exception loop!!!!!! ,there is problem for getting picture")
        if status:
            self.slider_management()
            mask, z_mask = self.mask_gen(frame)
            shape = z_mask.shape
            if shape[0] <= SHOW_BOUND:
                self.last_point = shape[0]
            else:
                self.first_point += self.update_step
                self.last_point += self.update_step
            self.current_segment = np.ones((SHOW_BOUND, WIDTH, 3), np.uint8) * 255
            self.display_segment_schematic(
                mask, z_mask[self.first_point : self.last_point]
            )
            if self.num_frames == self.frame_pre_segment:
                self.segment_detail_list[self.segment_index] = self.current_segment
                self.segment_annotation.write(
                    os.path.join(
                        segments_info,
                        str(self.segment_index),
                        str(self.segment_index) + ".json",
                    )
                )
                temp = cv2.cvtColor(self.current_segment, cv2.COLOR_BGR2RGB)
                cv2.imwrite(
                    os.path.join(
                        segments_info,
                        str(self.segment_index),
                        str(self.segment_index) + ".png",
                    ),
                    temp,
                )

            if self.segment_index != ((self.num_frames - 1) // self.frame_pre_segment):
                self.segment_index = (self.num_frames - 1) // self.frame_pre_segment
                self.segment_detail_list[self.segment_index] = self.current_segment
                self.segment_annotation.write(
                    os.path.join(
                        segments_info,
                        str(self.segment_index),
                        str(self.segment_index) + ".json",
                    )
                )
                temp = cv2.cvtColor(self.current_segment, cv2.COLOR_BGR2RGB)
                cv2.imwrite(
                    os.path.join(
                        segments_info,
                        str(self.segment_index),
                        str(self.segment_index) + ".png",
                    ),
                    temp,
                )

            if DEBUG_UI:
                cv2.namedWindow("aaaaaaaaaaaaaa", cv2.WINDOW_NORMAL)
                cv2.imshow("aaaaaaaaaaaaaa", mask)

            if self.num_frames >= self.frame_per_roll:
                stack_row = np.zeros((mean_index, WIDTH))
                self.num_frames = 0
                self.z_heatmap.reset_32bit_part()
                self.mask.reset()
                self.last_point = self.update_step
                self.first_point = 0
                self.segment_index = 0

                self.create_path = True
                num_prev = len(self.segment_path) // self.image_pre_row
                for _ in range(num_prev):
                    update_imagesslider_on_ui(self, "prev")
                if len(self.segment_path) % self.image_pre_row != 0:
                    update_imagesslider_on_ui(self, "prev")
                self.index_slider = 0
                self.index_of_scanning_segment = -1

            self.set_image_label(self.LBL_live_camera, self.current_segment)

    def display_segment_schematic(self, mask, z_value):

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        details = {}
        details["defects_boundbox_list"] = []
        details["defects_position_list"] = []
        details["defects_depth_list"] = []
        details["defects_type_list"] = []
        details["defects_area_list"] = []
        # details["defects_xpixel_list"] = []
        # details["defects_ypixel_list"] = []

        for _, cnt in enumerate(contours):
            (
                check_flag,
                area,
                perimeter,
                thickness,
                Type,
                err_cordinats,
            ) = self.defects_features_extractor(cnt)
            if check_flag:
                x, y, w, h = err_cordinats
                shape = mask.shape
                raw_canvas = np.zeros(shape, np.uint8)
                x1, y1 = average_moveing_contour(
                    cnt=cnt,
                )
                raw_canvas[y1, x1] = 255
                cv2.line(raw_canvas, (x1[0], y1[0]), (x1[-1], y1[-1]), 255, thickness=1)
                single_contours, _ = cv2.findContours(
                    raw_canvas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
                )
                cv2.drawContours(raw_canvas, single_contours, -1, 255, -1)
                locs = np.where(raw_canvas == 255)
                detph = np.mean(z_value[locs[0], locs[1]], axis=0)
                if detph < 180:
                    color = (255, 0, 0)
                    type_ = "jerrrrrrr"
                elif detph < 220:
                    color = (235, 134, 13)
                    type_ = "paregi"
                else:
                    color = (229, 236, 9)
                    type_ = "farsayesh"

                # details["defects_ypixel_list"].append(locs[0].tolist())
                # details["defects_xpixel_list"].append(locs[1].tolist())
                details["defects_boundbox_list"].append(err_cordinats)
                details["defects_depth_list"].append(detph)
                details["defects_type_list"].append(type_)
                details["defects_area_list"].append(area)
                details["defects_position_list"].append((x + (w // 2), y + (h // 2)))

                self.current_segment[locs[0], locs[1], 0] = z_value[locs[0], locs[1]]
                self.current_segment[locs[0], locs[1], 1] = z_value[locs[0], locs[1]]
                self.current_segment[locs[0], locs[1], 2] = z_value[locs[0], locs[1]]

                self.current_segment = cv2.rectangle(
                    self.current_segment, (x, y), (x + w, y + h), color, 3
                )
        self.segment_annotation.set_all(details=details)
        # self.set_image_label(self.LBL_live_camera, mask)
        # self.set_image_label(self.LBL_live_camera, z_value)

    # ______________________________________________________
    def save_segment_schematic(self):

        if self.num_frames == self.frame_pre_segment:
            temp = cv2.cvtColor(self.current_segment, cv2.COLOR_BGR2RGB)
            cv2.imwrite(
                os.path.join(
                    segments_info,
                    str(self.segment_index),
                    str(self.segment_index) + "_.png",
                ),
                temp,
            )

        if self.segment_index != ((self.num_frames - 1) // self.frame_pre_segment):
            temp = cv2.cvtColor(self.current_segment, cv2.COLOR_BGR2RGB)
            cv2.imwrite(
                os.path.join(
                    segments_info,
                    str(self.segment_index),
                    str(self.segment_index) + "_.png",
                ),
                temp,
            )

    # _____________________________________________________should check
    def write_defect_images(self):
        if len(self.save_defect_images_list) > 0:
            mask = self.save_defect_images_list.pop(0)
            file_name = self.save_defect_images_list_name_file.pop(0)
            json = self.json_list.pop(0)
            path = os.path.join(self.path, file_name)
            if WRITE:
                cv2.imwrite(path, mask)
                self.json_obj.set_all(json)
                self.json_obj.write(str(path).replace("jpg", "json"))
                self.defect_image_list.append_mylist(path, self.name)

    def UpDate_Slider(self):
        if len(self.save_defect_images_list) > 0:
            update_defect_images_on_ui(ui_obj=self, prevornext="next")
            (self.current_image_list) = self.defect_image_list.get_n_current(
                name="defect", get_annots=False
            )

    def update_slider_2(self):
        res = set_image_to_ui_slider_full_path(
            ui_obj=self,
            image_path_list=self.current_image_list,
            annot_path_list=[],
            prefix="defect",
            image_per_row=6,
        )

    # _____________________________________________________

    def defects_features_extractor(self, cnt):
        """this function get contour image of detected err,and extract the features of it

        Parameters
        ----------
        cnt : np.ndarray
            numpy array of contour pixel

        Returns
        -------
        _type_
            _description_
        """
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        thickness = 1
        Type = "defect"

        if area > 5000 or perimeter > 5000:
            return True, area, perimeter, thickness, Type, (x, y, w, h)
        return False, area, perimeter, thickness, Type, (x, y, w, h)

    def slider_management(self):

        last_index = self.index_of_scanning_segment
        temp = (self.num_frames - 1) // self.frame_pre_segment
        self.index_of_scanning_segment = temp % self.image_pre_row
        if self.index_slider != (temp // self.image_pre_row):
            update_imagesslider_on_ui(self, "next")
        if last_index != self.index_of_scanning_segment:
            for j in range(self.image_pre_row):
                set_label_style(self, j, "segment", "normal")
            set_label_style(self, self.index_of_scanning_segment, "segment", "scanning")
        self.index_slider = temp // self.image_pre_row

    def stop_live(self):
        if not self.live_flag:
            self.timer_live.stop()
            self.set_live_flag = False
            print("stop live")

    def start_live(self):
        if not self.live_flag:
            self.timer_live.start()
            self.set_live_flag = True
            print("start live")

    def stop_detect(self):
        if self.detect_flag:
            self.timer_live_detect.stop()
            # self.timer_save_segment_schematic.stop()
            # self.timer_save_defect_images.stop()
            # self.defect_slider_show.stop()
            # self.defect_slider_show_2.stop()
            self.detect_flag = False
            print("stop detect")

            self.set_warning(
                label_name=self.msg_label,
                text="Stop Detection",
                level=1,
            )

    def start_detect(self):
        if not self.detect_flag:
            # self.create_folder()
            self.timer_live_detect.start()
            # self.timer_save_segment_schematic.start()
            if WRITE:
                self.timer_save_defect_images.start(500)
                self.defect_slider_show.start(500)
                # self.defect_slider_show_2.start(500)
                self.detect_flag = True
                print("start detect")
                self.set_warning(
                    label_name=self.msg_label,
                    text="Start Detection",
                    level=1,
                )

    def widget_connector(self):
        self.BTN_camera_setting.clicked.connect(self.load_page)
        self.BTN_dashboard.clicked.connect(self.load_page)
        self.BTN_general_setting.clicked.connect(self.load_page)
        self.BTN_history.clicked.connect(self.load_page)

        self.BTN_camera_connect.clicked.connect(self.start_live)
        self.BTN_camera_disconnect.clicked.connect(self.stop_live)

        self.BTN_camera_setting_apply.clicked.connect(self.pre_load_camera_setting)
        self.brn_set_calib_parms.clicked.connect(self.set_camera_calibration)

        self.BTN_scane_start.clicked.connect(self.start_detect)
        self.BTN_scan_stop.clicked.connect(self.stop_detect)

        # UI
        self.menu_btn.clicked.connect(lambda: self.toggleMenu(enable=False))

        self.camera_calib_btn.clicked.connect(self.open_close_camera)
        self.camera_live_btn.clicked.connect(self.open_close_camera)

        self.spinBox_laserDTH_2.valueChanged.connect(
            lambda: self.set_laser_detector_threshold()
        )

    def set_camera_calibration(self):

        laser = self.spinBox_laserDTH_2.value()
        mean = self.median_1_spin.value()
        th1 = self.median_2_spin.value()
        th2 = self.threshold_2_spin.value()
        fr = self.spinBox_f_r.value()
        ls = self.spinBox_l_s.value()
        pv = self.spinBox_pixel_value.value()
        fpv = self.label_pixel_value.text()

        parms = {
            "laser": laser,
            "mean": mean,
            "th1": th1,
            "th2": th2,
            "frame_rate": fr,
            "line_speed": ls,
            "pixel_value": pv,
            "final_pixel_value": fpv,
        }
        self.db.update_camera_parms(table_name="calibration", id_number=0, parms=parms)

    def load_camera_calibration(self):

        parms = self.db.load_parms("calibration")

        self.spinBox_laserDTH_2.setValue(parms["laser"])
        self.median_1_spin.setValue(parms["mean"])
        self.median_2_spin.setValue(parms["th1"])
        self.threshold_2_spin.setValue(parms["th2"])
        self.spinBox_f_r.setValue(parms["frame_rate"])
        self.spinBox_l_s.setValue(parms["line_speed"])
        self.spinBox_pixel_value.setValue(parms["pixel_value"])
        self.label_pixel_value.setText(str(parms["final_pixel_value"]))

    def open_close_camera(self):
        """this function used for connecting sofware to camera"""

        if self.camera == None:
            self.camera = 1
            self.camera_loading()
            try:
                self.camera.start_grabbing()
                if self.camera.camera.IsGrabbing():
                    self.set_btn_image(self.camera_calib_btn, image_open_camera)
                    self.set_btn_image(self.camera_live_btn, image_open_camera)
                    self.enable_disable_camera_btns(True)
                    self.set_image_label(self.LBL_live_camera_2, self.current_segment)
                else:
                    self.set_warning(
                        label_name=self.msg_label,
                        text="cannot connect to camera   -----------------",
                        level=2,
                    )
                    self.eror_img = 0
                    self.sett_cam_size.setText("-")
                    self.sett_cam_fps.setText("-")
            except:

                # self.set_btn_image(self.camera_calib_btn, image_close_camera)
                # self.set_btn_image(self.camera_live_btn, image_close_camera)
                # self.enable_disable_camera_btns(False)
                self.set_warning(
                    label_name=self.msg_label,
                    text="cannot connect to camera",
                    level=2,
                )
                # 280533219
                self.eror_img = 0
                self.sett_cam_size.setText("-")
                self.sett_cam_fps.setText("-")

        else:
            self.stop_detect()
            self.stop_live()
            self.camera = None
            self.set_btn_image(self.camera_calib_btn, image_close_camera)
            self.set_btn_image(self.camera_live_btn, image_close_camera)
            self.enable_disable_camera_btns(False)
            self.eror_img = 0
            self.sett_cam_size.setText("-")
            self.sett_cam_fps.setText("-")
            self.set_warning(
                label_name=self.msg_label,
                text="Camera Disconnected Succussfully",
                level=2,
            )

    def enable_disable_camera_btns(self, mode):

        btns = [
            self.BTN_camera_connect,
            self.BTN_camera_disconnect,
            self.BTN_scane_start,
            self.BTN_scan_stop,
        ]
        for btn in btns:
            btn.setEnabled(mode)

    def set_btn_image(self, btn_name, path):

        btn_name.setIcon(QIcon(path))

    def load_page(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "BTN_camera_setting":
            self.stackedWidget.setCurrentWidget(self.camera_settings)
        elif btnName == "BTN_dashboard":
            self.stackedWidget.setCurrentWidget(self.Dashboard)
        elif btnName == "BTN_calibration_setting":
            self.stackedWidget.setCurrentWidget(self.calibration_settings)
        elif btnName == "BTN_general_setting":
            self.stackedWidget.setCurrentWidget(self.general_setting)
        elif btnName == "BTN_history":
            self.stackedWidget.setCurrentWidget(self.history)

    def load_history(self):

        self.create_folders()

    def create_folders(self):
        self.clearLayout(self.verticalLayout_20)
        self.folders = []
        for it in os.scandir(PATH_DEFECT_SPLIT):
            if it.is_dir():
                print(it.path)
                self.folders.append(it)
        for _, button_number in enumerate(self.folders):
            button = QPushButton()
            bt = str(button_number).split("'")[1]
            button.setText(bt)
            button.setObjectName("%d" % _)
            button.clicked.connect(self.click)
            button.setFont(QFont("Sanserif", 15))
            # button.setIcon(QIcon("G:\work/abrarvan\images/folder-icon.png"))
            button.setIconSize(QSize(10, 10))
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet(
                "QPushButton { background-color: rgb(0, 0, 0);color : rgb(255,255,255)}"
            )
            self.verticalLayout_20.addWidget(button)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def click(self):
        self.clearLayout(self.gridLayout)
        btn = self.sender()
        btnName = btn.objectName()
        print(btnName)

        path_ = os.path.join(self.folders[int(btnName)])
        print("path_  sssssssssss", path_)
        self.lineEdit_load_path.setText(path_)
        path = os.listdir(path_)
        self.img_path = []
        for it in path:
            if it[-3:] == "jpg":
                # print(it)
                self.img_path.append(it)
        print(self.img_path)
        for _, i in enumerate(self.img_path):

            label = QLabel()
            label.setObjectName("label_{}_{}".format(path_, i))
            # label.mousePressEvent = self.show_image()
            # label.clicked.connect(self.show_image)
            label.setFont(QFont("Sanserif", 15))
            img_path = os.path.join(path_, i)
            # self.set_btn_image(label, img_path)
            # label.setIconSize(QSize(200,200))
            self.set_image_label(label, cv2.imread(img_path))
            label.setCursor(Qt.PointingHandCursor)
            self.gridLayout.addWidget(label)

    def show_image(self, e):

        # self.clearLayout(self.gridLayout)
        btn = self.sender()
        btnName = btn.objectName()
        print(btnName)

    def set_btn_image(self, btn_name, path):
        btn_name.setIcon(QIcon(path))


if __name__ == "__main__":
    app = QApplication()
    app.setAttribute(sQtCore.Qt.AA_EnableHighDpiScaling)
    win = UI_main_window()
    win.show()
    sys.exit(app.exec())
