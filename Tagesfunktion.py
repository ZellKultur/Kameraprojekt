from picamera import PiCamera
import time
import datetime
#Kamera importieren
camera = PiCamera()

for i in range (96):
    start = time.time()                                                                                              #starpunkt Messung mit Uhrzeit
    camera.start_preview()
    time.sleep(2)
    timestamp = datetime.datetime.now().isoformat()
    timestamp_without_colon = "".join([c if not c == ":" else "_" for c in timestamp])
    filename = f'/home/pi/Desktop/Testbilder/image{timestamp_without_colon}.jpg'
    camera.capture(filename)
    camera.stop_preview()
    time_needed = time.time() - start                                                                                # wieviel Zeit wurde benötigt? - wird abgezogen
    time.sleep(10 - time_needed)                                                                                     # benötigte Zeit von Loop abziehen
