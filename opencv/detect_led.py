import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob

def detect():
    
    run = False

    camera = PiCamera(resolution=(640,360))
    rawCapture = PiRGBArray(camera)

    camera.iso = 300
    camera.shutter_speed = 3000

    camera.capture(rawCapture, format="bgr")
    img = rawCapture.array
    cv2.imwrite('test2.jpg',img)

    #img = cv2.resize(img,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Both
    #lower = np.array([0,230,25])
    #upper = np.array([180,255,255])

    #green
    lower_green = np.array([40,230,23])
    upper_green = np.array([100, 255,255])

    #Red
    lower_red_u = np.array([110, 230, 55])
    upper_red_u = np.array([180,255,255])
    lower_red_l = np.array([0,230,50])
    upper_red_l = np.array([1,255,255])

    mask_green = cv2.inRange(hsv,lower_green,upper_green)
    mask_red_u = cv2.inRange(hsv,lower_red_u,upper_red_u)
    mask_red_l = cv2.inRange(hsv,lower_red_u,upper_red_u)
    mask_red = cv2.bitwise_or(mask_red_l,mask_red_u)

    kernal_green = np.ones((5,5),np.uint8)
    mask_green = cv2.erode(mask_green,kernal_green,iterations = 1)
    mask_green = cv2.dilate(mask_green,kernal_green,iterations = 1)
    mask_green = cv2.morphologyEx(mask_green,cv2.MORPH_CLOSE,kernal_green)

    kernal_red = np.ones((5,5),np.uint8)
    mask_red = cv2.erode(mask_red,kernal_red,iterations = 1)
    mask_red = cv2.dilate(mask_red,kernal_red,iterations = 1)
    mask_red = cv2.morphologyEx(mask_red,cv2.MORPH_CLOSE,kernal_red)

    res_green = cv2.bitwise_and(img,img,mask=mask_green)
    res_gred = cv2.bitwise_and(img,img,mask=mask_red)

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 20;
    params.maxThreshold = 200;

    params.filterByArea = False
    params.minArea = 1

    params.filterByColor= False
    params.blobColor = 200

    params.filterByCircularity = False
    params.minCircularity = 0.1

    params.filterByConvexity = False
    params.minConvexity = 0.5

    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    detector = cv2.SimpleBlobDetector(params)

    keypoints_green = detector.detect(mask_green)
    keypoints_red = detector.detect(mask_red)

    if len(keypoints_green)>0 and len(keypoints_red)==0 and not run:
        run = True
    elif len(keypoints_green) == 0 and len(keypoints_red)>0 and run:
        run = False
    

    cv2.imshow('Image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #camera.release()
    return run

f = detect()
print f
