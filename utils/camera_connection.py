"""
########################################
---------------------------------------

Made with Malek & Milad

Features:

    ● Create Unlimite Object of Cameras and Live Preview By serial number
    ● Set Bandwitdh Of each Cameras
    ● Set gain,exposure,width,height,offet_x,offset_y
    ● Get tempreture of Cmeras
    ● Set Trigger Mode on
    ● There are Some diffrents between ace2(pro) and ace

---------------------------------------
########################################
"""

from pickle import FALSE
from pypylon import pylon
import cv2
import time
import numpy as np
from pypylon import genicam

DEBUG = False
NULL_IMG = np.zeros([1200, 1920, 3], dtype=np.uint8)

class Collector:
    def __init__(
        self,
        serial_number,
        gain=0,
        exposure=70000,
        max_buffer=20,
        trigger=True,
        delay_packet=100,
        packet_size=1500,
        frame_transmission_delay=0,
        width=1000,
        height=1000,
        offet_x=0,
        offset_y=0,
        manual=False,
        list_devices_mode=False,
    ):
        """Initializes the Collector
        Args:
            gain (int, optional): The gain of images. Defaults to 0.
            exposure (float, optional): The exposure of the images. Defaults to 3000.
            max_buffer (int, optional): Image buffer for cameras. Defaults to 5.
        """
        self.gain = gain
        self.exposure = exposure
        self.max_buffer = max_buffer
        self.cont_eror = 0
        self.serial_number = serial_number
        self.trigger = trigger
        self.dp = delay_packet
        self.ps = packet_size
        self.ftd = frame_transmission_delay
        self.width = width
        self.height = height
        self.offset_x = offet_x
        self.offset_y = offset_y
        self.manual = manual
        self.list_devices_mode = list_devices_mode
        self.exitCode = 0

        self.__tl_factory = pylon.TlFactory.GetInstance()
        devices = []

        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        for device in self.__tl_factory.EnumerateDevices():
            if (
                device.GetDeviceClass() == "BaslerGigE"
                or device.GetDeviceClass() == "BaslerUsb"
            ):
                devices.append(device)

        assert len(devices) > 0 , 'No Camera is Connected!'

        if self.list_devices_mode:
            self.cameras = list()

            for device in devices:
                camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))
                self.cameras.append(camera)

        else:
            for device in devices:
                camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))

                if camera.GetDeviceInfo().GetSerialNumber() == self.serial_number:
                    self.camera = camera

                    break

        assert len(devices) > 0 , 'No Camera is Connected!'

    def eror_window(self, msg, level):
        self.window_eror = UI_eror_window()
        self.window_eror.show()
        self.window_eror.set_text(msg, level)

    def tempreture(self):
        return self.camera.TemperatureAbs.GetValue()

    def start_grabbing(self):

        device_info = self.camera.GetDeviceInfo()
        self.camera.Open()
        if self.manual:
                self.camera.ExposureTime.SetValue(self.exposure)
                self.camera.Gain.SetValue(self.gain)
                self.camera.Width.SetValue(self.width)
                self.camera.Height.SetValue(self.height)
                self.camera.OffsetX.SetValue(self.offset_x)
                self.camera.OffsetY.SetValue(self.offset_y)

        self.camera.Close()
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.exitCode = 0

    def update_exposure(self,val):
        self.exposure=val
        self.camera.ExposureTime.SetValue(self.exposure)

    def upadte_gain(self,val):
        self.gain=val
        self.camera.Gain.SetValue(self.gain)

    def update_offsetx(self,val):
        self.offset_x=val
        self.camera.OffsetX.SetValue(self.offset_x)

    def update_offsety(self,val):
        self.offset_y=val
        self.camera.OffsetY.SetValue(self.offset_y)

    def stop_grabbing(self):
        self.camera.Close()

    def listDevices(self):
        """Lists the available devices"""
        for i, camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()
            print(
                "Camera #%d %s @ %s (%s) @ %s"
                % (
                    i,
                    device_info.GetModelName(),
                    device_info.GetIpAddress(),
                    device_info.GetMacAddress(),
                    device_info.GetSerialNumber(),
                )
            )

    def serialnumber(self):
        serial_list = []
        for i, camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()
            serial_list.append(device_info.GetSerialNumber())
        return serial_list

    def getPictures(self, time_out=500):
        try:
            if DEBUG:
                print("TRIGE Done")
            if self.camera.IsGrabbing():
                if DEBUG:
                    print("Is grabbing")

                grabResult = self.camera.RetrieveResult(
                    time_out, pylon.TimeoutHandling_ThrowException
                )

                if grabResult.GrabSucceeded():
                    if DEBUG:
                        print("Grab Succed")

                    image = self.converter.Convert(grabResult)
                    img = image.Array
                    return True, img

                else:
                    img = NULL_IMG
                    self.cont_eror += 1
                    print("eror", self.cont_eror)
                    print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
            else:
                print("eror in grab camera")
                img = NULL_IMG
                return False, img
        except:
            print('eror in get picture')
            return False, img

    def get_cam(self, i):
        return self.camera


if __name__ == "__main__":


    collector = Collector(
        "40079306",
        exposure=2000,
        gain=10,
        trigger=False,
        delay_packet=8988,
        packet_size=9000,
        frame_transmission_delay=9018,
        height=1200,
        width=1920,
        offet_x=0,
        offset_y=0,
        manual=True,
        list_devices_mode=False,
    )
    collector.start_grabbing()

    while True:
        s, img = collector.getPictures()
        cv2.imshow("img1", cv2.resize(img, None, fx=0.2, fy=0.2))
        cv2.waitKey(1000)
