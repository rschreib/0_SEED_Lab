from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

if __name__ == '__main__':
 
  # fileName = raw_input("File Name:")
   camera = PiCamera()
   rawCapture = PiRGBArray(camera)
   camera.hflip = True
   camera.vflip = True

 
   # allow the camera to warmup
   time.sleep(0.1)
 
   # grab an image from the camera
   print "Capturing Image..."
   try:
      camera.capture(rawCapture, format="bgr")
      image = rawCapture.array
   except:
      print "Failed to capture"
 
   # display the image on screen and wait for a keypress
   try:
      cv2.imshow("Image", image)
   except Exception, e:
      print e

   # save the image to the disk
   print "Saving image"
   try:
      cv2.imwrite('image.jpg', image)
   except:
      print "Couldn't save "
      pass
   
   cv2.waitKey(0)
   cv2.destroyAllWindows()
