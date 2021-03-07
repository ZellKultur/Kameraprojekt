from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range (5):
    camera.start_preview()
    sleep(2)
    camera.capture('Home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    sleep(10)
