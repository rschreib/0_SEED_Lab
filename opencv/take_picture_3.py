######################################
#
# Name: Intro to OpenCV Part 2
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Takes a picture and then
#       isolates the color yellow.
#       shows three images: the original,
#       the mask of yellow, and the original
#       with the mask on top.
#
######################################

import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
rawCapture = PiRGBArray(camera)

camera.capture(rawCapture, format="bgr")
img = rawCapture.array
cv2.imwrite('colors.jpg',img)

img2 = img
img = cv2.resize(img,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([50,200,50])
upper = np.array([70,255,255])

mask = cv2.inRange(hsv,lower,upper)

res = cv2.bitwise_and(img,img, mask = mask)

cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
