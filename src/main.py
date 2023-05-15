
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime 
import nltk 
from transformers import AutoTokenizer 
from transformers import AutoModelForSeq2SeqLM
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
import os.path 

global years, months, df, monthly_data, now_year, now_month, model, toeknizer, initFlag, FILEPATH


import streamlit as st

st.markdown("## Main page 📃")
st.sidebar.markdown("## Main page 📃")

def isExistFile(filepath):
    if os.path.isfile(filepath):
        return True 
    else: 
        return False 
    
# select year, select month 
def mainPage() : 
    initFlag = False 
    global years, months, df, monthly_data, now_year, now_month 
    df = init() 
    if initFlag == False: 
        modelInit()     
    

    st.title("논문 요약 정보 페이지📃")
    # st.dataframe(df) 
    
    with st.form("select_month") : 
        
        st.write("원하는 연도를 입력하세요")
        col1, col2  = st.columns(2)

        with col1: 
            selected_year = st.text_input("Year")
            
        with col2: 
            selected_month = st.text_input("Month")
        


        submitted = st.form_submit_button("Submit")


        count = 1 
        if submitted:
            
            data = df 
            monthly_data = data[(data['year'] == int(selected_year)) & (data['month'] == int(selected_month))] 
            # st.dataframe(monthly_data[:3]) 
            #요약 정보 보여주기 
            totalCount = len(monthly_data) 
            
            st.write(f'{selected_year}년 {selected_month}월 총 {totalCount}개의 논문이 있습니다')


            for i in range(totalCount): 
                text = monthly_data.iloc[i]['summary']
               
                pdf_url = data.iloc[i]['pdf_url']
                st.write(str(count) + ". TITLE: " + monthly_data.iloc[i]['title']) 
                pdf_link = f'[PDF]({pdf_url})'
                st.markdown(pdf_link, unsafe_allow_html=True)
                with st.spinner('Wait for it...'):
                    summary = getSummary(text) 
                    st.success("[요약]" + summary) 
                with st.expander("Abract 보기"): 
                    st.write(text)
                count += 1 



def modelInit() : 
    global model, tokenizer 
    nltk.download('punkt')
    model_name = "checkpoint-600"
    model_dir = f"D:\workspace\streamlist_prj\myModels\{model_name}"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir,local_files_only = True )
    tokenizer = AutoTokenizer.from_pretrained(model_dir,local_files_only = True )
    initFlag = True 



def getSummary(text) : 
    result = [] 
    inputs = ["summarize: " + text]
    max_input_length = 1024 

    inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=50, max_length=100)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]
    return predicted_title 

# DATA INITIATLIZTE --> MONTHLY DATA 
@st.cache_data
def init(): 
    global years, months, df, monthly_data, now_year, now_month 
    FILEPATH = "D:/workspace/streamlist_prj/src/data/block_chain.csv"
    now_year =  datetime.datetime.now().year 
    now_month = datetime.datetime.now().month 

    df = pd.read_csv(FILEPATH) 

    df['year'] = df['published'].apply(lambda x : int(pd.to_datetime(x).year))
    df['month'] = df['published'].apply(lambda x : int(pd.to_datetime(x).month))
    df['day'] = df['published'].apply(lambda x : int(pd.to_datetime(x).day))

    years = df['year'].unique() 
    months = df['month'].unique() 

    return df   

mainPage() 
