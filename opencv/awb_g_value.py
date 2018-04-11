import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob

camera = PiCamera()
rawCapture = PiRGBArray(camera)

camera.iso = 1600
camera.shutter_speed = 16000
camera.start_preview()
time.sleep(3)
camera.stop_preview()
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
print g
