import cv2
import numpy as np
from deepface import DeepFace

def detect_emotion(file):
    try:
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        result = DeepFace.analyze(image)
        return result[0]['dominant_emotion']
    except:
        return 400