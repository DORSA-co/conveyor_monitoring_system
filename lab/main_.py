from PyQt5 import QtWidgets, uic
import sys
from utils.heatmap import heatmap
from utils.laserScaner import ProfileMeter
from utils.camera_connection import Collector
import numpy as np

import cv2
import os
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy, QApplication
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5 import QtCore, QtGui


PATHS = os.listdir(r"image_conv_with_stable_config")
SIZE_OF_VIEW = (1500, 400)

kernel = np.array([[0, -1, 0], [-1, 1, -1], [0, -1, 0]])
kernel_ = np.ones((5, 5), np.uint8)


itr = 0
width = 1500

min = 350
norm = 380
max = 395

fps = 42
i = 0


MIN_DEFECT_AREA = 1000
MIN_DEFECT_HEIGHT = 50
MIN_DEFECT_WIDTH = 50


class Ui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(r"UI\ui_main.ui", self)  # Load the .ui file

        self.LBL_LiveHeatMap.setScaledContents(True)
        self.LBL_LiveHeatMap.setWhatsThis("")
        # self.LBL_ThicknessTrend.setScaledContents(True)
        # self.LBL_ThicknessTrend.setWhatsThis("")

        # self.collector = Collector(serial_number="0", list_devices_mode=True)
        # # get serial number of available cameras
        # serial_list = self.collector.serialnumber()
        # camera_serials = serial_list

        # self.camera = Collector(
        #     camera_serials[0],
        #     exposure=200,
        #     gain=250,
        #     trigger=False,
        #     delay_packet=16256,
        #     packet_size=9000,
        #     frame_transmission_delay=0,
        #     height=1212,
        #     width=1800,
        #     offet_x=136,
        #     offset_y=0,
        #     manual=False,
        #     list_devices_mode=False,
        # )

        # self.camera.start_grabbing()

        # algo:
        self.profile = ProfileMeter()
        self.mask = heatmap(1500, chanel=1)
        self.show_bound = 900

        self.thersh_laser_detector = 36
        self.thresh_of_roughness = 14
        self.thresh_of_binary = 100

        self.pixel_size = 0.013  # cm
        self.v = 1200 / 1.5  # pixel per secend
        self.tpf = 1 / 42  # time per frame =1/fps
        self.rate = 17  # int(v*tpf)#pixel per frame
        self.speed_rate = 100 / (self.rate * 14 * fps)  # cm per frame
        self.r = self.rate

        self.create_trend_chart()

        self.show()  # Show the GUI

    def create_trend_chart(
        self,
        bg_color="#000000",
        text_color="#FFFFFF",
        axisX_title="conveyor position",
        axisX_range=232,
        axisY_title="thickness(mm)",
        axisY_range=6,
        trend_name="thickness",
        trend_color="#FFFF00",
        setpoint_name="Set Point",
        setpoint_color="#008000",
        setpoint_value=0,
        threshold_name="Threshold",
        threshold_color="#FF0000",
        threshold_value=2,
        line_width=2,
    ):

        # create main chart
        self.chart = QChart()
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.setAnimationDuration(1000)
        self.chart.legend().setVisible(False)
        self.chart.setBackgroundBrush(QtGui.QColor(bg_color))
        self.chart.setBackgroundRoundness(0)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        self.chart.setMargins(QtCore.QMargins(0, 0, 0, 0))

        self.chart_axisX = QValueAxis()
        self.chart_axisX.setRange(0, axisX_range)

        self.chart_axisX.setTickCount(10)
        self.chart_axisX.setLabelsBrush(QtGui.QColor(text_color))
        self.chart_axisX.setTitleText(axisX_title)
        self.chart_axisX.setTitleBrush(QtGui.QColor(text_color))

        self.chart_axisY = QValueAxis()
        self.chart_axisY.setRange(2, axisY_range)

        self.chart_axisY.setLabelsBrush(QtGui.QColor(text_color))
        self.chart_axisY.setTickCount(10)
        self.chart_axisY.setTitleText(axisY_title)
        self.chart_axisY.setTitleBrush(QtGui.QColor(text_color))

        self.chart.addAxis(self.chart_axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.chart_axisY, QtCore.Qt.AlignLeft)

        # create chartview
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chartview.setContentsMargins(0, 0, 0, 0)

        # create trend series
        self.trend_series = QLineSeries()
        self.trend_series.setName(trend_name)
        trend_pen = QtGui.QPen()
        trend_pen.setStyle(QtCore.Qt.SolidLine)
        trend_pen.setWidth(line_width)
        trend_pen.setColor(QtGui.QColor(trend_color))
        self.trend_series.setPen(trend_pen)
        ############################################################################
        self.trend_series_1 = QLineSeries()
        self.trend_series_1.setName("th2")
        trend_pen = QtGui.QPen()
        trend_pen.setStyle(QtCore.Qt.SolidLine)
        trend_pen.setWidth(line_width)
        trend_pen.setColor(QtGui.QColor("#008000"))
        self.trend_series_1.setPen(trend_pen)

        self.trend_series_2 = QLineSeries()
        self.trend_series_2.setName("th3")
        trend_pen = QtGui.QPen()
        trend_pen.setStyle(QtCore.Qt.SolidLine)
        trend_pen.setWidth(line_width)
        trend_pen.setColor(QtGui.QColor("#3364FF"))
        self.trend_series_2.setPen(trend_pen)

        self.trend_series_3 = QLineSeries()
        self.trend_series_3.setName("th4")
        trend_pen = QtGui.QPen()
        trend_pen.setStyle(QtCore.Qt.SolidLine)
        trend_pen.setWidth(line_width)
        trend_pen.setColor(QtGui.QColor("#EE3214"))
        self.trend_series_3.setPen(trend_pen)

        self.trend_series_4 = QLineSeries()
        self.trend_series_4.setName("th5")
        trend_pen = QtGui.QPen()
        trend_pen.setStyle(QtCore.Qt.SolidLine)
        trend_pen.setWidth(line_width)
        trend_pen.setColor(QtGui.QColor("#AD24D3"))
        self.trend_series_4.setPen(trend_pen)

        ########################################################################################
        # create setpoint series
        self.setpoint_series = QLineSeries()
        self.setpoint_series.setName(setpoint_name)
        setpoint_pen = QtGui.QPen()
        setpoint_pen.setStyle(QtCore.Qt.DashLine)
        setpoint_pen.setWidth(line_width)
        setpoint_pen.setColor(QtGui.QColor(setpoint_color))
        self.setpoint_series.setPen(setpoint_pen)

        # create threashold serieses
        # top
        self.topthreshold_series = QLineSeries()
        self.topthreshold_series.setName(threshold_name)
        threshold_pen = QtGui.QPen()
        threshold_pen.setStyle(QtCore.Qt.DashLine)
        threshold_pen.setWidth(line_width)
        threshold_pen.setColor(QtGui.QColor(threshold_color))
        self.topthreshold_series.setPen(threshold_pen)
        # bottom
        self.btmthreshold_series = QLineSeries()
        self.btmthreshold_series.setName(threshold_name)
        threshold_pen = QtGui.QPen()
        threshold_pen.setStyle(QtCore.Qt.DashLine)
        threshold_pen.setWidth(line_width)
        threshold_pen.setColor(QtGui.QColor(threshold_color))
        self.btmthreshold_series.setPen(threshold_pen)

        # add series to chart
        self.chart.addSeries(self.trend_series)
        self.chart.addSeries(self.setpoint_series)
        self.chart.addSeries(self.topthreshold_series)
        self.chart.addSeries(self.btmthreshold_series)

        self.chart.addSeries(self.trend_series_1)
        self.chart.addSeries(self.trend_series_2)
        self.chart.addSeries(self.trend_series_3)
        self.chart.addSeries(self.trend_series_4)

        # attach axis
        self.trend_series.attachAxis(self.chart_axisX)
        self.trend_series_1.attachAxis(self.chart_axisX)
        self.trend_series_2.attachAxis(self.chart_axisX)
        self.trend_series_3.attachAxis(self.chart_axisX)
        self.trend_series_4.attachAxis(self.chart_axisX)

        self.setpoint_series.attachAxis(self.chart_axisX)
        self.topthreshold_series.attachAxis(self.chart_axisX)
        self.btmthreshold_series.attachAxis(self.chart_axisX)

        self.trend_series.attachAxis(self.chart_axisY)
        self.trend_series_1.attachAxis(self.chart_axisY)
        self.trend_series_2.attachAxis(self.chart_axisY)
        self.trend_series_3.attachAxis(self.chart_axisY)
        self.trend_series_4.attachAxis(self.chart_axisY)

        self.setpoint_series.attachAxis(self.chart_axisY)
        self.topthreshold_series.attachAxis(self.chart_axisY)
        self.btmthreshold_series.attachAxis(self.chart_axisY)

        # add chart to ui
        self.trend_chart_frame.layout().addWidget(self.chartview)

    # insert_default setpoint and threshold lines
    # self.chart_insert_record(initialize_chart=True, width_value=None)

    def chart_insert_record(
        self,
        th1,
        th2,
        th3,
        th4,
        th5,
        setpoint_value,
        threshold_value,
        initialize_chart=False,
    ):
        # add default setpoint and threshold lines
        if initialize_chart:
            self.chart_axisY.setRange(
                setpoint_value - threshold_value, setpoint_value + threshold_value
            )

            for i in range(int(self.chart_axisX.max() + 1)):
                self.setpoint_series.append(i, setpoint_value)
            #
            for i in range(int(self.chart_axisX.max() + 1)):
                self.topthreshold_series.append(i, setpoint_value + 0.2)
                self.btmthreshold_series.append(i, setpoint_value - 0.2)

            return

        self.trend_series.append(self.cur_x_index + 1, th1)
        self.trend_series_1.append(self.cur_x_index + 1, th2)
        self.trend_series_2.append(self.cur_x_index + 1, th3)
        self.trend_series_3.append(self.cur_x_index + 1, th4)
        self.trend_series_4.append(self.cur_x_index + 1, th5)
        # self.topthreshold_series.append(self.cur_x_index + 1, setpoint_value + 0.2)
        # self.btmthreshold_series.append(self.cur_x_index + 1, setpoint_value - 0.2)
        self.chart_axisX.setRange(0, self.cur_x_index + 1)

        if self.cur_x_index == 232:
            # self.setpoint_series.append(self.cur_x_index + 1, setpoint_value)
            # self.topthreshold_series.append(self.cur_x_index + 1, setpoint_value + 0.2)
            # self.btmthreshold_series.append(self.cur_x_index + 1, setpoint_value - 0.2)
            # self.chart_axisX.setRange(0, self.cur_x_index + 1)
            self.trend_series.clear()
            self.trend_series_1.clear()
            self.trend_series_2.clear()
            self.trend_series_3.clear()
            self.trend_series_4.clear()

    def widget_connector(self):
        pass

    def test(self, i):

        self.cur_x_index = i
        img = cv2.imread(os.path.join(r"image_conv_with_stable_config", PATHS[i]))
        # img = self.camera.getPictures()
        temp = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        laser_mask = self.profile.laser_detetctor(
            img, thresh=self.thersh_laser_detector
        )
        pts = self.profile.extract_points_mean(laser_mask)
        mean_img = self.profile.pts2img(pts, laser_mask.shape)
        self.profile.save_points(pts)
        xyz_current = self.profile.get_cloudPoints_current()

        self.thickness_1 = (xyz_current[:, 2][0:300].mean()) * self.pixel_size
        self.thickness_2 = (xyz_current[:, 2][300:600].mean()) * self.pixel_size
        self.thickness_3 = (xyz_current[:, 2][600:900].mean()) * self.pixel_size
        self.thickness_4 = (xyz_current[:, 2][900:1200].mean()) * self.pixel_size
        self.thickness_5 = (xyz_current[:, 2][1200:].mean()) * self.pixel_size
        # self.thickness = (xyz_current[:, 2].mean()) * self.pixel_size

        self.chart_insert_record(
            th1=self.thickness_1,
            th2=self.thickness_2,
            th3=self.thickness_3,
            th4=self.thickness_4,
            th5=self.thickness_5,
            setpoint_value=5,
            threshold_value=1,
            initialize_chart=False,
        )

        row = np.zeros(width)
        row[xyz_current[:, 0]] = xyz_current[:, 2]
        # conve normal is Yellow and defects are red or blue
        row1 = row.copy()
        row1[np.where(row1 > max)] = max
        row1[np.where(row1 < min)] = min
        row1 = (row - min) / ((max - min) / 255)

        self.mask.optimiezedAdd(
            255 * np.array((row - norm) > self.thresh_of_roughness, dtype=np.uint8),
            colormap=None,
        )

        out_mask = np.array(self.mask.getImage(int(self.show_bound / self.r), self.r))
        img, dst = cv2.threshold(
            out_mask, self.thresh_of_binary, 255, cv2.THRESH_BINARY
        )

        contours, _ = cv2.findContours(out_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        dst = cv2.cvtColor(out_mask, cv2.COLOR_GRAY2RGB)

        for ctn in contours:
            x, y, w, h = cv2.boundingRect(ctn)

            if cv2.contourArea(ctn) > MIN_DEFECT_AREA:
                dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(
                    dst,
                    f"AREA , {round(h*self.speed_rate,1)}cm * {round(w*self.pixel_size,1)}cm",
                    (x, y + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2,
                )

            elif w > MIN_DEFECT_WIDTH:
                dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(
                    dst,
                    f"AREA , {round(h*self.speed_rate,1)}cm * {round(w*self.pixel_size,1)}cm",
                    (x, y + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2,
                )

            elif h > MIN_DEFECT_HEIGHT:
                dst = cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 0), 3)
                cv2.putText(
                    dst,
                    f"AREA , {round(h*self.speed_rate,1)}cm * {round(w*self.pixel_size,1)}cm",
                    (x, y + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2,
                )

        self.qimage = QImage(dst, dst.shape[1], dst.shape[0], QImage.Format_RGB888)
        self.pixmap = QPixmap(self.qimage)
        self.pixmap = self.pixmap.scaled(
            SIZE_OF_VIEW[0], SIZE_OF_VIEW[1], Qt.KeepAspectRatio
        )
        # should modify
        self.LBL_LiveHeatMap.setPixmap(self.pixmap)

        temp = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
        temp = cv2.rotate(temp, cv2.ROTATE_180)
        temp = cv2.flip(temp, 1)
        self.qimage_ = QImage(temp, temp.shape[1], temp.shape[0], QImage.Format_RGB888)
        self.pixmap_ = QPixmap(self.qimage_)
        self.pixmap_ = self.pixmap_.scaled(
            SIZE_OF_VIEW[0], SIZE_OF_VIEW[1], Qt.KeepAspectRatio
        )
        self.LBL_rawmap.setPixmap(self.pixmap_)


def main():
    i = 0
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()

    while 1:
        i += 1
        if len(PATHS) == i:
            i = 0
        window.test(i)
        if cv2.waitKey(50) & 0xFF == ord("q"):
            break
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
