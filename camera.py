import cv2 as cv


class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Camera not found")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
        self.cameraOn = False

        

    
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):

        if self.camera.isOpened():
            val, frame = self.camera.read()

            if val:
                return val, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return val, None
        else:
            return None
    
    def show_video(self):
        while(True): 
            ret, frame = self.camera.read()
            cv.imshow("frame", frame)
            if cv.waitKey(1) & 0xff == ord("q"):
                break
        self.camera.release()
        cv.destroyAllWindows()