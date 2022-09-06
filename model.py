from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np

def giveLabel(sample_img):
    model = load_model("./weights/FacialEmotionRecognition.h5")
    img = load_img(sample_img,target_size = (48,48,3))
    x = img_to_array(img)
    x = np.expand_dims(x,axis=0)

    target = model.predict(x)
    target = np.argmax(target)
    
    return target
