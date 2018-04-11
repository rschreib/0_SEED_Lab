from detect_led import detect
import time
import os

d = detect()
os.system('echo %i > data.txt' % (d))




