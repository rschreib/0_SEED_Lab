######################################
#
# Name: Intro to OpenCV Part 2
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Takes 3 pictures and isolates
#       red, blue, green and yellow. shows
#       the isolated pictures.
#
######################################

import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
rawCapture1 = PiRGBArray(camera)
rawCapture2 = PiRGBArray(camera)
rawCapture3 = PiRGBArray(camera)

raw_input('Press any key to take first picture')


camera.capture(rawCapture1, format="bgr")
img1 = rawCapture1.array
img1 = cv2.resize(img1,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

raw_input('Press any key to take second picture')

camera.capture(rawCapture2, format="bgr")
img2 = rawCapture2.array
img2 = cv2.resize(img2,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

raw_input('Press any key to take third picture')

camera.capture(rawCapture3, format="bgr")
img3 = rawCapture3.array
img3 = cv2.resize(img3,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)
hsv3 = cv2.cvtColor(img3,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,120])
upper_blue = np.array([120,255,255])
lower_red_l  = np.array([0,200,100])
upper_red_l  = np.array([20,255,255])
lower_red_u = np.array([165,200,100])
upper_red_u = np.array([180,255,255])
lower_green = np.array([50,200,50])
upper_green = np.array([70,255,255])
lower_yellow = np.array([10,200,100])
upper_yellow = np.array([30,255,255])

mask1 = cv2.inRange(hsv1,lower_blue,upper_blue)
mask2 = cv2.inRange(hsv1,lower_red_l,upper_red_l)
mask3 = cv2.inRange(hsv1,lower_green,upper_green)
mask4 = cv2.inRange(hsv1,lower_yellow,upper_yellow)
mask5 = cv2.inRange(hsv1,lower_red_u,upper_red_u)
mask  = cv2.bitwise_or(mask1,mask2)
mask  = cv2.bitwise_or(mask,mask3)
mask  = cv2.bitwise_or(mask,mask4)
mask = cv2.bitwise_or(mask,mask5)
res1 = cv2.bitwise_and(img1,img1,mask = mask)
cv2.imshow('res1',res1)

#cv2.imshow('maskBlue',mask1)

mask1 = cv2.inRange(hsv2,lower_blue,upper_blue)
mask2 = cv2.inRange(hsv2,lower_red_l,upper_red_l)
mask3 = cv2.inRange(hsv2,lower_green,upper_green)
mask4 = cv2.inRange(hsv2,lower_yellow,upper_yellow)
mask5 = cv2.inRange(hsv2,lower_red_u,upper_red_u)
mask  = cv2.bitwise_or(mask1,mask2)
mask  = cv2.bitwise_or(mask,mask3)
mask  = cv2.bitwise_or(mask,mask4)
mask = cv2.bitwise_or(mask,mask5)
res2 = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('res2',res2)

mask1 = cv2.inRange(hsv3,lower_blue,upper_blue)
mask2 = cv2.inRange(hsv3,lower_red_l,upper_red_l)
mask3 = cv2.inRange(hsv3,lower_green,upper_green)
mask4 = cv2.inRange(hsv3,lower_yellow,upper_yellow)
mask5 = cv2.inRange(hsv3,lower_red_u,upper_red_u)
mask  = cv2.bitwise_or(mask1,mask2)
mask  = cv2.bitwise_or(mask,mask3)
mask  = cv2.bitwise_or(mask,mask4)
mask = cv2.bitwise_or(mask,mask5)
res3 = cv2.bitwise_and(img3,img3,mask = mask)
cv2.imshow('res3',res3)

cv2.imwrite('colors_1.jpg',res1)
cv2.imwrite('colors_2.jpg',res2)
cv2.imwrite('colors_3.jpg',res3)

cv2.waitKey(0)
cv2.destroyAllWindows()

