import sys
import cv2
import numpy as np


from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage

from utils.heatmap import heatmap
from utils.laserScaner import ProfileMeter
from utils.camera_connection import Collector

UI_PATH = r"UI\main_UI.ui"
NO_IMAGE = cv2.imread(r"UI\images_icon\no_image.png")
WIDTH = 3840
SHOW_BOUND = 900

MIN_DEFECT_AREA = 0
MIN_DEFECT_WIDTH = 0
MIN_DEFECT_HEIGHT = 0


class Ui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(UI_PATH, self)

        # algo parameter
        self.laser_detector_threshold = 3
        self.norm_level_value = 210
        self.threshold1 = 0
        self.threshold2 = 0
        ################

        self.qimage = QImage(
            NO_IMAGE, NO_IMAGE.shape[1], NO_IMAGE.shape[0], QImage.Format_RGB888
        )
        self.pixmap = QPixmap(self.qimage)
        self.pixmap = self.pixmap.scaled(
            NO_IMAGE.shape[0], NO_IMAGE.shape[1], Qt.KeepAspectRatio
        )

        self.LBL_live_camera.setPixmap(self.pixmap)
        self.LBL_live_camera_for_setting_image_quality.setPixmap(self.pixmap)

        # speed parameter###################################################
        self.pixel_size = 0.00647  # cm
        self.Vpps = 120 / 13.5  # pixel per secend
        self.fps = 47.7
        self.tpf = 1 / 47.7  # time per frame =1/fps
        self.rate = 30  # int(v*tpf)#pixel per frame
        self.speed_rate = 100 / (self.rate * 14 * self.fps)  # cm per frame
        ###################################################################

        # camera setting##############################
        self.camera_loading()

        #############################################
        self.widget_connector()
        # self.profile = ProfileMeter()
        # self.mask = heatmap(WIDTH, chanel=1)

        self.show()

    def camera_loading(self):
        self.collector = Collector(serial_number="0", list_devices_mode=True)
        self.serial_list = self.collector.serialnumber()
        self.serial_number_combo.addItems(self.serial_list)

        if self.serial_list != []:

            self.camera = Collector(
                self.serial_list[0],
                exposure=200,
                gain=250,
                trigger=False,
                delay_packet=16256,
                packet_size=9000,
                frame_transmission_delay=0,
                height=1212,
                width=1800,
                offet_x=136,
                offset_y=0,
                manual=False,
                list_devices_mode=False,
            )
            self.camera.start_grabbing()
            self.msg_label.setText("FIRST AVALABLE CAMERAS CONNECTS TO SYSTEM")
            return True
        else:
            self.msg_label.setText(
                "NO CAMERAS CONNECTS AVALABLE WITH,STANDAED PROTOCOL"
            )
            return False

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

        self.camera.stop_grabbing()
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
        self.camera.start_grabbing()

    def set_live_flag(self, value):
        self.live_flag = value

    def set_live_image(self):

        # this function should edit

        while self.live_flag:
            img = self.camera.getPictures()
            # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            self.qimage = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
            self.pixmap = QPixmap(self.qimage)
            self.pixmap = self.pixmap.scaled(
                img.shape[0], img.shape[1], Qt.KeepAspectRatio
            )
            self.LBL_live_camera_for_setting_image_quality.setPixmap(self.pixmap)
            cv2.waitKey(1)
        else:
            self.qimage = QImage(
                NO_IMAGE, NO_IMAGE.shape[1], NO_IMAGE.shape[0], QImage.Format_RGB888
            )
            self.pixmap = QPixmap(self.qimage)
            self.pixmap = self.pixmap.scaled(
                NO_IMAGE.shape[0], NO_IMAGE.shape[1], Qt.KeepAspectRatio
            )
            self.LBL_live_camera_for_setting_image_quality.setPixmap(self.pixmap)

    def detect(self, frame):
        laser_mask = self.profile.laser_detetctor(
            frame, thresh=self.laser_detector_threshold
        )
        laser_mask = cv2.medianBlur(laser_mask, 5)
        pts = self.profile.extract_points_mean(laser_mask)
        mean_img = self.profile.pts2img(pts, laser_mask.shape)
        self.profile.save_points(pts)
        xyz_current = self.profile.get_cloudPoints_current()

        row = np.zeros(WIDTH)
        row[xyz_current[:, 0]] = xyz_current[:, 2]
        self.mask.optimiezedAdd(
            255
            * np.array((row - self.norm_level_value) > self.threshold1, dtype=np.uint8),
            colormap=None,
        )
        out_mask = np.array(self.mask.getImage(int(SHOW_BOUND / self.rate), self.rate))
        img, dst = cv2.threshold(out_mask, self.threshold2, 255, cv2.THRESH_BINARY)
        median = cv2.medianBlur(dst, 5)

        contours, _ = cv2.findContours(
            median, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        return contours,median

    def indicate_features_and_emergency_of_defect(self, contours, mask):

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            perimeter = cv2.arcLength(cnt, True)
            flag, color, type_ = self.contour_filter(
                w=w, h=h, area=area, perimeter=perimeter
            )
            if flag:
                mask[x : x + w, y : y + h] = self.average_moveing_contour(
                    cnt=cnt, k_pre_points=50, mask=mask[x : x + w, y : y + h]
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

    def contour_filter(self, w, h, area, perimeter):
        # will be completed
        color = (255, 0, 0)
        type_ = f"defect"
        return True, color, type_

    def average_moveing_contour(cnt, k_pre_points, mask):
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
        frame = self.camera.getPictures()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        contours,mask=self.detect(frame)
        self.indicate_features_and_emergency_of_defect(contours=contours,mask=mask)


    def widget_connector(self):
        self.BTN_camera_setting.clicked.connect(self.load_page)
        self.BTN_dashboard.clicked.connect(self.load_page)
        self.BTN_calibration_setting.clicked.connect(self.load_page)
        self.BTN_general_setting.clicked.connect(self.load_page)
        self.BTN_history.clicked.connect(self.load_page)

        self.BTN_camera_connect.clicked.connect(lambda: self.set_live_flag(value=True))
        self.BTN_camera_connect.clicked.connect(self.set_live_image)
        self.BTN_camera_disconnect.clicked.connect(
            lambda: self.set_live_flag(value=False)
        )

        self.BTN_camera_setting_apply.clicked.connect(self.camera_setting)

        self.BTN_scane_start.clicked.connect(self.surface_scanning)

        # self.camera_setting_apply_btn.clicked.connect(self.xxx)

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

    # def xxx(self):
    #     x = self.trigger_combo.currentText()
    #     print(x)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
