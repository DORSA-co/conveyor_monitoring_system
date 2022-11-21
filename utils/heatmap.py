import numpy as np

# import seaborn as sns
# import matplotlib.pylab as plt
import cv2 as cv
import random
import time


class heatmap:
    def __init__(self, w, chanel=3):
        """creat a class for save heat map

        Args:
            w (uint): width of camera(pixel)
        """
        self.chanel = chanel
        self.width = w
        self.size = 0
        self.capacity = 4
        self.total = np.zeros((self.capacity, w, self.chanel), dtype=np.uint8)

    def addArray(self, row):
        """add heatmap of a row to saved image but not time optimized for large size

        Args:
            row (numpy array): a numpy array in shape(width,)
        """
        # t1=time.time()
        row = [row]
        row = np.array(row, dtype=np.uint8)
        row = cv.applyColorMap(row, cv.COLORMAP_JET)
        self.size = min(self.size + 1, self.array_bound + 1)
        self.total = np.array([np.append(self.total, row)], dtype=np.uint8).reshape(
            self.size, self.width, 3
        )
        self.total = self.total[max(self.size - self.array_bound, 0) : self.size]

        # t2=time.time()
        # print(f' add run time: {t2-t1}')

    def optimiezedAdd(self, row, colormap=cv.COLORMAP_JET):
        """add heat map of a row to saved image fast

        Args:
            row (numpy array): a numpy array in shape(width,)
        """
        # t1 = time.time()
        row = np.array(row, dtype=np.uint8)
        if colormap != None:
            row = cv.applyColorMap(row, colormap)
        if self.size == self.capacity:
            self.capacity *= 4
            newdata = np.zeros((self.capacity, self.width, self.chanel), dtype=np.uint8)
            newdata[: self.size] = self.total
            self.total = newdata
        # print(row[:,0].shape)
        # print(self.total[self.size].shape)
        if colormap != None:
            self.total[self.size] = row[:, 0]
        else:
            row = row.reshape(self.width, self.chanel)
            self.total[self.size] = row[:]
        self.size += 1

        # t2=time.time()
        # print(f' add run time: {t2-t1}')

    def reset(self):
        """clear the saved image"""
        self.size = 0
        self.capacity = 4
        self.total = np.zeros((self.capacity, self.width, self.chanel), dtype=np.uint8)

    def getImage(self, bound, r):
        """return a image(width = self.width and height = bound*r) stored in  a numpy array

        Args:
            bound (uint): height of output image

        Returns:
            numpy array: return  a numpy array contain output image
        """

        bounded = cv.resize(
            self.total[max(self.size - bound, 0) : self.size], None, fx=1, fy=r
        )
        return bounded


# import matplotlib.pyplot as plt
# import numpy as np
# import cv2

# mask = np.zeros((1200, 1000), np.uint8)
# print(mask.shape)
# cv2.imshow("xxx", mask)
# k = cv2.waitKey(0)
