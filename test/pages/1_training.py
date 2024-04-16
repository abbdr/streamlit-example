import streamlit as st 
import pandas as pd
import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

'# Dataset'

with st.spinner('Getting Dataset...'):
    df = pd.read_excel('dataset_tweet_sentimen_tayangan_tv.xlsx')
    # df = pd.read_csv('dataset_tweet_sentimen_tayangan_tv.csv')
    st.session_state['data_awal'] = df['Text Tweet']
    st.session_state['sentiment'] = df['Sentiment']
    st.session_state['id'] = df['Id']
    df

data_pre = pd.DataFrame(df['Text Tweet'])
'# Sentences Data'
st.write(data_pre)

kata = ['ya','yuk','aja','yg','liat','ni','moga','nih','oke','kes','gin','t']
stop_words = set(stopwords.words('indonesian'))

f = open('combined_stop_words.txt','r').readlines()
for i in f:
  stop_words.add(re.sub(r'[^a-z]','',i))
for i in kata:
  stop_words.add(i)


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


with st.spinner('Reducing url...'):
  data_pre['cleaning'] = data_pre['Text Tweet'].apply(lambda x: remove_url(x))
  '## Reduce url'
  data_pre['cleaning']

with st.spinner('Reducing html code...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_html(x))
  '## Reduce html code'
  data_pre['cleaning']

with st.spinner('Reducing punctuation...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_punct(x))
  '## Reduce punctuation'
  data_pre['cleaning']

with st.spinner('Reducing emoji...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_emoji(x))
  '## Reduce emoji'
  data_pre['cleaning']

with st.spinner('Reducing number...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: remove_angka(x))
  '## Reduce number'
  data_pre['cleaning']

with st.spinner('Reducing duplicate item...'):
  data_pre['cleaning'].drop_duplicates(inplace=True)
  '## Reduce duplicate item'
  data_pre['cleaning']

with st.spinner('Lowercasing and Tokenization...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: x.lower().split())
  '## Lowercasing and Tokenization'
  data_pre['cleaning']

with st.spinner('Reducing stopword...'):
  data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: [word for word in x if word not in stop_words])
  '## Reduce stopword'
  data_pre['cleaning']

@st.cache_data
def stem():
    data = data_pre['cleaning'].apply(lambda x: stem_text(x))
    return data

@st.cache_data
def root_word():
  with st.spinner('Getting LLM Dictionary...'):
    kamus = set(pd.read_csv('kata_dasar_bhs_indo.csv')['0'])
    kamus.remove('moga')
    data_pre['cleaning'] = data_pre['cleaning'].apply(lambda x: [word for word in x if word in kamus])
  
    return data_pre['cleaning']



'## Stemming'
with st.spinner('Stemming...'):
  data_pre['cleaning'] = stem()
  data_pre['cleaning']


'## Apply kata dasar'
data_pre['cleaning'] = root_word()
# data_pre['cleaning']


# '## And that\'s the \'clean\' training data\n\n'
'## '


dataku = data_pre['cleaning']
st.session_state['training'] = dataku
st.session_state['training']

num = st.session_state['nB'] if 'nB' in st.session_state else 0
st.write(num)
    

