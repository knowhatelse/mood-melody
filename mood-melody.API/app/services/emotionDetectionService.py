import cv2
import numpy as np
from deepface import DeepFace

def detectEmotion(image):
    try:
        img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        result = DeepFace.analyze(img)
        return result[0]['dominant_emotion']
    except:
        return 400