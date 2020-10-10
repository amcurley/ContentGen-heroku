import streamlit as st
from PIL import Image
import os, random
import base64
import awesome_streamlit as ast

# AWS
import io
import random
import boto3


s3 = boto3.resource(
    service_name = 's3',
    region_name = 'us-east-2',

)

def image_from_s3(bucket, key):

    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get('Body').read()

    return Image.open(io.BytesIO(img_data))

def gen():

    nums = random.randint(1, 10)
    image = image_from_s3('images-contentgen', f'seeds{nums}.png')

    file = s3.Bucket('images-contentgen').download_file(f'seeds{nums}.png', f'seed{nums}.png')

    st.title('Person Generation')
    st.markdown('These faces were pre generated in a [Google Colab](https://github.com/amcurley/test-heroku/blob/master/StyleGAN2_faces.ipynb) notebook due to computing contraints.')
    st.markdown('Due to financial and computing constraints this will only generate the same 10 random images.')
    st.markdown('Here is a link to the folder of 15,000 fake faces: [Google Drive](https://drive.google.com/drive/folders/1g1206aLsGX-PZ65tGKNdAFKBmyVHTrae?usp=sharing)')
    st.markdown("Click **generate** to generate a face!")
    if st.button('Generate'):
        st.image(image, use_column_width=True)

        st.title('Latent Walk')
        st.markdown('This is an example of interpolation through the latent space of the GAN ')
        st.markdown("![Alt Text](https://media.giphy.com/media/oXhfoaXQXAozUJat25/giphy.gif)")

def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        stylegan = gen()
