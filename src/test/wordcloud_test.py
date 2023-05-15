import streamlit as st
import pandas as pd 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
import plotly.express as px 
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

wordcloud = WordCloud().generate(text)
img = "cat.png"
fig, ax = plt.subplots()

ax.scatter([1,2,3], [2,3,4])
ax.axis("off")
st.pyplot(fig)
