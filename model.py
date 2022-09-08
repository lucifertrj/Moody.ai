from random import sample
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np
import cv2
import os

def detectFace(sample_img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + '../data/haarcascade_frontalface_default.xml')
    face = cv2.imread(os.path.join("static",sample_img),0)
    detected_face = faceCascade.detectMultiScale(face)
    saveFileName,ext = sample_img.split(".")
    if len(detected_face) == 0:
        return -999
    elif len(detected_face) == 1:
        x,y,w,h = detected_face[0]
        croppedImage = face[y:y+h,x:x+w]
        cv2.imwrite(f"static/{saveFileName}_predicted.jpg",croppedImage)
        return saveFileName
    else:
        for x,y,w,h in detected_face:
            temp = face[y:y+h,x:x+w]
            detect_temp = faceCascade.detectMultiScale(temp)
            if len(detected_face) == 0:
                return -999
            else:
                for _ in detect_temp:
                    croppedImage = face[y:y+h,x:x+w]
                    cv2.imwrite(f"static/{saveFileName}_predicted.jpg",croppedImage)
                    return saveFileName

def giveLabel(IMG):
    model = load_model("./weights/FacialEmotionRecognition.h5")
    img = load_img(IMG,target_size = (48,48,3))
    x = img_to_array(img)
    x = np.expand_dims(x,axis=0)

    target = model.predict(x)
    target = np.argmax(target)
    
    return target
