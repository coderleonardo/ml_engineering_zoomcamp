# final model 

import tflite_runtime.interpreter as tflite
import numpy as np 

interpreter = tflite.Interpreter(model_path='dino_dragon.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

classes = [
    "dino", 
    "dragon"
]

#url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg"
def predict(url):
    img = download_image(url)
    img = prepare_image(img, target_size=(150, 150))

    # preprocessing the image
    x = np.array(img) / 255
    X = np.array([x])

    interpreter.set_tensor(input_index, X.astype(np.float32))
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result