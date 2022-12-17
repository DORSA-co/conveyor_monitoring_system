import json


class Annotation():
    
    def read(self, path):
        with open(path) as jfile:
            file = json.load(jfile)
        return file
        

    def write(self,path):    
        with open(path, 'w') as f:
            json.dump(self.annotation,f)

    def __init__(self,):
        self.annotation = {}

    #--------------------------------------------------------
    #
    #--------------------------------------------------------
    def set_all(self,details):
        self.set_date(details['date'])
        self.set_location(details['loc'])
        self.set_area(details['area'])
        self.set_type(details['type'])
        self.set_p(details['p'])
        self.set_depth(details['depth'])

    def set_date(self, name):
        self.annotation['date'] = name

    def set_location(self, location):
        self.annotation['loc'] = location

    def set_area(self, area):
        self.annotation['area'] = area

    def set_type(self,type_):
        self.annotation['type'] = type_

    def set_p(self, p):
        self.annotation['p'] = p

    def set_depth(self, depth):
        self.annotation['depth'] = depth


if __name__=='__main__':
    a=Annotation()
    default_details = {"date": "-","loc": "-", "area": "-", "type": "-", "p": "-", "depth": "-"}
    a.set_all(default_details)
    a.write('a.json')