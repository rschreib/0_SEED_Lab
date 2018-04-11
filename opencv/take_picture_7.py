######################################
#
# Name: Intro to OpenCV Part 7
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Reads in an image, and detects
#       the blobs in the image, and then
#       removes then roughly cirlces the blobs.
#
######################################

import cv2
import numpy as np
import glob

img = cv2.imread('blurred_colors.jpg')
cv2.imshow('Original',img)

lower = np.array([10,10,10])
upper = np.array([255,255,255])

mask = cv2.inRange(img,lower,upper)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10;
params.maxThreshold = 200;

params.filterByArea = False
params.minArea = 5

params.filterByColor= False
params.blobColor = 200

params.filterByCircularity = False
params.minCircularity = 0.1

params.filterByConvexity = False
params.minConvexity = 0.5

params.filterByInertia = False
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector(params)

keypoints = detector.detect(mask)
for kp in keypoints:
    cv2.circle(img,(int(kp.pt[0]), int(kp.pt[1])), int(kp.size),(0,0,255))

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
