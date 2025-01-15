import cv2
import pandas as pd
import numpy as np
import copy

img = cv2.imread("./digital_camera_photo-1080x675.jpg")
window = "Kanvas"
x_awal, y_awal = 0, 0
mouse_active = False
rect = []


new_img = copy.deepcopy(img)

# def clickFunc(event, x, y, flags, param):
    
#     global x_awal, y_awal, new_img
    
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if x_awal == 0 and y_awal == 0:
#             x_awal, y_awal = x, y
#             new_img = new_img[y_awal:new_img.shape[0], x_awal:new_img.shape[1]]
#         else:
#             new_img = new_img[0:y, 0:x]

def clickFunc(event, x, y, flags, param):
    
    global x_awal, y_awal, new_img, mouse_active, rect, img
        
    if event == cv2.EVENT_LBUTTONDOWN:
        x_awal, y_awal = x, y
        mouse_active = True
        
    if event == cv2.EVENT_LBUTTONUP:
        img = img[y_awal:y,x_awal:x]
        new_img = copy.deepcopy(img)
        mouse_active = False
        
    if mouse_active == True:
        new_img = copy.deepcopy(img)
        cv2.rectangle(new_img, (x_awal, y_awal), (x, y), color=(0,0,0),thickness=1)
        
        

cv2.namedWindow(window)
cv2.setMouseCallback(window, clickFunc)

run = True

# Pencet "r" jika ingin mengembalikkan image yang sudah di crop
# Pencet "q" jika ingin keluar
while run:

    if cv2.waitKey(10) == ord("q"):
        run = False
    elif cv2.waitKey(10) == ord("r"):
        img = cv2.imread("./digital_camera_photo-1080x675.jpg")
        new_img = copy.deepcopy(img)
        x_awal, y_awal = 0, 0
    else:
        cv2.imshow(window,new_img)
        
cv2.destroyAllWindows()
