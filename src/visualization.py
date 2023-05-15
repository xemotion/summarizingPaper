import pandas as pd 

import numpy as np 
import matplotlib.pyplot as plt 
from wordcloud import WORDCLOUD 
import nltk
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

def word_cloud() : 
    # Start with one review:
    # define the stopwords and also import predefined ones

    # print(custom_stopword)
    STOP_WORDS = setStopWords(words) 
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords=STOPWORDS).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def setStopWords(words): 
    
    nltk.download('stopwords')

    custom_stopword = [] 
    for w in words:
        #print(w, " : ", ps.stem(w))
        filepath = "/content/drive/MyDrive/Colab Notebooks/mini_project/data/stopword_list"
        f = open(filepath)
        custom_stopword = [] 
        while True:
            line = f.readline() 
            custom_stopword.append(line.rstrip())
        
        f.close()
        return custom_stopword 

    
    from nltk.corpus import stopwords
    custom_stopwords = set(stopwords.words('english')) # get the default English stop words
    custom_stopwords.update(custom_stopword) 
    print(len(custom_stopwords)) 


def init(filepath) : 
    df = pd.read_csv(filepath) 

    df['year'] = df['published'].apply(lambda x : pd.to_datetime(x).year)
    df['month'] = df['published'].apply(lambda x : pd.to_datetime(x).month)
    df['day'] = df['published'].apply(lambda x : pd.to_datetime(x).day)

def getData(year, month): 

    data = df[(df['year'] == year) & (df['month'] == month)]

    def getData(year, month) :

        data = df[(df['year'] == year) & (df['month'] == month)]

        return data 
