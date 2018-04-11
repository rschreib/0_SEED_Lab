from func_detect_led import detect
from picamera import PiCamera
import warnings
warnings.filterwarnings('ignore')

camera = PiCamera(resolution=(640,360))     
run = False

for i in range(10):
    try:
        run = detect(camera,run)
        print i, ':', run
    except:
        pass

