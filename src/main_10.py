
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

global years, months, df, monthly_data, now_year, now_month, model, toeknizer 



def isExistFile(filepath):
    if os.path.isfile(filepath):
        return True 
    else: 
        return False 
    
FILEPATH = "data\block_chain.csv"
# select year, select month 
def mainPage() : 
    global years, months, df, monthly_data, now_year, now_month 
    init() 
    modelInit() 
    selected_year = 2023 
    selected_month = 4 

    st.markdonw("# Main Page ")
    st.sidebar.markdown("# Main Page ")


    st.title(f"논문 요약 정보 : ")
    col1, col2, col3 = st.columns(3)

    with col1: 
       selected_year = st.text_input("label goes here", default_value_goes_here)
    with col2: 
       selected_month = st.text_input("label goes here", default_value_goes_here)
    
    submitted = st.button(" 선택 ")

   
    if submitted : 
        monthly_data = df[(df['year'] == selected_year) & (df['month'] == selected_month)]
        #요약 정보 보여주기 
        totalCount = len(monthly_data) 
        

        filepath = "data/"
        for i in range(totalCount): 
            text = monthly_data['summary'][i] 
            #st.text("[내용] \n" + monthly_data['title'][i] ) 
            st.text("[title]" + monthly_data['title'][i] + "\n")
            
            with st.expander('Abstract 보기') :
                st.write(monthly_data['summary']) 
            summary = getSummary(text) 
            
            st.write("[요약] \n"+ summary )
                
        


def modelInit() : 
    global model, tokenizer 
    nltk.download('punkt')
    model_name = "checkpoint-200"
    model_dir = f"statics/models/MyModel/{model_name}"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir,local_files_only = True )
    tokenizer = AutoTokenizer.from_pretrained(model_dir,local_files_only = True )



def getSummary(text) : 
    result = [] 
    inputs = ["summarize: " + text]
    max_input_length = 2048 

    inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=25, max_length=50)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]
    return predicted_title 

# DATA INITIATLIZTE --> MONTHLY DATA 

def init(): 
    global years, months, df, monthly_data, now_year, now_month 
    
    now_year =  datetime.datetime.now().year 
    now_month = datetime.datetime.now().month 

    df = pd.read_csv(FILEPATH) 

    df['year'] = df['published'].apply(lambda x : pd.to_datetime(x).year)
    df['month'] = df['published'].apply(lambda x : pd.to_datetime(x).month)
    df['day'] = df['published'].apply(lambda x : pd.to_datetime(x).day)

    years = df['year'].unique() 
    months = df['month'].unique() 

    monthly_data = df[(df['year'] == now_year) & (df['month'] == now_month)]



mainPage() 
