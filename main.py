import sys
import cv2,random
import numpy as np
import threading,datetime


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


MIN_DEFECT_AREA = 0
MIN_DEFECT_WIDTH = 0
MIN_DEFECT_HEIGHT = 0


ui, _ = loadUiType("UI/main_UI.ui")
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


DEBUG_UI = False
WRITE = True








mean_index = 10

weights = np.zeros((mean_index, WIDTH))
weights[0 : mean_index // 3, :] = 1
weights[mean_index // 3 : 2 * (mean_index // 3)] = 10
weights[2 * (mean_index // 3), :] = 20

row_5 = np.zeros((mean_index, WIDTH))


def average_moveing_contour(cnt, k_pre_points, mask_raw):

    for i, _ in enumerate(cnt):
        # if cnt[i : i + k_pre_points, 0, 0].shape[0] == k_pre_points:
        x_ = cnt[i : i + k_pre_points, 0, 0].mean()
        y_ = cnt[i : i + k_pre_points, 0, 1].mean()
        # else:
        #     x_ = cnt[i, 0, 0]
        #     y_ = cnt[i, 0, 1]
        mask_raw[int(y_), int(x_)] = 255

    return mask_raw







class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    x = 0
    _i_ = -1

    image_path = 'D:/Newfolder3'


    temp_image_folder = os.listdir(image_path)

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
        self.laser_detector_threshold = 12.56
        self.norm_level_value = 210
        self.threshold1 = 0
        self.threshold2 = 200
        ################
        self.create_path = True
        if not os.path.exists(PATH_DEFECT_SPLIT):
            os.mkdir(PATH_DEFECT_SPLIT)
        # popup windwo
        self.popup_window_obj = UI_popup_window()
        # self.popup_window_obj.show()
        

        #json object

        self.json_obj = Annotation()


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

        # self.LBL_live_camera.setPixmap(self.pixmap)
        # self.LBL_live_camera_for_setting_image_quality.setPixmap(self.pixmap)

        # speed parameter###################################################
        self.pixel_size = 0.00647  # cm
        self.Vpps = 120 / 13.5  # pixel per secend
        self.fps = 47.7
        self.tpf = 1 / 47.7  # time per frame =1/fps
        self.rate = 30  # int(v*tpf)#pixel per frame
        self.speed_rate = 100 / (self.rate * 14 * self.fps)  # cm per frame
        self.belt_height = 10000
        ###################################################################
        self.num_frames = 0
        self.process_flag = False
        self.frame_per_roll = 200

        ###################################################################

        # camera setting##############################
        self.laod_camera_parms()
        self.load_camera_calibration()

        #############################################
        self.widget_connector()
        self.profile = ProfileMeter()
        self.mask = heatmap(WIDTH, chanel=1)

        self.set_image_label(self.LBL_live_camera, NO_IMAGE)

        self._old_pos = None
        self.pos_ = self.pos()

        # camera connection
        self.live_flag = False
        self.detect_flag = False

        self.timer_live = QTimer(self)
        self.timer_live.timeout.connect(self.set_live_image)

        self.timer_live_detect = QTimer(self)
        self.timer_live_detect.timeout.connect(self.surface_scanning)

        self.save_defect_images_list_name_file = []
        self.save_defect_images_list = []
        self.timer_save_defect_images = QTimer(self)
        self.timer_save_defect_images.timeout.connect(self.write_defect_images)

        self.defect_slider_show = QTimer(self)
        self.defect_slider_show.timeout.connect(self.UpDate_Slider)
        self.current_image_list = []
        self.json_list=[]

        # self.parent_path =os.path.join(PATH_DEFECT_SPLIT,self.create_folder())

        # self.defect_slider_show_2 = QTimer(self)
        # self.defect_slider_show_2.timeout.connect(self.update_slider_2)
        # self.current_image_list = []

        # self.timer_live.start(200)

        # self.defect_image_list = moveOnImagrList(
        #     sub_directory="slider_images/", step=6
        # )
        # name = 'slider_images'
        # self.defect_image_list.add(
        #     mylist=self.defect_image_list,
        #     name=name,
        # )
        # # create next and prev funcs
        # --------------------------slider image

        self.defect_split_path = []
        self.name = "defect"
        # for img in os.listdir(PATH_DEFECT_SPLIT):                     # enable if you want show last iamges in init
        #     if img[-3:]=='jpg':
        #         self.defect_split_path.append(os.path.join(PATH_DEFECT_SPLIT, img))

        self.defect_image_list = moveOnImagrList(
            sub_directory=PATH_DEFECT_SPLIT,
        )
        self.defect_image_list.add(self.defect_split_path, self.name)
        self.defect_image_list_next_func = self.defect_image_list.build_next_func(
            name=self.name
        )
        self.defect_image_list_prev_func = self.defect_image_list.build_prev_func(
            name=self.name
        )
        self.create_slider()
        update_defect_images_on_ui(ui_obj=self)
        # -----------------------------------

        self.defects_prev_btn.clicked.connect(
            partial(lambda: update_defect_images_on_ui(ui_obj=self, prevornext="prev"))
        )
        self.defects_next_btn.clicked.connect(
            partial(lambda: update_defect_images_on_ui(ui_obj=self, prevornext="next"))
        )


        self.width_spinbox.valueChanged.connect(self.update_pixel_value)
        self.spinBox_pixel_value.valueChanged.connect(self.update_pixel_value)

        self.BTN_history.clicked.connect(self.load_history)




    def update_pixel_value(self):
        
        
        val = int(self.label_width_p_value.text())/self.spinBox_pixel_value.value() 
        self.label_pixel_value.setText(str(round(val,1)))


    def create_folder(self):
        from datetime import datetime
        x =datetime.now()
        path_part=x.strftime("%Y-%m-%d-%H-%M-%S")

        path = os.path.join(PATH_DEFECT_SPLIT, path_part)

        print('first_path',path)

        if self.create_path==True:
            print('create_path')
            if not os.path.exists(path):
                
                os.mkdir(path)
                self.path=path
                self.create_path=False
                try:
                    
                    print("Directory '% s' created" % self.path)
                except:
                    print('eror')
                    # notif.setText('Eror : {}/cam_{}_*.tiff '.format(directory,cam))

            elif os.path.exists(path):
                
                # directory = str(slab_id) +'_'+ '{}'.format(x)
                # print(directory)
                # path = os.path.join(self.parent_dir, directory)
                # print('path',path)
                # os.mkdir(path)

                self.create_path=False

                # self.path=path

        return self.path


    def set_laser_detector_threshold(self):
        self.laser_detector_threshold = float(self.spinBox_laserDTH_2.value())
        print(self.laser_detector_threshold)

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

            self.showNormal()
        else:
            self.showMaximized()

    def set_warning(self, label_name, text, level=1):
        """Show warning with time delay 2 second , all labels for show warning has been set here"""

        # print('set_warning')
        if text != None:

            if level == 1:
                label_name.setText(" " + text + " ")
                label_name.setStyleSheet(
                    "background-color:#20a740;border-radius:2px;color:white"
                )

            if level == 2:
                label_name.setText(" Warning: " + text)
                label_name.setStyleSheet(
                    "background-color:#FDFFA9;border-radius:2px;color:black"
                )

            if level >= 3:
                label_name.setText(" ERROR : " + text)
                label_name.setStyleSheet(
                    "background-color:#D9534F;border-radius:2px;color:black"
                )
            QTimer.singleShot(2000, lambda: self.set_warning(label_name, None))
            # threading.Timer(2, self.set_warning, args=(None, name)).start()

        else:
            label_name.setText("")
            label_name.setStyleSheet("")

    def set_image_label(self, label_name, img):
        """set imnage in input label"""
        # if len(img.shape) != 3:
        #     img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        try:
            h, w, ch = img.shape
        except:
            h, w = img.shape
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            ch=3
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
            manual=True,
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

        # try:
        status, img = self.camera.getPictures()
        # status = True
        # if self._i_ == len(self.temp_image_folder) - 1:
        #     self._i_ = -1
        # self._i_ += 1

        # img = cv2.imread(os.path.join(self.image_path, self.temp_image_folder[self._i_]))
        if status:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            laser_mask = self.profile.laser_detetctor(
                gray_img, self.laser_detector_threshold
            )
            pts = self.profile.extract_points_mean(laser_mask)
            mean_img = self.profile.pts2img(pts, laser_mask.shape)

            self.set_image_label(self.LBL_live_camera_for_setting_image_quality, img)
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

    # except:
    #     self.set_image_label(
    #         self.LBL_live_camera_for_setting_image_quality, NO_IMAGE
    #     )
    #     self.set_image_label(self.LBL_area_laser_detected_2, NO_IMAGE)
    #     self.set_image_label(self.LBL_line_laser_detected_2, NO_IMAGE)

    def mask_gen(self, frame):
        # return frame
        laser_mask = self.profile.laser_detetctor(
            frame, thresh=1
        )
        
        # if self.checkBox_median_1.isChecked():
        laser_mask = cv2.medianBlur(laser_mask, 5)
        if DEBUG_UI:
            cv2.imshow('laser_mask',laser_mask)

        # return laser_mask

        pts = self.profile.extract_points_mean(laser_mask)
        self.profile.save_points(pts)
        xyz_current = self.profile.get_cloudPoints_current()

        row = np.zeros(WIDTH)
        row[xyz_current[:, 0]] = xyz_current[:, 2]



        j=self.num_frames
        
        row2 = row.copy()
        row_temp = np.ones(WIDTH) * 255

        if j < mean_index:
            row1 = row.copy()
            xxx = np.array((255 * row1 / row1.max()), dtype=np.uint8)
            self.mask.optimiezedAdd(xxx, colormap=None)
            row_5[j, :] = row
        else:
            # x = np.mean(row_5, axis=0)

            x = np.average(row_5, axis=0, weights=weights)
            row_temp[np.where((row2 - x) > 30)] = 0
            xxx = np.array((255 * row_temp / row_temp.max()), dtype=np.uint8)

            locs = np.where(xxx < 10)[0]
            for k, _ in enumerate(locs[:-2]):
                if locs[k + 1] - locs[k] < 150:
                    xxx[locs[k] : locs[k + 1]] = 0

            self.mask.optimiezedAdd(xxx, colormap=None)

            row_5[0 : mean_index - 1, :] = row_5[1:mean_index, :]
            row_5[mean_index - 1, :] = row2


        out_mask = self.mask.getImage(int(SHOW_BOUND / self.rate), self.rate)
        out_mask = np.array(out_mask)
        # return out_mask
        # if self.checkBox_th_2.isChecked():
            # _, out_mask = cv2.threshold(out_mask, self.threshold_2_spin.value(), 255, cv2.THRESH_BINARY_INV)
        _, dst = cv2.threshold(out_mask, 254, 255, cv2.THRESH_BINARY_INV)
        # if self.checkBox_median_2.isChecked():
        #     out_mask = cv2.medianBlur(out_mask, self.median_2_spin.value())
        # return dst
        if DEBUG_UI: 
            cv2.namedWindow("dst", cv2.WINDOW_NORMAL) 
            cv2.imshow('dst',dst)
            cv2.waitKey(1)
        # return dst
        if self.num_frames % int(SHOW_BOUND / self.rate) == 0:
            self.process_flag = True
        else:
            self.process_flag = False
        #temp=dst.copy()        
        if self.process_flag:
            contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            # dst = cv2.cvtColor(out_mask, cv2.COLOR_GRAY2BGR)
            color = 255

            # cv2.imshow('a',dst)
            # cv2.waitKey(0)

            # type_ = f"defect"
            temp = np.zeros(dst.shape)
            
            for k,cnt in enumerate(contours):
                x, y, w, h = cv2.boundingRect(cnt)
                area = cv2.contourArea(cnt)
                perimeter = cv2.arcLength(cnt, True)

                if area > 5000 or perimeter > 1000:
                    temp = average_moveing_contour(cnt=cnt, k_pre_points=50, mask_raw=temp)
                    # temp = cv2.dilate(temp, kernel, iterations=1)
                    
                    temp = cv2.rectangle(temp, (x, y), (x + w, y + h), color, 3)
                    area = round(area/(float(self.label_pixel_value.text())), 1)
                    cv2.putText(
                        temp,
                        "Area :{}".format(str(area)),
                        (x, y + 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        255,
                        2,
                    )
                    self.save_defect_images_list.append(temp[y : y + h, x : x + w])
                    self.save_defect_images_list_name_file.append(
                            str(self._i_) + "_" + str(k) + ".jpg"
                        )
                    print(str(self._i_) + "_" + str(k))

                    default_details = {"date":"{}".format(date_module.get_datetime()),"loc": "{}".format(random.randint(5,500)), "area": "{}".format(area), "type": "-", "p": "-", "depth": "-"}
                    self.json_list.append(default_details)
                # self.json_obj.set_all(default_details)
                # self.json_obj.write(str(path).replace('jpg', 'json'))

        else:
            contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            color = 255
            temp = np.zeros(dst.shape)
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                area = cv2.contourArea(cnt)
                perimeter = cv2.arcLength(cnt, True)

                if area > 5000 or perimeter > 1000:
                    temp = average_moveing_contour(cnt=cnt, k_pre_points=10, mask_raw=temp)
                    # temp = cv2.dilate(temp, kernel, iterations=1)
                    temp = cv2.rectangle(temp, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(
                        temp,
                        "Area :{}".format(str(round(area/(float(self.label_pixel_value.text())), 1))),
                        (x, y + 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        255,
                        2,
                    )
        temp = temp.astype('uint8')
        return temp

    def indicate_features_and_emergency_of_defect(self, contours, mask):

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # area = cv2.contourArea(cnt)
            # perimeter = cv2.arcLength(cnt, True)
            # flag, color, type_ = self.contour_filter(
            #     w=w, h=h, area=area, perimeter=perimeter
            # )
            flag = True
            type_ = f"defect"
            color = (255, 0, 0)
            if flag:
                mask[x : x + w, y : y + h] = 0
                mask[x : x + w, y : y + h] = self.average_moveing_contour(
                    cnt=cnt, k_pre_points=2, mask=mask[x : x + w, y : y + h]
                )
                mask = cv2.rectangle(mask, (x, y), (x + w, y + h), color, 3)
                cv2.putText(
                    mask,
                    type_,
                    (x, y + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2,
                )
                self.set_image_label(self.LBL_live_camera, mask)

    def contour_filter(self, w, h, area, perimeter):
        # will be completed
        color = (255, 0, 0)
        type_ = f"defect"
        return True, color, type_

    def average_moveing_contour(self, cnt, k_pre_points, mask):

        for i, _ in enumerate(cnt):
            if cnt[i : i + k_pre_points, 0, 0].shape[0] == k_pre_points:
                x_ = cnt[i : i + k_pre_points, 0, 0].mean()
                y_ = cnt[i : i + k_pre_points, 0, 1].mean()
            else:
                x_ = cnt[i, 0, 0]
                y_ = cnt[i, 0, 1]

            mask[int(y_), int(x_)] = 255

        return mask

    def surface_scanning(self):
        # try:
        # status, frame = self.camera.getPictures()
        # frame_org = frame
        self.num_frames += 1
        # _____________temp_______________________
        status = True
        if self._i_ == len(self.temp_image_folder) - 1:
            self._i_ = -1
        self._i_ += 1
        frame = cv2.imread(os.path.join(self.image_path, self.temp_image_folder[self._i_]))
        frame_org = frame
        if DEBUG_UI:
            cv2.imshow('faaaaaaaaaaaaaaaaaaaaaaaaa',frame)
            cv2.waitKey(1)
        # print(frame.shape,os.path.join(self.image_path, self.temp_image_folder[self._i_]))

        # _____________temp_______________________

        if status:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_org = frame
            mask = self.mask_gen(frame)
             
            if DEBUG_UI:
                cv2.namedWindow("aaaaaaaaaaaaaa", cv2.WINDOW_NORMAL)
                cv2.imshow('aaaaaaaaaaaaaa',mask)

            resized = cv2.resize(
                mask,
                (self.scrollArea.width(), 900),  #this relative to the camera
                interpolation=cv2.INTER_AREA,
            )
            # try:
            self.set_image_label(self.LBL_live_camera, resized)
            # self.set_image_label(self.LBL_line_laser_detected_2, frame_org)
            # except:
            #     pass
            # self.set_image_label(self.LBL_area_laser_detected_2, mask)
            # self.set_image_label(self.LBL_live_camera_for_setting_image_quality, frame_org)


            # cv2.imshow('resized',resized)
            # cv2.imshow('frame_org',frame_org)
            # cv2.waitKey(0)


            # self.indicate_features_and_emergency_of_defect(
            #     contours=contours, mask=mask
            # )
            # ______________mini process____________________________
            if self.num_frames>=200:
                self.create_path=True
                self.create_folder()
                self.num_frames=0
    # except:
    #     pass

    def write_defect_images(self):
        if len(self.save_defect_images_list) > 0:
            mask = self.save_defect_images_list.pop(0)
            file_name = self.save_defect_images_list_name_file.pop(0)
            json = self.json_list.pop(0)
            path = os.path.join(self.path, file_name)
            if WRITE:
                cv2.imwrite(path, mask)
                # cv2.imwrite(path, mask)
                # default_details = {"date":"{}".format(date_module.get_datetime()),"loc": "{}".format(random.randint(5,500)), "area": "{}".format(random.randint(5,500)), "type": "-", "p": "-", "depth": "-"}
                self.json_obj.set_all(json)
                self.json_obj.write(str(path).replace('jpg', 'json'))
            self.defect_image_list.append_mylist(path, self.name)

    def UpDate_Slider(self):
        if len(self.save_defect_images_list) > 0:
            # print("a")
            # threading.Thread(
            #     target=update_defect_images_on_ui, args=(self, "next")
            # ).start()
            update_defect_images_on_ui(ui_obj=self, prevornext="next")
            # self.defect_image_list_next_func()
            (self.current_image_list) = self.defect_image_list.get_n_current(
                name="defect", get_annots=False
            )
            # print(current_image_list)
            # current_annots_list = []
            # print("current_image_list", self.current_image_list)
            # # set/update images on UI

    def update_slider_2(self):
        res = set_image_to_ui_slider_full_path(
            ui_obj=self,
            image_path_list=self.current_image_list,
            annot_path_list=[],
            prefix="defect",
            image_per_row=6,
        )

    # def defects_features_extractor(self,cnt,mask):
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     area = cv2.contourArea(cnt)
    #     perimeter = cv2.arcLength(cnt, True)
    #     #thickness=
    #     for i,_ in enumerate(cnt):
    #         mask[]
    #         cnt[i,0,0]
    #         cnt[i,0,1]

    def stop_live(self):
        if self.live_flag:
            self.timer_live.stop()
            self.set_live_flag = False
            print("stop live")

    def start_live(self):
        if not self.live_flag:
            self.timer_live.start()
            self.set_live_flag = True
            print("start live")

    def stop_detect(self):
        print(self.detect_flag)
        if self.detect_flag:
            self.timer_live_detect.stop()
            self.timer_save_defect_images.stop()
            self.defect_slider_show.stop()
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
            self.create_folder()
            self.timer_live_detect.start()
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
        

        parms = {"laser": laser, "mean": mean, "th1": th1, "th2": th2,'frame_rate':fr,'line_speed':ls,'pixel_value':pv,'final_pixel_value':fpv}
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
        print("starttttttttt", self.camera)

        if self.camera == None:
            self.camera = 1
            self.camera_loading()
            try:
                self.camera.start_grabbing()
                if self.camera.camera.IsGrabbing():
                    self.set_btn_image(self.camera_calib_btn, image_open_camera)
                    self.set_btn_image(self.camera_live_btn, image_open_camera)
                    self.enable_disable_camera_btns(True)
                else:
                    self.set_warning(
                        label_name=self.msg_label,
                        text="cannot connect to camera",
                        level=2,
                    )
                    self.eror_img = 0
                    self.sett_cam_size.setText("-")
                    self.sett_cam_fps.setText("-")
            except:
                self.set_warning(
                    label_name=self.msg_label,
                    text="cannot connect to camera",
                    level=2,
                )
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

        print("enddddddddddddddd", self.camera)

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
        # print(folders)
        # name=['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4']
        for _,button_number in enumerate(self.folders):
            button = QPushButton()
            bt = str(button_number).split("'")[1]
            button.setText(bt)
            button.setObjectName('%d' % _)
            button.clicked.connect(self.click)
            button.setFont(QFont("Sanserif", 15))
            # button.setIcon(QIcon("G:\work/abrarvan\images/folder-icon.png"))
            button.setIconSize(QSize(10,10))
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);color : rgb(255,255,255)}")
            self.verticalLayout_20.addWidget(button)


    def clearLayout(self,layout):
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
        print('path_  sssssssssss',path_)
        self.lineEdit_load_path.setText(path_)
        path = os.listdir(path_)
        self.img_path=[]
        for it in path:
            if it[-3:]=='jpg':
                # print(it)
                self.img_path.append(it)
        print(self.img_path)
        for _,i in enumerate(self.img_path):

            label = QLabel()
            label.setObjectName('label_{}_{}'.format(path_,i))
            # label.mousePressEvent = self.show_image()
            # label.clicked.connect(self.show_image)
            label.setFont(QFont("Sanserif", 15))
            img_path = (os.path.join(path_,i))
            # self.set_btn_image(label, img_path)
            # label.setIconSize(QSize(200,200))
            self.set_image_label(label, cv2.imread(img_path))
            label.setCursor(Qt.PointingHandCursor)
            self.gridLayout.addWidget(label)  

    def show_image(self,e):

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
