# import json

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
# path = 'defect_split/89_8.json'
# # parse x:
# # y = json.loads(path)
# with open(path) as jfile:
#     file = json.load(jfile)
# # the result is a Python dictionary:
# print(file)
import cv2
a=cv2.imread('D:/Newfolder3\Basler_a2A3840-45ucBAS__40079306__20221128_192813593_0177.tiff')
print(a.shape)
cv2.imshow('a',a)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
# cv2.resizeWindow("output", 400, 300)              # Resize window to specified dimensions
# im = cv2.imread("earth.jpg")                        # Read image
cv2.imshow("output", a)  
cv2.waitKey(0)