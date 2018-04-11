######################################
#
# Name: Intro to OpenCV Part 1
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Takes a picture. Prompts user
#       For file name to save picture. Then
#       the user can click on the picture
#       and the RGB value for the pixel is
#       displayed.
#
######################################

import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.hflip = True
camera.vflip = True

camera.capture(rawCapture, format="bgr")
img = rawCapture.array

fileName = raw_input("File Name:")
cv2.imwrite(fileName,img)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        px = img[x,y]
        print px

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

print 'Please select a pixel'

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
