import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob

camera = PiCamera()
camera.start_preview()
time.sleep(2)
