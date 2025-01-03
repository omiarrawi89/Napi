
import streamlit as st
import numpy as np
from PIL import Image
import io

st.title('Follicle Labeler Demo')

# Upload image
uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Add controls for labeling
    st.subheader('Labeling Controls')
    
    # Add a button to mark follicle
    if st.button('Mark Follicle'):
        st.write('Follicle marked! (Demo functionality)')
    
    # Add size measurement
    size = st.slider('Follicle Size (pixels)', 1, 100, 50)
    st.write(f'Selected size: {size} pixels')
    
    # Add classification
    follicle_type = st.selectbox(
        'Select follicle type',
        ['Primary', 'Secondary', 'Tertiary', 'Graafian']
    )
    st.write(f'Selected type: {follicle_type}')
    
    # Save button
    if st.button('Save Labels'):
        st.success('Labels saved! (Demo functionality)')
