from PySide6.QtWidgets import QLabel as sQLabel
from PySide6.QtWidgets import QHBoxLayout as sQHBoxLayout
import cv2
from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap
from functools import partial
import json

n_images_per_row = 6


def create_image_slider_on_ui(
    ui_obj,
    db_obj,
    frame_obj,
    prefix="defect",
    image_per_row=n_images_per_row,
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

    # try:
    # create layout
    layout = sQHBoxLayout()
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
        # assign image
        set_image_to_ui(
            label_name=eval("ui_obj.%s_label_%s" % (prefix, i)),
            image=None,
            no_image=True,
        )

        # # doble-click event for labels
        eval("ui_obj.%s_label_%s" % (prefix, i)).mouseDoubleClickEvent = partial(
            maximize_image_on_click,
            ui_obj,
            db_obj,
            eval("ui_obj.%s_label_%s" % (prefix, i)),
        )

    # assign layout to frame
    frame_obj.setLayout(eval("ui_obj.%s_layout" % prefix))

    # ui_obj.logger.create_new_log(
    #     message=texts.MESSEGES["BINARYLIST_SLIDER_build"]["en"], level=1
    # )
    return True

    # except Exception as e:
    #     ui_obj.set_warning(
    #         texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"], "binarylist", level=3
    #     )
    #     ui_obj.logger.create_new_log(
    #         message=texts.ERRORS["BUILD_BINARYLIST_SLIDER_ERROR"]["en"], level=5
    #     )
    #     return False


no_image_path = "UI/images_icon/no_image.png"  # path for a raw image (using for labels default image)


def set_image_to_ui(label_name, image, no_image=False):
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
    
    # try:
    # set dataset images on UI
    for i, image_path in enumerate(image_path_list):
        # load image
        if image_path[-3:]=='jpg':
            image = cv2.imread(image_path)

            # if image

            # set to UI label
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
            try:
                i += 1
            except:
                i = 0
    # for j in range(i, image_per_row):
    #     set_image_to_ui(
    #         label_name=eval("ui_obj.%s_label_%s" % (prefix, j)),
    #         image=None,
    #         no_image=True,
    #     )
    #     whats_this_text = image_path
    #     try:
    #         eval("ui_obj.%s_label_%s" % (prefix, j)).setWhatsThis(whats_this_text)
    #     except:
            # pass
    return True

    # except Exception as e:
    #     ui_obj.logger.create_new_log(
    #         message=texts.ERRORS["set_image_to_slider_failed"][ui_obj.language], level=5
    #     )
    #     return False


# maximize image label on click (open image in a window)
def maximize_image_on_click(ui_obj, db_obj, label, event):
    """this function is used to maximize an image lable on click (open new image viewer window)

    :param ui_obj: main ui object
    :type ui_obj: _type_
    :param db_obj: database object
    :type db_obj: _type_
    :param label: label name
    :type label: _type_
    :param event: _description_
    :type event: _type_
    """
    try:
        path = label.whatsThis()  # image path is set on its label whatsthis
    except:
        path =''
    # try:
    # path exists
    # urrent_image_list aaaa['defect_split\\9_53.jpg', 'defect_split\\9_61.jpg']
    json_details = {}
    # try:
    json_path = str(path).replace("jpg", "json")
    with open(json_path) as jfile:
        json_details = json.load(jfile)
    # except:
    #     pass
    # # some JSON:
    # x =  '{ "name":"John", "age":30, "city":"New York"}'

    # # parse x:
    # y = json.loads(x)

    # # the result is a Python dictionary:
    ui_obj.popup_window_obj.update_image_details(
        image=cv2.imread(path), details=json_details
    )
    ui_obj.popup_window_obj.show()
