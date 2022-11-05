import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
class Video(object):
    def __init__(self) :
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        result = DeepFace.analyze(img_path=frame, actions=['emotion'], enforce_detection=False)
        # emotion=result['dominant_emotion']
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        emotion=result['dominant_emotion']
        txt=str(emotion)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, txt, (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()
        