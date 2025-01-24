import cv2
import pandas as pd
import numpy as np
import copy

img = cv2.imread("./digital_camera_photo-1080x675.jpg")
window = "Kanvas"
x_awal, y_awal = 0, 0
mouse_active = False

new_img = copy.deepcopy(img)

def clickFunc(event, x, y, flags, param):
    
    global x_awal, y_awal, new_img, mouse_active, img
        
    if event == cv2.EVENT_LBUTTONDOWN:
        x_awal, y_awal = x, y
        mouse_active = True
        
    if event == cv2.EVENT_LBUTTONUP:
        if abs(y_awal - y) > 50 and abs(x_awal - x) > 50:
            img = img[y_awal:y,x_awal:x]
        new_img = copy.deepcopy(img)
        mouse_active = False
        
    if mouse_active == True:
        new_img = copy.deepcopy(img)
        cv2.rectangle(new_img, (x_awal, y_awal), (x, y), color=(0,0,0),thickness=3)
            
trackbar_window = "resize"     
resize_img = np.ones((1,600,1)).astype(np.uint8)*255  
def on_hello(val):
    global img, new_img
    
    if val <= 100 :
        new_img = cv2.resize(img, (0, 0), fx=val*0.01, fy=val*0.01, interpolation=cv2.INTER_NEAREST)
    elif val > 100:
        new_img = cv2.resize(img, (0, 0), fx=val*0.01, fy=val*0.01, interpolation=cv2.INTER_CUBIC)
    
        
cv2.namedWindow(window)
cv2.namedWindow(trackbar_window)
cv2.setMouseCallback(window, clickFunc)
cv2.createTrackbar("resize", trackbar_window, 100, 300, on_hello)
on_hello(100)    

run = True

# Pencet "r" jika ingin mengembalikkan image yang sudah di crop
# Pencet "q" jika ingin keluar
while run:

    if cv2.waitKey(10) == ord("q"):
        run = False
    if cv2.waitKey(10) == ord("r"):
        img = cv2.imread("./digital_camera_photo-1080x675.jpg")
        new_img = copy.deepcopy(img)
        x_awal, y_awal = 0, 0
    cv2.imshow(window,new_img)
    cv2.imshow(trackbar_window, resize_img)
        
cv2.destroyAllWindows()
