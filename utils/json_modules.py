import json


class Annotation:
    def read(self, path):
        with open(path) as jfile:
            file = json.load(jfile)
        return file

    def write(self, path):
        with open(path, "w") as f:
            json.dump(self.annotation, f)

    def __init__(self):
        self.annotation = {}

    # --------------------------------------------------------
    #
    # --------------------------------------------------------
    def set_all(self, details):

        self.set_defects_pixels_list(details["defects_pixels_list"])
        self.set_defects_depth_list(details["defects_depth_list"])
        self.set_defects_type_list(details["defects_type_list"])
        self.set_defects_postion_list(details["defects_postion_list"])

    def set_defects_pixels_list(self, defects_pixels_list):
        self.annotation["defects_pixels_list"] = defects_pixels_list

    def set_defects_depth_list(self, defects_depth_list):
        self.annotation["defects_depth_list"] = defects_depth_list

    def set_defects_type_list(self, defects_type_list):
        self.annotation["defects_type_list"] = defects_type_list

    def set_defects_postion_list(self, defects_postion_list):
        self.annotation["defects_postion_list"] = defects_postion_list

    #     self.set_date(details["date"])
    #     self.set_location(details["loc"])
    #     self.set_area(details["area"])
    #     self.set_type(details["type"])
    #     self.set_p(details["perimeter"])
    #     self.set_depth(details["depth"])

    # def set_date(self, name):
    #     self.annotation["date"] = name

    # def set_location(self, location):
    #     self.annotation["loc"] = location

    # def set_area(self, area):
    #     self.annotation["area"] = area

    # def set_type(self, type_):
    #     self.annotation["type"] = type_

    # def set_p(self, p):
    #     self.annotation["perimeter"] = p

    # def set_depth(self, depth):
    #     self.annotation["depth"] = depth


if __name__ == "__main__":
    a = Annotation()
    # default_details = {
    #     "date": "-",
    #     "loc": "-",
    #     "area": "-",
    #     "type": "-",
    #     "perimeter": "-",
    #     "depth": "-",
    # }
    default_details = {
        "defects_pixels_list": [],
        "defects_depth_list": [],
        "defects_type_list": [],
        "defects_postion_list": [],
    }
    a.set_all(default_details)
    a.write("a.json")
