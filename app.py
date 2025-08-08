import streamlit as st
from PIL import Image
from utils import load_model, stylize_image

st.set_page_config(page_title='Style Transfer APP', layout='centered')

st.title('Neural Style Transfker')
st.markdown('Upload an image and choose an art style to stylize it')