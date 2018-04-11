######################################
#
# Name: Intro to OpenCV Part 5
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: loads in a saved image and
#       uses OpenCV tools to morph the image
#
######################################

import cv2
import numpy as np

img = cv2.imread('colors_1.jpg')
cv2.imshow('Original',img)
kernal = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernal,iterations = 1)

dilation = cv2.dilate(erosion,kernal,iterations = 1)

opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernal)

closing = cv2.morphologyEx(opening,cv2.MORPH_OPEN,kernal)
cv2.imshow('Final',closing)

cv2.imwrite('morphed_colors.jpg',opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
