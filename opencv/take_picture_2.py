######################################
#
# Name: Intro to OpenCV Part 2
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Reads in a saved picture and
#       resizes the picture in half.
#
######################################

import cv2
import numpy as np

img = cv2.imread('image.jpg')

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

res = cv2.resize(img,None,fx=.5,fy=.5,interpolation = cv2.INTER_CUBIC)

cv2.imshow('Image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
