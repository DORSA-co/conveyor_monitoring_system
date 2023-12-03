from PyQt5 import QtGui
import time

class LiveView_UI(Common_Function_UI):

    """Description of the code

    :param
    """

    def __init__(self, ui):
        """Description of the code"""

        self.ui = ui
        self.general_information_live = {
            "Length": self.ui.Length,
            "Width": self.ui.Width,
            "Depth": self.ui.Depth,
            "Total_Number_Defect": self.ui.Total_Number_Defect,
            "Total_Number_Critical_defect": self.ui.Total_Number_Critical_defect,
        }
        self.style_information_live = {
            "Not_Critical_live_view": self.ui.Not_Critical_live_view,
            "Critical_live_view": self.ui.Critical_live_view,
            "Normal_live_view": self.ui.Normal_live_view,
        }

        self.ui.Stop_connection.setEnabled(False)
        self.ui.live.setEnabled(False)
        self.ui.Stop.setEnabled(False)
        self.camera_connection=False
        
        self.t = time.time()



    def button_connector(self,camera_connection):   # input fun for getting image from folder
        self.camera_connection=camera_connection
        self.ui.Camera_connection.clicked.connect(partial(self.connect_camera))
        self.ui.Stop_connection.clicked.connect(partial(self.disconnect_camera))
       

       # self.ui.live.clicked.connect(
       #     fun
       # )  ###################  for getting image from  folder

    def Set_fn(self, fun):
        self.fn = fun

    def Get_fn(self):
        return self.fn

    def button_connector_QTimer(self, fun):
        self.Set_fn(fun)
        self.ui.live.clicked.connect(self.button_connector_QTimer_fun)

    def button_connector_stop(self):
        
       self.ui.Stop.clicked.connect(self.stop_live)
      

    def stop_live(self):
        self.picktimer.stop()
        self.ui.live.setEnabled(True)
        self.ui.Stop.setEnabled(False)

    def button_connector_QTimer_fun(self):
        fun = self.Get_fn()
        self.picktimer = QTimer()
        #self.picktimer.setInterval(0.001)
        self.picktimer.timeout.connect(fun)
        self.picktimer.start(25)


        self.time = QTimer()
        #self.picktimer.setInterval(0.001)
        self.time.timeout.connect(self.show_time)
        self.time.start(1000)


    def show_time(self):

        print(time.time()-self.t)