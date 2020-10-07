import streamlit as st
from PIL import Image
import os, random
import base64


def home_app():
    st.title('Project ContentGen')

    st.write("""

    Welcome to the [ContentGen](https://github.com/amcurley/ContentGen) project. The goal of this project is to display the possibilties of AI generated content.

    I believe content generation such as automatic tweets, generated blog posts, and fake influencers are the way of the future.

    If you have any questions feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/aidancurley/). Enjoy!

    """)

def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        home = home_app()
