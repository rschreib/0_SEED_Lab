######################################
#
# Name: Intro to OpenCV Part 6
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Reads in a saved image, converts
#       it to grayscale, and the perfoms a
#       gaussian blur ontop of it.
#
######################################

import cv2
import numpy as np

img = cv2.imread('morphed_colors.jpg',0)
cv2.imshow('Original',img)

gaus = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Blurred',gaus)

cv2.imwrite('blurred_colors.jpg',gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
