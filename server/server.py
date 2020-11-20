import base64
import io
import os

import numpy as np
from PIL import Image
from flask import request
from keras.models import load_model
from keras_preprocessing.image import img_to_array

from server import app

threshold = 0.5
img_size = (256, 256)

# To use only CPU and not any visible GPUs:
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model = load_model('../model')
model.summary()

# Very simple homepage
home_html = '''
    <!DOCTYPE html>
    <title>Is pineapple pizza</title>
    
    <div style="text-align: center;">
        <h1>Upload a Photo</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=image>
            <input type=submit value=Upload>
        </form>
    </div>
    '''


def prepare_image(image):
    # Make sure it's RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(img_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        img_data = request.files["image"]
        if img_data:
            data = img_data.read()
            image = Image.open(io.BytesIO(data))
            image = prepare_image(image)

            result = model.predict(image)
            accuracy = result[0][0]
            is_pineapple = accuracy > threshold
            label = ("" if is_pineapple else "Not ") + "Pineapple Pizza"
            color = "green" if is_pineapple else "red"

            return home_html + """
                <div style="text-align: center;">
                    <h2 style="color: %s"> %s (%s%%)</h2>
                    <img style="width: 600px;" src="data:image/jpg;base64, %s "/>
                </div>
            """ % (color, label, str(round(accuracy * 100, 2)), base64.b64encode(data).decode('ascii'))

    return home_html
