import os
import subprocess
from camera import Camera


def check_open_cv():
    open_cv_present = False
    try:
        import cv2
        open_cv_present = True
    except ImportError:
        os.system("pip install opencv-python")
    return ["openCv", open_cv_present]

def test_camera():
    camera = Camera()
    try:
        camera.show_video()
    except ValueError as e:
        pass



