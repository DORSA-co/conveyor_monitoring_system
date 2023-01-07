import cv2
import numpy as np
import time
import pandas as pd


# def moving_average(a, n=150):
#     ret = np.cumsum(a, dtype=float)
#     ret[n:] = ret[n:] - ret[:-n]
#     return (ret[n - 1 :] / n).astype("uint8")


# img = cv2.imread(r"lab\defect (1).png")
# img = cv2.resize(img, (224, 224))
# _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(
#     gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
# )
# bgr_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
# # cv2.drawContours(bgr_img, contours, -1, (0, 255, 0), 3)
# mask = np.zeros((224, 224), np.uint8)
# # mask[contours[0][:, 0, 1], contours[0][:, 0, 0]] = 255


# index = 3
# k = 100
# print(len(contours))
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# for ctn in contours:
#     x = cv2.contourArea(ctn)
#     print(x)


# t1 = time.time()
# x_y = {"x": list(contours[index][:, 0, 0]), "y": list(contours[index][:, 0, 1])}
# x_y = pd.DataFrame(x_y)
# x_y["x"] = x_y["x"].rolling(150).mean()
# x_y["y"] = x_y["y"].rolling(150).mean()
# t2 = time.time()
# print(t2 - t1)
# time_ = 0
# for index, cnt in enumerate(contours):
#     t3 = time.time()
#     x = moving_average(cnt[:, 0, 0])
#     y = moving_average(cnt[:, 0, 1])
#     print(cnt[:, 0, 0].max(), cnt[:, 0, 0].min())
#     print(cnt[:, 0, 1].max(), cnt[:, 0, 1].min())
#     t4 = time.time()
#     # print(len(cnt[:, 0, 0]))
#     # print(len(contours[index][:, 0, 1]))
#     # print(x)
#     # print(y)

#     if len(x) != 0:
#         mask[y, x] = 255
#         cv2.line(mask, (x[0], y[0]), (x[-1], y[-1]), 255, thickness=1)
#     # print(t4 - t3)
#     time_ += t4 - t3
# print(time_ / 1.00000)


# t5 = time.time()
# for i, pt in enumerate(contours[index]):

#     if contours[index][i : i + k, 0, 0].shape[0] == k:
#         x_ = contours[index][i : i + k, 0, 0].mean()
#         y_ = contours[index][i : i + k, 0, 1].mean()
#     else:
#         x_ = contours[index][i, 0, 0]
#         y_ = contours[index][i, 0, 1]

#     mask[int(y_), int(x_)] = 255
# t6 = time.time()
# print(t6 - t5)


# cv2.imshow("xxx", mask)
# cv2.imshow("yyy", bgr_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# segment = np.ones((180, 355), dtype=np.uint8) * 255
# cv2.rectangle(segment, (0, 0), (355, 180), color=0, thickness=20)
# temp = np.resize(segment, (1800, 355))
# temp = cv2.rotate(temp, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("jj", temp)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# def nothing(x):
#     print(x)


# cv2.namedWindow("controls")
# cv2.createTrackbar("R", "controls", 3, 255, nothing)
# cv2.createTrackbar("G", "controls", 3, 255, nothing)
# cv2.createTrackbar("B", "controls", 3, 255, nothing)

# mask = np.zeros((224, 224, 3), np.uint8)


# while True:
#     mask[:, :, 0] = int(cv2.getTrackbarPos("R", "controls"))
#     mask[:, :, 1] = int(cv2.getTrackbarPos("G", "controls"))
#     mask[:, :, 2] = int(cv2.getTrackbarPos("B", "controls"))
#     mask = cv2.cvtColor(mask, cv2.COLOR_RGB2BGR)
#     cv2.imshow("mask", mask)
#     cv2.waitKey(5)

# segment_shematic = np.ones((224, 224, 3), np.uint8)
# segment_shematic[:, :, 0] = 223
# segment_shematic[:, :, 1] = 193
# segment_shematic[:, :, 2] = 83
# segment_shematic = cv2.cvtColor(segment_shematic, cv2.COLOR_RGB2BGR)

# segment_shematic = cv2.putText(
#     segment_shematic,
#     ("0-20"),
#     (80, 120),
#     cv2.FONT_HERSHEY_SIMPLEX,
#     1,
#     (255, 255, 255),
#     4,
# )


# cv2.imshow("df", segment_shematic)
# cv2.waitKey(0)
