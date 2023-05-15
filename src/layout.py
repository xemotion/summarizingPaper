
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime 
from wordcloud import WordCloud


st.title("논문 요약 정보 페이지")


col1, col2, col3 = st.columns(3)
monthly_data = df[(df['year'] == selected_year) & (df['month'] == selected_month)]
#요약 정보 보여주기 
totalCount = len(monthly_data) 
col4, col5 = st.columns(2)



# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

col1, col2, col3 = st.beta_columns(2, widths=[1,1])
# 첫번째 열에 텍스트 추가
with col1:
    st.write("This is column 1")

# 두번째 열에 텍스트 추가
with col2:
    st.write("This is column 2")

col1, col2, col3 = st.columns(3) 

filepath = "data/block_chain.csv"
data = pd.read_csv(filepath)

# current_month 

month = datetime.datetime.now().month 
year = datetime.datetime.now().year 



with col1: 
    st.header("A Cat")
    st.image("https://images.app.goo.gl/oWwBqsX2jgQN76Be6")


with col2: 
    st.header("button")
    if st.button("Button!!") : 
        st.write("YES")
    
with col3: 
    st.header("Chart Data")
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns =["a", "b", "c" ])
    st.bar_chart(chart_data) 


