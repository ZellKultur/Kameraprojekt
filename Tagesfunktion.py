from picamera import PiCamera
import time
import datetime

camera = PiCamera()

for i in range (96):
    start = time.time()                                                                                              #starpunkt Messung mit Uhrzeit
    camera.start_preview()
    time.sleep(2)
    camera.capture('/home/pi/Desktop/Testbilder/image%s.jpg' % str(datetime.datetime.now().isoformat()))
    camera.stop_preview()
    time_needed = time.time() - start                                                                                # wieviel Zeit wurde benötigt? - wird abgezogen
    time.sleep(10 - time_needed)                                                                                     # benötigte Zeit von Loop abziehen
