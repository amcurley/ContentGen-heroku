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

    # DO NOT PUSH TO GITHUB WITHOUT REMOVING THESE FIRST
    # aws_access_key_id = AWS_ACCESS_KEY_ID,
    # aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    # DO NOT PUSH TO GITHUB WITHOUT REMOVING THESE FIRST


)

def image_from_s3(bucket, key):

    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get('Body').read()

    return Image.open(io.BytesIO(img_data))

def gen():
    # folder = r'/Users/aidancurley/Documents/dsir/personal/ContentGen/faces'
    #
    # a = random.choice(os.listdir(folder))
    #
    # file = folder + "/" + a #File to selected image
    #
    # image = Image.open(file)
    nums = random.randint(1, 4)
    image = image_from_s3('images-contentgen', f'seed{nums}.png')

    file = s3.Bucket('images-contentgen').download_file(f'seed{nums}.png', f'seed{nums}.png')

    st.title('Person Generation')
    st.markdown("Click Generate to Get Your Face!")
    if st.button('Generate'):
        st.image(image, use_column_width=True)


def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        stylegan = gen()
