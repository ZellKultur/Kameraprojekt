from picamera import PiCamera
import time
import datetime
import os


def get_user_home():
    if os.environ.get("USER") == "root":
        return os.environ.get("SUDO_USER")
    else:
        return os.environ.get("USER")


def get_picture_path():
    return f"/home/{get_user_home()}/Desktop/Testbilder"


def create_testbilder_path():
    path = get_picture_path()
    if not os.path.isdir(path):
        os.makedirs(path)


if __name__ == '__main__':
    picture_path = get_picture_path()
    create_testbilder_path()

    camera = PiCamera()
    for i in range(96):
        start = time.time()  # starpunkt Messung mit Uhrzeit
        camera.start_preview()
        time.sleep(2)
        timestamp = datetime.datetime.now().isoformat()
        timestamp_without_colon = "".join([c if not c == ":" else "_" for c in timestamp])
        filename = f'image{timestamp_without_colon}.jpg'
        camera.capture(f"{picture_path}/{filename}")
        camera.stop_preview()
        time_needed = time.time() - start  # wieviel Zeit wurde benötigt? - wird abgezogen
        time.sleep(10 - time_needed)
