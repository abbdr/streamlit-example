import streamlit as st 
import pandas as pd
import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
'''
# Preprocessing
## Dataset
'''
df = pd.read_csv('dataset_tweet_sentimen_tayangan_tv.csv')
df

query = 'yang kamu butuhkan hanyalah mengambil pulpen dan mulai belajar'
data = df['Text Tweet'].tolist()
data.append(query)

data_pre = pd.DataFrame(data,columns=['Text Tweet'])
'## Sentences Data'
st.write(data_pre)


stop_words = stopwords.words('indonesian')
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def remove_url(tweet):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',tweet)

def remove_html(tweet):
    html = re.compile(r'<.*?>')
    return html.sub(r'',tweet)

def remove_emoji(tweet):
    emoji_pattern = re.compile(u'['
                           u'\U0001F600-\U0001F64F'  # Emoticons
                           u'\U0001F300-\U0001F5FF'  # Symbols & pictographs
                           u'\U0001F680-\U0001F6FF'  # Transport & map symbols
                           u'\U0001F1E0-\U0001F1FF'  # Flags (iOS)
                           u']+', flags=re.UNICODE)
    return emoji_pattern.sub(r'', tweet)

def remove_angka(tweet):
    tweet = re.sub('[0-9]+', '', tweet)
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    return tweet

def remove_punct(tweets):
    translator = str.maketrans('', '', string.punctuation)
    return tweets.translate(translator)

def stem_text(text):
    return [stemmer.stem(word) for word in text]


data_pre['cleaning'] = data_pre['Text Tweet'].apply(lambda x: remove_url(x)) #
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_html(x))
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_punct(x))
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_emoji(x))
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_angka(x))
data_pre['cleaning'].drop_duplicates(inplace=True)
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: x.lower().split())
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: [word for word in x if word not in stop_words])
data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: stem_text(x))

'# \'Clean\' Data'
data_pre['cleaning']


'# \nPR mu iku 👆👆👆👆👆\ngilangi kata-kata slang'
