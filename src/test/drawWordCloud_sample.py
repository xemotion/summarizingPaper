import pandas as pd
import streamlit as st 

import csv
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import os
import nltk
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
import datetime 
import string 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 

path  = "/Users/hyeyongseo/workspace/streamlit_prj/summarizingPaper/src/data/"
df_filename = path + "block_chain.csv" 
now_year =  datetime.datetime.now().year 
now_month = datetime.datetime.now().month 

df = pd.read_csv(df_filename) 

df['year'] = df['published'].apply(lambda x : pd.to_datetime(x).year)
df['month'] = df['published'].apply(lambda x : pd.to_datetime(x).month)
df['day'] = df['published'].apply(lambda x : pd.to_datetime(x).day)

years = df['year'].unique() 
months = df['month'].unique() 

monthly_data = df[(df['year'] == now_year) & (df['month'] == now_month)]



# 불용어 리스트 만들기 




text ="" 
for i in range(len(monthly_data)): 
    text += monthly_data['summary'][i] 


# tokenizer (pos-tag)
nltk.download('averaged_perceptron_tagger')


my_tag_set = ['NN', 'VB']
ps = PorterStemmer()
# only nn 
token = word_tokenize(text) 

pos_free = [word for word, tag in nltk.pos_tag(token) if tag in my_tag_set]
stop_free=" ".join([i for i in pos_free if i not in custom_stopwords])
punct_free= stop_free.translate(str.maketrans('', '', stop_free.punctuation))
num_free=''.join(i for i in punct_free if not i.isdigit())

print(num_free) 


# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()






# 불용어 set 만드는 함수 
def setStopWord() : 

    init_stopwords = set(stopwords.words('english')) 
    
    # stopword open file 

    stop_fileapth = path + "stopword_list.txt"
    f = open(stop_fileapth)
    custom_stopword = [] 

    while True:
        line = f.readline() 
        custom_stopword.append(line.rstrip())
        if not line: break
        # print(line)
    f.close()


    set(custom_stopword)
    #print(len(custom_stopword))
    init_stopwords.update(custom_stopword) 

    return init_stopwords

# 텍스트 처리해서 word cloud 만드는 함수
def clean(doc) : 

    my_words = [word for word, tag in nltk.pos_tag(token) if tag in my_tag_set]

    nltk.download('averaged_perceptron_tagger')



def clean(doc):
    STOP_WORDS = setStopWord()
    my_tag_set = ['NN', 'VB']
    ps = PorterStemmer()
    pos_free = [word for word, tag in nltk.pos_tag(token) if tag in my_tag_set]
    stop_free=" ".join([i for i in pos_free if i not in STOP_WORDS])
    # stop_free=" ".join([i for i in doc.lower().split() if i not in custom_stopwords])
    punct_free=''.join(stop_free.maketrans('', '', stop_free.punctuation))
    num_free=''.join(i for i in punct_free if not i.isdigit())
    # stem_free = " ".join( [ ps.stem(w) for w in num_free]) 
 
    return num_free

# 데이터에 대한 shape 등으로 clean 작업함 

# word_cloud 만드는 함수 
def draw_wordCloud(text): 
    # Start with one review:
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def draw(): 
    for text in range(len(monthly_data)) : 
        text += monthly_data['summary']
        draw_wordCloud(text) 


draw() 