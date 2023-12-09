import cv2
import numpy as np
# from utils.Defect2 import getDate
from datetime import date
import jdatetime


PATH_of_SAVE_IMAGE="Detection/image6/imagess_"


class Defect:
    DECIMAL = 2

    def __init__(self, cnt, image, depth_image, w_px2mm=1, h_px2mm=1, d_px2mm=1) -> None:
        self.cnt = cnt

        self.w_px2mm = w_px2mm
        self.h_px2mm = h_px2mm
        self.d_px2mm = d_px2mm

        self.crop_depth_image(depth_image, image)

    def crop_depth_image(self, depth_image, image):
        x, y, w, h = cv2.boundingRect(self.cnt)
        self.defect_depth_img = depth_image [max(y, 0) : y + h, x : x + w].copy()
        self.defect_img = image[max(y, 0) : y + h, x : x + w].copy()


        self.mean_depth = np.abs(self.defect_depth_img[self.defect_depth_img > 0]).mean()
        self.max_depth = np.abs(self.defect_depth_img).max()
        self.width = w 
        self.height = h

        self.width_mm = np.round(self.width * self.w_px2mm, self.DECIMAL )
        self.height_mm = np.round(self.height * self.h_px2mm, self.DECIMAL )
        self.mean_depth_mm = np.round(self.mean_depth * self.d_px2mm, self.DECIMAL )
        self.max_depth_mm = np.round(self.max_depth * self.d_px2mm, self.DECIMAL )

    
    def get_sizes(self,):
        return self.width * self.w_px2mm, self.height * self.h_px2mm, self.max_depth * self.d_px2mm









class defectTracker:
    def __init__(self, min_g_thresh, step_per_line, db_Report) -> None:
        self.min_g_thresh = min_g_thresh
        self.step_per_line = step_per_line

        self.complete_defects:list[Defect] = (
            []
        )  # This list is used to store the complete_defect_cnt
        self.inprogress_defects_cnts2 = (
            []
        )  # This list is used to store the inprogress_defect_cnt
        self.inprogress_defects_cnts = (
            []
        )  # This list is used to store the inprogress_defect_cnt

        ###############   add by myself  ############
        self.total_complete_defects = []
        self.total_depth = []
        self.critical_flage = []
        self.number_of_defect = 0
        self.number_of_critical_defect = 0
        self.total_area_of_defect = 0
        self.step = 2
        #######self.pix_mm_depth = 0.4
        self.pix_mm_depth = 0.34
        # self.pix_mm_width = 140 / 640
        self.pix_mm_width = (140 / 590) *3.2
        self.CONVAYER_SPEED = 120  # mm/s
        ######self.pix_mm_length = self.step * self.CONVAYER_SPEED / 1000
        self.pix_mm_length = (self.step * self.CONVAYER_SPEED / 400 ) * 1.4 ############## 750
        self.db_Report = db_Report
        self.max_depth=0

    def refresh(self, img, depth_img, pix_length, pix_width,Critical_Depth1,Critical_Width,Critical_Lenght,not_Critical_Depth1,not_Critical_Width,not_Critical_Lenght,not_Critical_Depth1_Max,not_Critical_Width_Max,not_Critical_Lenght_Max):
       
        self.pix_mm_width= pix_width
        self.pix_mm_length=pix_length


        h_img, w_img = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh_img = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        thresh_img = cv2.erode(thresh_img, np.ones((3, 3)), iterations=1)
        thresh_img = cv2.dilate(thresh_img, np.ones((3, 3)), iterations=4)
        thresh_img = cv2.erode(thresh_img, np.ones((3, 3)), iterations=3)

        not_remove_cnts = []
        for defect in self.complete_defects:
            defect.cnt[:, 0, 1] -= self.step_per_line
            if np.max(defect.cnt[:, 0, 1]) <= 0:
                pass
            else:
                not_remove_cnts.append(defect)

        self.complete_defects = not_remove_cnts
        cnts = list(map( lambda x:x.cnt, self.complete_defects))
        cv2.drawContours(
            thresh_img, cnts, -1, color=0, thickness=-1
        )
        contours, _ = cv2.findContours(
            thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        self.inprogress_defects_cnts = []
        self.max_depth=0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 300:  # or perimeter > 100:   # filter the area of the defect
                critical_flage_id = 2
                ######### I changed this part
                ####if area > 300:  # or perimeter > 100:   # filter the area of the defect
                # print("area of defect")
                # print(area)
                x, y, w, h = cv2.boundingRect(cnt)

                if (
                    y + h < h_img - self.min_g_thresh
                ):  # if the defect is completed, then we add it to complete_defects list
                    # {"bbox": (x, y, w, h), "cnt": cnt}
                    defect = Defect(cnt, image=img,  depth_image=depth_img, w_px2mm=pix_width, h_px2mm=pix_length, d_px2mm=0.34)
                    self.complete_defects.append(defect)
                    #self.total_complete_defects.append(cnt)

                    # self.total_area_of_defect = (
                    #     cv2.contourArea(cnt) * self.pix_mm_length * self.pix_mm_width
                    # ) + self.total_area_of_defect
                    #w_mm = w * self.pix_mm_width
                    #h_mm = h * self.pix_mm_length
                    #defect_roi = depth_img[max(y, 0) : y + h, x : x + w]
                    #roi = img[y : y + h, x : x + w]
                    # cv2.imshow("img", roi)

                    self.total_depth.append(
                        abs(defect.max_depth_mm)
                    )  # Find the depth of the defect

                    if abs(defect.max_depth_mm) > Critical_Depth1  and defect.width_mm > Critical_Width   and defect.height_mm > Critical_Lenght :


                        self.number_of_critical_defect = (
                            self.number_of_critical_defect + 1
                        )
                        critical_flage_id = 1
                        self.critical_flage.append(
                            1
                        )  
 
                    else :
                        if not_Critical_Depth1 < abs(defect.max_depth_mm)  < not_Critical_Depth1_Max :
                         if  defect.width_mm > not_Critical_Width  and  defect.width_mm < not_Critical_Width_Max :
                               if  defect.height_mm > not_Critical_Lenght  and  defect.height_mm < not_Critical_Lenght_Max:         
                         # if abs(defect_roi).max()  >  not_Critical_Depth1  and  w_mm > not_Critical_Width   and  h_mm > not_Critical_Lenght:
                                    critical_flage_id = 0
                                    self.critical_flage.append(
                                                    0
                                    )  # If defect is not-critical, the flage is set to 0
                        else :    
                            critical_flage_id = 2  
                            self.number_of_defect = self.number_of_defect + 1  
                    # if len (self.total_complete_defects)> 0:
                    # print("self.complete_defects")
                    # print(len(self.total_complete_defects))
                    if critical_flage_id == 0 or critical_flage_id == 1 :
                       # print("self.number_of_defect")
                        #print(self.number_of_defect )
                       
                        ###str_date = self.getDate_of_system()
                        #str_date = date.today().strftime('%Y/%m/%d')    # This is used for getting the date and time in normal format
                        str_date = date.today().strftime('%Y/%#m/%#d')   # This is used for getting the date and time in decimal format
                        records=self.db_Report.search_Total()
                        if len(records) < 20 :
                            path = PATH_of_SAVE_IMAGE + str(self.number_of_defect) + ".jpg"
                            cv2.imwrite(
                                PATH_of_SAVE_IMAGE + str(self.number_of_defect) + ".jpg",
                                defect.defect_img,
                            )
                            self.db_Report.add_record(
                                (
                                    defect.height_mm,
                                    defect.max_depth_mm,
                                    defect.width_mm,
                                    str_date,
                                    critical_flage_id,
                                    path,
                                ),
                            )
                        self.number_of_defect = self.number_of_defect + 1
                else:
                    defect = Defect(cnt, image=img,  depth_image=depth_img, w_px2mm=pix_width, h_px2mm=pix_length, d_px2mm=.34)
                    #self.complete_defects.append(defect)
                    self.inprogress_defects_cnts.append(defect)
                   

            else:  # or perimeter > 100:
                self.inprogress_defects_cnts2.append(cnt)
               
        return self.max_depth
        

    # def get_defect_infoes(self, depth_img, img):
    #     h_img, w_img = img.shape[:2]
    #     all_cnts = self.inprogress_defects_cnts + self.complete_defects
    #     for cnt in all_cnts:
    #         x, y, w, h = cv2.boundingRect(cnt)
    #         if y + h < h_img - self.min_g_thresh:
    #             # if y + h < h_img - 30:
    #             # print(self.min_g_thresh)
    #             w_mm = w * self.pix_mm_width
    #             h_mm = h * self.pix_mm_length
    #             defect_roi = depth_img[max(y, 0) : y + h, x : x + w]
    #             mean_depth_mm = defect_roi[abs(defect_roi) > 0].mean()
    #             # print(abs(defect_roi).max())
    #             return abs(defect_roi).max()

    #  return res

    def draw(self, img,depth_img, color=(0, 0, 255), thickness=1):
        res = img.copy()
        res = cv2.blur(res, (3, 3))
        all_cnts = self.inprogress_defects_cnts + self.complete_defects
        #all_cnts2 = self.inprogress_defects_cnts2
        h_img, w_img = img.shape[:2]
        for defect in self.complete_defects+self.inprogress_defects_cnts:
            x, y, w, h = cv2.boundingRect(defect.cnt)
            

            # if y + h < h_img - self.min_g_thresh:
            #     depth_pr = self.total_depth[self.function_number_of_defect() - 1]

            # else:
            #     defect_roi = depth_img[
            #         max(y, 0) : y + h, x : x + w
            #     ]  # find the location of the defect
            #     depth_pr = abs(defect_roi).max()
            #     depth_pr=0

            # rand_color = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)
            cv2.rectangle(res, (x, y), (x + w, y + h), color=color, thickness=thickness)
            cv2.putText(
                res,
                #str(w)+ str("-") +str(h)+str("-")+str(depth_pr),
                str(defect.max_depth_mm),
                (x, y + 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )
            defect_roi = img[y : y + h, x : x + w]
            #mean_intensity = defect_roi[defect_roi > 0].mean()


       ## for cnt in all_cnts2:
       ##      x, y, w, h = cv2.boundingRect(cnt)
            # Rand_color = np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)
       ##     cv2.rectangle(res, (x, y), (x + w, y + h), color=(0, 0, 0), thickness=-1)

        return res

    def function_return_complete_defects(self):
        return self.complete_defects

    def function_return_critical_flage(self):
        return self.critical_flage

    def function_return_total_depth(self):
        return self.total_depth

    def function_inprogress_defects_cnts(self):
        return self.inprogress_defects_cnts

    def function_number_of_defect(self):
        return self.number_of_defect

    def function_number_of_critical_defect(self):
        return self.number_of_critical_defect

    def function_total_area_of_defect(self):
        return self.total_area_of_defect

    def function_total_complete_defects(self):
        return self.total_complete_defects

    def function_inprogress_defects_cnts_x_y_w_h(self, depth_img, img):
        # res = img2.copy()
        # res = cv2.blur(res, (5, 5))
        h_img, w_img = img.shape[:2]
        all_cnts = self.inprogress_defects_cnts + self.complete_defects
        # all_cnts2 = self.inprogress_defects_cnts

        depth_pr = 0
        for defect in self.complete_defects:
            x, y, w, h = cv2.boundingRect(defect.cnt)

            # if y + h < h_img - self.min_g_thresh:
            #     depth_pr = self.total_depth[self.function_number_of_defect() - 1]

            # else:
            #     defect_roi = depth_img[
            #         max(y, 0) : y + h, x : x + w
            #     ]  # find the location of the defect
            #     depth_pr = abs(defect_roi).max()
            #     depth_pr=0


            return x, y, defect.width_mm, defect.height_mm, defect.max_depth

    def getDate_of_system(self):
        this_year = date.today().year
        this_month = date.today().month
        this_day = date.today().day
        str_date = jdatetime.date.fromgregorian(
            day=this_day, month=this_month, year=this_year
        )
        return str_date
