import cv2
import os
import time
from PyQt5.QtCore import QTimer
from Detection.Defect import (
    defect_detection,
    function_total_complete_defects_cnts,
    function_return_total_depth,
    function_return_critical_flage,
    getDate,
)
from Detection.defectTrackerClass import defectTracker

import cv2
import numpy as np
from backend.Camera.dorsaPylon import Collector, Camera
from backend.Camera import dorsaPylon


Blank_img = np.zeros((640,480),dtype='uint8')

class LiveView_API:

    """Description of the code

    :param
    """

    def __init__(self, ui,db_Report):
        self.ui_live = ui
        self.step = 2
        self.pix_mm_depth = 0.34
        self.pix_mm_width = (140 / 590)  * 3.2
        self.CONVAYER_SPEED = 120  # mm/s
        self.pix_mm_length = (self.step * self.CONVAYER_SPEED / 400 )  * 1.4  #   750   
        self.frame_idx = 1000 // self.step     #remove the error when the defect occur in th first place of frame
        self.refresh_rate = 5
        #self.refresh_rate = 1
        #self.frame_idx = 0    #get error when the defect occur in th first place of frame
        self.collector = Collector() 
      
        self.db_Report=db_Report
        self.defect_tracker = defectTracker(min_g_thresh=120, step_per_line=2, db_Report=self.db_Report)   # min_g_thresh=  66   76
        self.parms_camera_liveView = {
            "Serial": 0,
            "Gain": 0,
            "Exposure": 0,
            "Width": 0,
            "Height": 0,
            "offsetX": 0,
            "offsetY": 0,
        }

        self.parms_calibration_liveView = {
            "Width_critical": 0,
            "Depth_Critical": 0,
            "Lenght_Critical": 0,
            "Width_not_critical": 0,
            "Depth_not_Critical":0,
            "Lenght_not_Critical": 0,
            "Width_not_critical_Max": 0,
            "Depth_not_Critical_Max":0,
            "lenght_not_critical_Max": 0,
        }

        self.parms_algorithm_liveView = {
            "GRADIENT_SIZE": 0,
            "Critical_Depth": 0,
            "TEAR_DEPTH": 0,
            "MAX_ERROR": 0,
            "pix_length":0,
            "pix_width":0,
            "gradient_number" :0
           
        }
        #####self.camera=camera
        #self.cam = camera_connection.Collector(
        #     str(23287291), 217, 5000, 640, 480, 16, 16
        #)
        #self.result1, _ = self.cam.start_grabbing()
        self.camera=None 
        self.button_connector()
        self.button_connector_QTimer()    ###################  for getting image from  camera
        self.button_connector_Stop()

        styles_Live_Camera = { "Camera": "background-color:rgb(218, 0, 0)"}
        self.ui_live.set_style_Camera(styles_Live_Camera)

        self.Error_img =0

    def button_connector(self,):
        self.ui_live.button_connector(self.connect_camera_API,self.dis_connect_camera_API)    ############## for getting image from camera
        ########self.ui_live.button_connector(self.start_selection)  # for getting image from folder

    def button_connector_QTimer(
        self,
    ):  ###################  for getting image from camera
        self.ui_live.button_connector_QTimer(self.start_selection_camera)

    def button_connector_Stop(
      self,
    ):  ###################  for getting image from camera
        self.ui_live.button_connector_stop()

    def stop_camera(self):
        # print("hi")
         self.camera.Operations.stop_grabbing()
         #print(self.camera.Operations.stop_grabbing())

    def start_selection(self):
        self.show_farme()

    def start_selection_camera(self):
        # self.picktimer = QTimer()
        # self.picktimer.timeout.connect(self.show_farme_camera)
        # self.picktimer.start()
        self.show_farme_camera()

    def show_image(self, frame):
        img = frame
        h, w, ch = img.shape
        img = cv2.resize(
            img,
            (w, h),  # this is relative to the camera
           ### (1000, 280),  # 
            interpolation=cv2.INTER_AREA,
        )

        try:
            h, w, ch = img.shape

        except:
            h, w = img.shape

            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            ch = 3
        bytes_per_line = ch * w
        self.ui_live.set_Pixmap(img.data, w, h, bytes_per_line)

    def connect_camera_API(self):
        self.camera = self.collector.get_camera_by_serial(str(23287291))    ###################  for getting image from  camera
        try:
            if self.camera!=None: #and self.camera:
                styles_Live_Camera = { "Camera": "background-color:rgb(47, 140, 68)"}

                self.ui_live.set_style_Camera(styles_Live_Camera)

                self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)         ###################  for getting image from  camera
                self.camera.Operations.start_grabbing()
                self.camera.Parms.set_exposureTime(1500)
                self.camera.Parms.set_gain(217)  #217   #### get the good answer
                self.camera.Parms.set_transportlayer(packet_delay=16000)
                self.ui_live.connect_Camera_liveView_button()
                self.ui_live.set_Meassage_on_API("Connect to Camera Successfully")

            else :

                self.ui_live.set_Meassage_on_API("Please check the connection to the camera")
            

        except:
             print('Cant get camera')


    def dis_connect_camera_API(self):
         
        if self.camera!=None:
            styles_Live_Camera = { "Camera": "background-color:rgb(218, 0, 0)"}
            self.ui_live.set_style_Camera(styles_Live_Camera)


            self.camera.Operations.stop_grabbing()
            self.camera.Operations.close()
            self.camera=None
            self.ui_live.disconnect_Camera_liveView_button()
            self.ui_live.set_Meassage_on_API("Disconnect to Camera Successfully")
             

    def show_farme_camera(self):  ###################  for getting image from  the camera
        
        t1=time.time()
        self.ui_live.disable_live()
        self.ui_live.enable_stop()
       
        if self.camera !=None:
     

            #print("connect To camera on liveView_API")

            ##################  self.camera.build_converter(pixel_type=dorsaPylon.PixelType.GRAY8)         ###################  for getting image from  camera set on main_API
            ##################  self.camera.Operations.start_grabbing()
            ##################  self.camera.Parms.set_exposureTime(5000)
            ##################  self.camera.Parms.set_gain(517)  #217   #### get the good answer



            try:
                img = self.camera.getPictures()
                self.Error_img=0
            except:
                img = Blank_img
                self.Error_img+=1
                if self.Error_img>=5:
                    self.dis_connect_camera_API()

                return
                ###print('Cant Get Picture')
          

            ###########  res,img = self.cam.getPictures()
            idx_Width_critical=self.parms_calibration_liveView["Width_critical"]
            idx_Depth_Critical=self.parms_calibration_liveView["Depth_Critical"]
            idx_Lenght_Critical=self.parms_calibration_liveView["Lenght_Critical"]
        

            idx_Width_not_critical=self.parms_calibration_liveView["Width_not_critical"]
            idx_Depth_not_Critical=self.parms_calibration_liveView["Depth_not_Critical"]
            idx_Lenght_not_Critical=self.parms_calibration_liveView["Lenght_not_Critical"]

            idx_Width_not_critical_Max=self.parms_calibration_liveView["Width_not_critical_Max"]
            idx_Depth_not_Critical_Max=self.parms_calibration_liveView["Depth_not_Critical_Max"]
            idx_Lenght_not_Critical_Max=self.parms_calibration_liveView["lenght_not_critical_Max"]


            #parms_algorithm_liveView["GRADIENT_SIZE"]
            #parms_algorithm_liveView["Critical_Depth"]


            idx_TEAR_DEPTH=self.parms_algorithm_liveView["TEAR_DEPTH"]
            idx_MAX_ERROR=self.parms_algorithm_liveView["MAX_ERROR"]
            idx_Critical_Depth=self.parms_algorithm_liveView["Critical_Depth"]
            idx_TEAR_GRADIENT_SIZE=self.parms_algorithm_liveView["GRADIENT_SIZE"]


            idx_pix_length=self.parms_algorithm_liveView["pix_length"]
            idx_pix_width=self.parms_algorithm_liveView["pix_width"]

           

            idx_gradient_number=self.parms_algorithm_liveView["gradient_number"]
    
           
            #self.pix_mm_length=idx_pix_length
            #self.pix_mm_width= idx_pix_width
        

            self.frame_idx = self.frame_idx + 1

            
            res_img, s, Number_Defect, Number_of_Critical_Defect, falge_laser= defect_detection(
                    self.frame_idx, img,idx_gradient_number,idx_pix_length, idx_pix_width,idx_TEAR_DEPTH,idx_TEAR_GRADIENT_SIZE,idx_MAX_ERROR,idx_Depth_Critical,idx_Width_critical,idx_Lenght_Critical,idx_Depth_not_Critical,idx_Width_not_critical,idx_Lenght_not_Critical,idx_Depth_not_Critical_Max,idx_Width_not_critical_Max,idx_Lenght_not_Critical_Max,self.defect_tracker
                )
            
            if falge_laser :
                    styles_Live_Laser = { "Laser": "background-color:rgb(47, 140, 68)"}
                    self.ui_live.set_style_laser(styles_Live_Laser)

                    styles_Live = {
                            "Not_Critical_live_view": "background-color:rgb(219, 219, 219)",
                            "Critical_live_view": "background-color:rgb(219, 219, 219) ",
                            "Normal_live_view": "background-color:rgb(47, 140, 68)",
                        }
                    # self.ui_live.set_style_information(styles_Live)

                    if s != None and self.frame_idx % self.refresh_rate == 0:
                            infoes_Live = {
                                    "Length": "{:.2f}".format(float(s[3] * self.pix_mm_length))
                                    + " "
                                    + "mm",
                                    "Width": "{:.2f}".format(float(s[2] * self.pix_mm_width))
                                    + " "
                                    + "mm",
                                    "Depth": "{:.2f}".format(float(s[4])*0.34) + " " + "mm",
                                    #"Depth": "{:.2f}".format(float(max_depth)) + " " + "mm",
                                    "Total_Number_Defect": str(Number_Defect),
                                    "Total_Number_Critical_defect": str(Number_of_Critical_Defect),
                                }
                            self.ui_live.set_general_information(infoes_Live)
                            #print(max_depth)

                            if float(s[4]) > idx_Depth_Critical and float(s[2] * self.pix_mm_width) > idx_Width_critical and  float(s[3] * self.pix_mm_length) > idx_Lenght_Critical:
                                styles_Live = {
                                    "Not_Critical_live_view": "background-color:rgb(219, 219, 219)",
                                    "Critical_live_view": "background-color:rgb(218, 0, 0) ",
                                    "Normal_live_view": "background-color:rgb(219, 219, 219)",
                                }
                                # self.ui_live.set_style_information(styles_Live)


                            elif float(s[4]) > idx_Depth_not_Critical and float(s[4]) < idx_Depth_not_Critical_Max and float(s[2] * self.pix_mm_width) > idx_Width_not_critical  and float(s[2] * self.pix_mm_width) < idx_Width_not_critical_Max  and float(s[3] * self.pix_mm_length) > idx_Lenght_not_Critical and float(s[3] * self.pix_mm_length) < idx_Lenght_not_Critical_Max:
                                
                                    styles_Live = {
                                        "Not_Critical_live_view": "background-color:rgb(213, 213, 0)",
                                        "Critical_live_view": "background-color:rgb(219, 219, 219) ",
                                        "Normal_live_view": "background-color:rgb(219, 219, 219)",
                                    }
                                    # self.ui_live.set_style_information(styles_Live)


                    if self.frame_idx % self.refresh_rate == 0: 
                        self.show_image(res_img)

            else:
                    styles_Live_Laser = { "Laser": "background-color:rgb(218, 0, 0)"}
                    self.ui_live.set_style_laser(styles_Live_Laser)




        else :
            print("error in connection")

        #t1= t1 - time.time()
       # print(t1)


    def set_initial_param_calibration(self, param_cal):      
        self.set_calibration_parms_API(param_cal)
      
       

    def set_param_calibration(self, param_cal):   
        self.set_calibration_parms_API(param_cal)
      
      
    def set_initial_param_camera(self, param_cam):   
        self.set_camera_parms_API(param_cam)
       

    def set_param_camera(self, param_cam):  
       self.set_camera_parms_API(param_cam)


    def set_param_algorithm(self, param_algorithm):  
       self.set_algorithm_parms_API( param_algorithm)
       #print("change the param_algorithm")
       #print(param_algorithm)

    def set_initial_param_algorithm(self, param_algorithm):   
        self.set_algorithm_parms_API(param_algorithm)
        #print("initial param_algorithm")
        #print(param_algorithm)
       


    def set_calibration_parms_API(self, example_dict): 
        for name, value in example_dict.items():
            self.parms_calibration_liveView[name]=example_dict[name]
       
    def set_camera_parms_API(self, example_dict):   
        for name, value in example_dict.items():
            self.parms_camera_liveView[name]=example_dict[name]


    def set_algorithm_parms_API(self, example_dict):   
        for name, value in example_dict.items():
            self.parms_algorithm_liveView[name]=example_dict[name]

        ###################   self.camera.Parms.set_exposureTime(self.parms_camera_liveView["Exposure"])     ###################  for getting image from  camera
        ###############      self.camera.Parms.set_gain(self.parms_camera_liveView["Gain"])                    ###################  for getting image from  camera
         

    def show_farme(self):  ###################  for getting image from folder
        self.ui_live.disable_live()
        idx=self.parms_camera_liveView["Exposure"]
        image_path = "Part6"
       
        for frame_idx, fname in enumerate(os.listdir(image_path)):
            res_img, s, Number_Defect, Number_of_Critical_Defect,max_depth = defect_detection(
                frame_idx, fname,idx,self.defect_tracker
            )
            #print(max_depth)
            styles_Live = {
                "Not_Critical_live_view": "background-color:rgb(219, 219, 219)",
                "Critical_live_view": "background-color:rgb(219, 219, 219) ",
                "Normal_live_view": "background-color:rgb(47, 140, 68)",
            }
            self.ui_live.set_style_information(styles_Live)

            if s != None:
                infoes_Live = {
                        "Length": "{:.2f}".format(float(s[3] * self.pix_mm_length))
                        + " "
                        + "mm",
                        "Width": "{:.2f}".format(float(s[2] * self.pix_mm_width))
                        + " "
                        + "mm",
                        "Depth": "{:.2f}".format(float(s[4])) + " " + "mm",
                        #"Depth": "{:.2f}".format(float(max_depth)) + " " + "mm",
                        "Total_Number_Defect": str(Number_Defect),
                        "Total_Number_Critical_defect": str(Number_of_Critical_Defect),
                    }
                self.ui_live.set_general_information(infoes_Live)
                #print(max_depth)
                if float(s[4]) > 20:
                        styles_Live = {
                            "Not_Critical_live_view": "background-color:rgb(219, 219, 219)",
                            "Critical_live_view": "background-color:rgb(218, 0, 0) ",
                            "Normal_live_view": "background-color:rgb(219, 219, 219)",
                        }
                        self.ui_live.set_style_information(styles_Live)

                else:
                        styles_Live = {
                            "Not_Critical_live_view": "background-color:rgb(213, 213, 0)",
                            "Critical_live_view": "background-color:rgb(219, 219, 219) ",
                            "Normal_live_view": "background-color:rgb(219, 219, 219)",
                        }
                        self.ui_live.set_style_information(styles_Live)

            #"background-color:rgb(219, 219, 219); border-radius : 50; border : 2px solid black"
            self.show_image(res_img)
            cv2.waitKey(1)
