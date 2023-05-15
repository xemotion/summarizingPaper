from wordcloud import WordCloud
import streamlit as st
from PIL import Image
import numpy as np

# generate word cloud from frequencies
frequencies = {"apple": 10, "banana": 5, "cherry": 3}
wc = WordCloud().generate_from_frequencies(frequencies)

# convert word cloud object to image
wc_image = wc.to_image()

# convert image to numpy array
np_array = np.array(wc_image)

# convert numpy array to PIL image
pil_image = Image.fromarray(np_array)

# display image using streamlit
st.image(pil_image)