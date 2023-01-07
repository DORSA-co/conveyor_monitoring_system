from PySide6.QtWidgets import QLabel as sQLabel
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
from PySide6.QtWidgets import QVBoxLayout as sQVBoxLayout
import cv2
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from functools import partial
import json
import numpy as np
import os

n_images_per_row = 6
no_image_path = "UI/images_icon/no_image.png"  # path for a raw image (using for labels default image)
segments_info = r"segments_info"


def create_image_slider_on_ui(
    ui_obj,
    db_obj,
    frame_obj,
    prefix="defect",
    image_per_row=n_images_per_row,
    # segments=None,
    orientation='H'
):
    """this function is used to create dataset image slider on ui binary list page, this slider is used to show dataset images

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param frame_obj: ui frame object to create slider in
    :type frame_obj: _type_
    :param prefix: _description_, defaults to widjet_prefixes['perfect']
    :type prefix: _type_, optional
    :param image_per_row: n images to show on each page of slider, defaults to n_images_per_row
    :type image_per_row: _type_, int
    :return: a boolean determining if the slider is initialized
    :rtype: boolean
    """
    layout = sQHBoxLayout()
    if orientation == 'V':
        layout = sQVBoxLayout()
    # create layout
    
    eval("exec('ui_obj.%s_layout = layout')" % prefix)

    # creat and assign labels to layout
    for i in range(image_per_row):
        label = sQLabel()
        label.setScaledContents(True)
        label.setWhatsThis("")
        # assign label to UI with name
        eval("exec('ui_obj.%s_label_%s = label')" % (prefix, i))
        # add to layout
        eval("ui_obj.%s_layout" % prefix).addWidget(
            eval("ui_obj.%s_label_%s" % (prefix, i))
        )
        set_image_to_ui(
            label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
            image=None,
            no_image=True,
        )

        # doble-click event for labels
        eval("ui_obj.%s_label_%s" % (prefix, i)).mouseDoubleClickEvent = partial(
            maximize_image_on_click,
            i,
            ui_obj,
            db_obj,
            eval("ui_obj.%s_label_%s" % (prefix, i)),
        )

    # assign layout to frame
    frame_obj.setLayout(eval("ui_obj.%s_layout" % prefix))

    return True


def set_image_to_ui(label_name, image, no_image=False, mode=None):
    """this function is used to set an image on ui label using label name

    :param label_name: name if the label
    :type label_name: _type_
    :param image: image in numpy format
    :type image: numpy array
    :param no_image: a boolean determinign wheater to assign defaults raw image to label. Defaults to False., defaults to False
    :type no_image: bool, optional
    """

    if no_image:
        image = cv2.imread(no_image_path)
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    #
    h, w, ch = image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = sQImage(
        image.data, w, h, bytes_per_line, sQImage.Format_BGR888
    )
    label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))
    label_name.setStyleSheet(
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: gray;"
        "border-radius: 3px"
    )


def set_label_style(ui_obj, index, prefix, mode="normal"):

    if mode == "scanning":
        eval("ui_obj.%s_label_%s" % (prefix, index)).setStyleSheet(
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: black;"
            "border-radius: 3px"
        )
    elif mode == "defective":
        eval("ui_obj.%s_label_%s" % (prefix, index)).setStyleSheet(
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: red;"
            "border-radius: 3px"
        )
    else:
        eval("ui_obj.%s_label_%s" % (prefix, index)).setStyleSheet(
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: gray;"
            "border-radius: 3px"
        )


def update_imagesslider_on_ui(ui_obj, prevornext="False"):
    """this function is used to update classification images list on UI slider

    :param prevornext: boolean determining whether to get next/prev page, defaults to 'False'
    :type prevornext: str, optional
    """

    # next or prev on list
    if prevornext == "next":
        ui_obj.segment_image_list_next_func()

    elif prevornext == "prev":
        ui_obj.segment_image_list_prev_func()

    # get curent image list to set to UI
    (current_image_list) = ui_obj.segment_image_list.get_n_current(
        name="segment", get_annots=False
    )
    # print("current_image_list", current_image_list)
    current_annots_list = []
    # # set/update images on UI
    res = set_image_to_ui_slider_full_path(
        ui_obj=ui_obj,
        image_path_list=current_image_list,
        annot_path_list=current_annots_list,
        prefix="segment",
        image_per_row=n_images_per_row,
    )


# update slider images
def update_defect_images_on_ui(ui_obj, prevornext="False"):
    """this function is used to update classification images list on UI slider

    :param prevornext: boolean determining whether to get next/prev page, defaults to 'False'
    :type prevornext: str, optional
    """

    # next or prev on list
    if prevornext == "next":
        ui_obj.defect_image_list_next_func()
        # print("aaaa")
    # prev
    elif prevornext == "prev":
        ui_obj.defect_image_list_prev_func()

    # get curent image list to set to UI
    (current_image_list) = ui_obj.defect_image_list.get_n_current(
        name="defect", get_annots=False
    )
    # print("current_image_list", current_image_list)
    current_annots_list = []
    # # set/update images on UI
    res = set_image_to_ui_slider_full_path(
        ui_obj=ui_obj,
        image_path_list=current_image_list,
        annot_path_list=current_annots_list,
        prefix="defect",
        image_per_row=n_images_per_row,
    )


def set_image_to_ui_slider_full_path(
    ui_obj,
    image_path_list,
    annot_path_list,
    prefix="defect",
    image_per_row=n_images_per_row,
):
    """this function is used to set images on binarylist image sliders (using image full/relative pathes)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param image_path_list: image full pathes
    :type image_path_list: list of str
    :param annot_path_list: annotaions full pathes
    :type annot_path_list: list of str
    :param prefix: _description_, defaults to widjet_prefixes['perfect']
    :type prefix: _type_, optional
    :param image_per_row: n image in slider page, defaults to n_images_per_row
    :type image_per_row: int, optional
    :return: _description_
    :rtype: boolean determiing if done
    """

    # set dataset images on UI
    temp_i = 0
    for i, image_path in enumerate(image_path_list):

        # load image
        if image_path[-3:] == "jpg":
            image = cv2.imread(image_path)

            # set to UI label
            if eval("ui_obj.%s_label_%s" % (prefix, i)).isVisible() == False:
                eval("ui_obj.%s_label_%s" % (prefix, i)).setVisible(True)

            set_image_to_ui(
                label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
                image=image,
                no_image=False,
            )

            # update/set text (image url) on image label whatsthis
            whats_this_text = image_path
            try:
                eval("ui_obj.%s_label_%s" % (prefix, i)).setWhatsThis(whats_this_text)
            except:
                pass
            # set last image labels on UI as empty
            temp_i = i

    for j in range(temp_i + 1, image_per_row):
        eval("ui_obj.%s_label_%s" % (prefix, j)).setVisible(False)
        # set_image_to_ui(
        #     label_name=eval("ui_obj.%s_label_%s" % (prefix, j)),
        #     image=None,
        #     no_image=True,
        # )

    return True


# maximize image label on click (open image in a window)
def maximize_image_on_click(index, ui_obj, db_obj, label, event):
    slide_index = (ui_obj.num_frames - 1) // (
        (ui_obj.frame_pre_segment) * (ui_obj.image_pre_row)
    )
    clicked_index = (slide_index * ui_obj.image_pre_row) + index
    try:
        ui_obj.popup_window_obj.set_and_update_schematic(
            ui_obj.segment_detail_list[clicked_index], clicked_index, 5
        )
        ui_obj.popup_window_obj.show()
        path = os.path.join(
            segments_info,
            str(clicked_index),
            str(clicked_index) + ".json",
        )

        if os.path.exists(path):
            ui_obj.popup_window_obj.hint_window_obj.load_detail(
                annotation=ui_obj.segment_annotation,
                path=path,
            )

    except:
        pass
