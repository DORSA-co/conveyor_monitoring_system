import numpy as np

# import seaborn as sns
# import matplotlib.pylab as plt
import cv2 as cv
import random
import time


class heatmap:
    def __init__(self, w, chanel=3, creat_total_32=False):
        """creat a class for save heat map

        Args:
            w (uint): width of camera(pixel)
        """
        self.chanel = chanel
        self.width = w
        self.size = 0
        self.capacity = 4
        self.total = np.zeros((self.capacity, w, self.chanel), dtype=np.uint8)
        self.h_total = np.zeros((w, self.capacity, self.chanel), dtype=np.uint8)

        if creat_total_32:
            self.size_32 = 0
            self.capacity_32 = 4
            self.total_32 = np.zeros((self.capacity, w, self.chanel), dtype=np.uint32)
            self.h_total_32 = np.zeros((w, self.capacity, self.chanel), dtype=np.uint32)

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
        row = np.array(row, dtype=np.uint8)
        if colormap != None:
            row = cv.applyColorMap(row, colormap)
        if self.size == self.capacity:
            self.capacity *= 4
            newdata = np.zeros((self.capacity, self.width, self.chanel), dtype=np.uint8)
            newdata[: self.size] = self.total
            self.total = newdata
            # _____________________related to h-part
            h_newdata = np.zeros(
                (self.width, self.capacity, self.chanel), dtype=np.uint8
            )
            h_newdata[:, 0 : self.size, :] = self.h_total
            self.h_total = h_newdata
            # _____________________
        if colormap != None:
            self.total[self.size] = row[:, 0]
        else:
            row = row.reshape(self.width, self.chanel)
            self.total[self.size] = row[:]
            # _____________________related to h-part

            self.h_total[:, self.size, :] = row[:]
            # _____________________
        self.size += 1

    # ___________________________________________________________________#32 bit part for z-pivots
    def optimiezedAdd_32_bits(self, row, colormap=cv.COLORMAP_JET):

        row = np.array(row, dtype=np.uint32)
        if colormap != None:
            row = cv.applyColorMap(row, colormap)
        if self.size_32 == self.capacity_32:
            self.capacity_32 *= 4
            newdata = np.zeros(
                (self.capacity_32, self.width, self.chanel), dtype=np.uint32
            )
            newdata[: self.size_32] = self.total_32
            self.total_32 = newdata

            # _____________________related to h-part
            h_newdata = np.zeros(
                (self.width, self.capacity_32, self.chanel), dtype=np.uint32
            )
            h_newdata[:, 0 : self.size_32, :] = self.h_total_32
            self.h_total_32 = h_newdata
            # _____________________

        if colormap != None:
            self.total_32[self.size_32] = row[:, 0]
        else:
            row = row.reshape(self.width, self.chanel)
            self.total_32[self.size_32] = row[:]
            # _____________________related to h-part

            self.h_total_32[:, self.size_32, :] = row[:]
            # _____________________
        self.size_32 += 1

    def getmatrix_32_bit(self, r):

        temp = self.total_32[0 : self.size_32].astype(np.uint8)
        bounded = cv.resize(temp, None, fx=1, fy=r)
        return bounded

    def getmatrix_32_bit_h(self, r):
        temp = self.h_total_32[:, 0 : self.size_32].astype(np.uint8)
        bounded = cv.resize(temp, None, fx=r, fy=1)
        return bounded

    def reset_32bit_part(self):

        self.size_32 = 0
        self.capacity_32 = 4
        self.total_32 = np.zeros(
            (self.capacity_32, self.width, self.chanel), dtype=np.uint32
        )
        self.h_total_32 = np.zeros(
            (self.width, self.capacity_32, self.chanel), dtype=np.uint32
        )

    def reset(self):
        """clear the saved image"""
        self.size = 0
        self.capacity = 4
        self.total = np.zeros((self.capacity, self.width, self.chanel), dtype=np.uint8)
        self.h_total = np.zeros(
            (self.width, self.capacity, self.chanel), dtype=np.uint8
        )

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

    def get_hImage(self, bound, r):

        bounded = cv.resize(
            self.h_total[:, max(self.size - bound, 0) : self.size, :], None, fx=r, fy=1
        )

        return bounded
