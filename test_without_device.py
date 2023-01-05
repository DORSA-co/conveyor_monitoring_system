import os
import cv2
import open3d as o3d
import numpy as np
from pypylon import pylon
import time
from PIL import Image, ImageFilter
from utils.camera_connection import Collector
from utils.heatmap import heatmap
from utils.laserScaner import ProfileMeter
import matplotlib.pyplot as plt
import math
import pandas as pd
import time


class cameraGraber:
    def __init__(self):

        # conecting to the first available camera
        self.camera = pylon.InstantCamera(
            pylon.TlFactory.GetInstance().CreateFirstDevice()
        )
        # Grabing Continusely (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.converter = pylon.ImageFormatConverter()

        # -------------------------------------------------------------------------------------

        self.camera.ExposureTimeRaw.SetValue(3000)
        # self.camera.ExposureTime.SetValue(self.exposure)

        # -------------------------------------------------------------------------------------
        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def grabber(self, rotate=None):
        i = 0
        while self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(
                5000, pylon.TimeoutHandling_ThrowException
            )
            self.camera.ClearBufferModeEnable.next()
            self.camera.ClearBufferModeEnable.acquire()
            if grabResult.GrabSucceeded():
                # Access the image data
                image = self.converter.Convert(grabResult)
                img = image.GetArray()

                if rotate != None:
                    img = cv2.rotate(img, rotate)
                yield img


def imshow(name, img):
    cv2.imshow(name, cv2.resize(img, None, fx=0.5, fy=0.5))
    # cv2.imshow(name, img)


# ________________________________________________________________________________________________________________________________________
#                                                           Main
# ________________________________________________________________________________________________________________________________________


def on_change(value):
    # print(value)
    pass


# collector = Collector(serial_number="0", list_devices_mode=True)
# # get serial number of available cameras
# serial_list = collector.serialnumber()
# camera_serials = serial_list

# camera = Collector(
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

# camera.start_grabbing()


profile = ProfileMeter()
itr = 0
width = 3840


MIN_DEFECT_AREA = 1000
MIN_DEFECT_HEIGHT = 200
MIN_DEFECT_WIDTH = 200

show_bound = 900


# cv2.namedWindow("controls")
# cv2.createTrackbar("th", "controls", 3, 250, on_change)


main_path = r"images\Newfolder3"
img_file_name = os.listdir(main_path)

fps = 42
i = 0


WIDTH = 3840
mean_index = 15
weights = np.zeros((mean_index, width))
weights[0 : mean_index // 3, :] = 1
weights[mean_index // 3 : 2 * (mean_index // 3)] = 10
weights[2 * (mean_index // 3), :] = 20
row_5 = np.zeros((mean_index, width))
mask = heatmap(width, chanel=1)
z_heatmap = heatmap(WIDTH, chanel=1, creat_total_32=True)


def moving_average(a, n=30):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return (ret[n - 1 :] / n).astype("uint32")


def average_moveing_contour(cnt):

    x = moving_average(cnt[:, 0, 0])
    y = moving_average(cnt[:, 0, 1])
    return x, y


pixel_size = 0.00647  # cm
v = 120 / 13.5  # pixel per secend
tpf = 1 / 47.7  # time per frame =1/fps
rate = 30  # int(v*tpf)#pixel per frame
speed_rate = 100 / (rate * 14 * fps)  # cm per frame
r = rate
j = -1
main_raw_canvas = np.ones((show_bound, width), dtype=np.uint8) * 255
while True:

    j += 1
    if j == len(img_file_name):
        j = 0
        # break

        # z_heatmap.reset_32bit_part()
        # mask.reset()

    frame = cv2.imread(os.path.join(main_path, img_file_name[j]))
    # (
    #     _,
    #     frame,
    # ) = camera.getPictures()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laser_mask = profile.laser_detetctor(frame, thresh=1, medianBlur_kernel=5)
    # imshow("f", frame)

    pts = profile.extract_points_mean(laser_mask)
    profile.save_points(pts)
    xyz_current = profile.get_cloudPoints_current()

    # extracts each z pivots
    row = np.zeros(WIDTH, dtype=np.uint32)
    row[xyz_current[:, 0]] = xyz_current[:, 2]
    # z-pivot capture
    z_row_array = np.array((row), dtype=np.uint32)
    z_heatmap.optimiezedAdd_32_bits(z_row_array, colormap=None)
    # z_pivots_h = z_heatmap.getmatrix_32_bit_h(r)
    z_pivots = z_heatmap.getmatrix_32_bit(r)
    row2 = row.copy()
    row_temp = np.ones(width) * 255

    if j < mean_index:
        xxx = np.array((255 * row2 / row2.max()), dtype=np.uint8)
        mask.optimiezedAdd(xxx, colormap=None)
        row_5[j, :] = row
    else:
        x = np.average(row_5, axis=0, weights=weights)
        row_temp[np.where((row2 - x) > 15)] = 0  # ekhtelafe row jadid ba ghabli
        xxx = np.array((255 * row_temp / row_temp.max()), dtype=np.uint8)
        locs = np.where(xxx < 100)[0]
        for k, _ in enumerate(locs[:-2]):
            if locs[k + 1] - locs[k] < 200:
                xxx[locs[k] : locs[k + 1]] = 0
        mask.optimiezedAdd(xxx, colormap=None)
        row_5[0 : mean_index - 1, :] = row_5[1:mean_index, :]
        row_5[mean_index - 1, :] = row2

    # out_mask_h = mask.get_hImage(int(show_bound / r), r)
    out_mask = mask.getImage(int(show_bound / r), r)
    out_mask_h = cv2.medianBlur(out_mask, 5)
    _, dst = cv2.threshold(out_mask_h, 254, 255, cv2.THRESH_BINARY_INV)
    # contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imshow("rrr", z_pivots)
    # for k, cnt in enumerate(contours):
    #     # x, y, w, h = cv2.boundingRect(cnt)
    #     area = cv2.contourArea(cnt)
    #     perimeter = cv2.arcLength(cnt, True)
    #     if area > 5000 or perimeter > 5000:
    #         # x, y, w, h = cv2.boundingRect(cnt)
    #         # dst = cv2.rectangle(dst, (x, y), (x + w, y + h), 255, 3)
    #         raw_canvas = np.zeros(dst.shape, dtype=np.uint8)
    #         x1, y1 = average_moveing_contour(cnt=cnt)
    #         raw_canvas[y1, x1] = 255
    #         # cv2.line(raw_canvas, (x1[0], y1[0]), (x1[-1], y1[-1]), 255, thickness=1)
    #         # single_contours, _ = cv2.findContours(
    #         #     raw_canvas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    #         # )
    #         # cv2.drawContours(raw_canvas, single_contours, -1, 255, -1)
    #         # locs = np.where(raw_canvas == 255)
    #         # main_raw_canvas[locs[0], locs[1]] = z_pivots[locs[0], locs[1]]

    # imshow("dst", main_raw_canvas)
    # imshow("dst_", dst)
    # imshow("z_pivots_h", z_pivots_h)
    cv2.waitKey(1)
    # if cv2.waitKey(0) & 0xFF == ord("x"):
    #     break


cv2.destroyAllWindows()
