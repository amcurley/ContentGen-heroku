import streamlit as st
from PIL import Image
import os, random
import base64


def home_app():
    st.title('Project ContentGen')

    st.write("""

    Welcome to the [ContentGen](https://github.com/amcurley/ContentGen) project.

    The purpose of the **ContentGen** project is to show the awesome/negative use cases of computer generated content.

    I believe AI generated content has the potential to accelerate business success while simultaneously replacing a lot of jobs and potentially ruining the creative industry.

    This application provides:
    - A section called **FaceGen** where you can view computer generated people.
    - A section called **BlogGen** where a user can generate an infinite amount of blogs.
    - A gallery of some of the best generated blog posts from **BlogGen**.

    If you have any questions feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/aidancurley/). Enjoy!

    """)

def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        home = home_app()
