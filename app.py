import streamlit as st
from PIL import Image
from utils import load_model, stylize_image

st.set_page_config(page_title='Style Transfer APP', layout='centered')

st.title('Neural Style Transfer')
st.markdown('Upload an image and choose an art style to stylize it')

# Style options
STYLE_NAMES = {
    "Candy": "candy",
    "Mosaic": "mosaic",
    "Rain Princess": "rain_princess",
    "Udnie": "udnie",
}

style_label = st.selectbox("Choose a style:", list(STYLE_NAMES.keys()))
style = STYLE_NAMES[style_label]

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert('RGB')
    st.image(input_image, caption="Original Image", use_container_width=True)

    if st.button('Stylize'):
        with st.spinner('Applying style...'):
            model = load_model(style)
            output_image = stylize_image(model, input_image)
            st.image(output_image, caption=f"Stylized with {style_label}", use_container_width=True)
