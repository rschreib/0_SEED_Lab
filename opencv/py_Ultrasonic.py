######################################
#
# Name: Mini-Project
#
# Created by: Dristen 
#
# Assisted by: Documentation on Canvas
#
# Purpose: Tells the motor if to run and
#       how quickly
#
######################################

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import struct
import smbus
import time
import Adafruit_CharLCD as LCD
from func_detect_led import detect
import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import glob

# Camera settup for taking pictures of the
# LEDs
camera = PiCamera(resolution=(640,360))     
mode = False

# Initialize LCD
lcd = LCD.Adafruit_CharLCDPlate()

# Set bus mode 
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

while True:
    try:
        mode = detect(camera, mode)
        print [int(mode)]
        bus.write_i2c_block_data(address, 0, [int(mode)])  
        time.sleep(0.1)
        data = bus.read_i2c_block_data(address, 0, 3)
    except:
        continue
    time.sleep(.1)
    if (data[0] > 100):
        continue
    else:
        print(data)
        speed = data[1] + (0.01*data[2])
        lcd.message("Speed:" + str(speed) + " rad/s")
        time.sleep(1)
        lcd.clear()
    
    
