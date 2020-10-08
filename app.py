import streamlit as st
from PIL import Image
import os, random
import base64
import fire
import json
import os
import numpy as np
import tensorflow as tf
import awesome_streamlit as ast
import gpt.src.encoder as encoder
import gpt.src.model as model
import gpt.src.sample as sample
import pages.gan
import pages.home
import pages.blog
import pages.best_generated

def main():
    """Main Function of the App"""
    PAGES = {
        'Home': pages.home,
        'PersonGen': pages.gan,
        "BlogGen": pages.blog,
        'The Best Generated Blog Posts': pages.best_generated
    }
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Select Your Page", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Aidan Curley. You can learn more about me and future projects on
        [LinkedIn](https://www.linkedin.com/in/aidancurley/).
        """
    )

if __name__ == "__main__":
    main()
