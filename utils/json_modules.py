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

    def set_all(self, details):
        self.set_defects_boundbox_list(details["defects_boundbox_list"])
        self.set_defects_area_list(details["defects_area_list"])
        self.set_defects_depth_list(details["defects_depth_list"])
        self.set_defects_type_list(details["defects_type_list"])
        # self.set_defects_ypixel_list(details["defects_ypixel_list"])
        # self.set_defects_xpixel_list(details["defects_xpixel_list"])
        self.set_defects_position_list(details["defects_position_list"])

    def set_defects_boundbox_list(self, defects_boundbox_list):
        # self.annotation["defects_boundbox_list"] = []
        self.annotation["defects_boundbox_list"] = defects_boundbox_list

    def set_defects_area_list(self, defects_area_list):
        # self.annotation["defects_area_list"] = []
        self.annotation["defects_area_list"] = defects_area_list

    def set_defects_depth_list(self, defects_depth_list):
        # self.annotation["defects_depth_list"] = []
        self.annotation["defects_depth_list"] = defects_depth_list

    def set_defects_type_list(self, defects_type_list):
        # self.annotation["defects_type_list"] = []
        self.annotation["defects_type_list"] = defects_type_list

    def set_defects_xpixel_list(self, defects_xpixel_list):
        # self.annotation["defects_xpixel_list"] = []
        self.annotation["defects_xpixel_list"] = defects_xpixel_list

    def set_defects_ypixel_list(self, defects_ypixel_list):
        # self.annotation["defects_ypixel_list"] = []
        self.annotation["defects_ypixel_list"] = defects_ypixel_list

    def set_defects_position_list(self, defects_position_list):
        # self.annotation["defects_position_list"] = []
        self.annotation["defects_position_list"] = defects_position_list


if __name__ == "__main__":
    a = Annotation()

    default_details = {
        "defects_boundbox_list": [(2, 4, 1, 1), (5, 2, 1, 1)],
        "defects_depth_list": [34.444, 56.3],
        "defects_type_list": ["ii", "iii"],
    }
    a.set_all(default_details)
    a.write("a.json")
    x = a.read("a.json")
    print(x)
    print(x["defects_boundbox_list"])
    print(x["defects_depth_list"])
    print(x["defects_type_list"])
