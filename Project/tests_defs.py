from picamera import PiCamera
from bounds_test import *

resX = 1440
resY = 816

camera = PiCamera(resolution=(resX,resY))
camera.iso = 50
camera.shutter_speed = 1500

f = 'led02.jpg'

keypoints = take_picture(camera, f)

leds = find_beacons(keypoints)

for l in leds:
    print '###########'
    for k in l:
        print '     ', k
