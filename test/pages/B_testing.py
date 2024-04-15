import streamlit as st 
import pandas as pd
import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


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

query = ''
data_pre = ''
data = ''
input = st.text_input("Masukkan teks Anda di sini:")

@st.experimental_memo
def show_data_pre():
  st.markdown('## Input Data')
  st.write(data_pre)

@st.experimental_memo
def show_data():
  st.markdown('## \'Clean\' Training + Test/Input Data')
  st.write(data_pre['cleaned'])

data_pre = ''
if st.button('simpan'):
  st.session_state['training'] = ''
  st.session_state['testing'] = ''
  st.session_state['c'] = ''

  del st.session_state['training']
  del st.session_state['testing']
  del st.session_state['c']
  show_data_pre.clear()
  show_data.clear()

  if 'nA' in st.session_state:
    st.session_state['nB'] += 1
    pass
  else:
    st.session_state['nA'] = 0
    st.session_state['nB'] = st.session_state['nA']+1

  if input=='':
    pass
  else:
    input_user = input
    # st.session_state['k'] = k
    query = [input_user]
    data_pre = pd.DataFrame(query,columns=['Text Input'])
    st.session_state['input_df'] = data_pre
    
    show_data_pre()
    
    with st.spinner('Reducing url...'):
      data_pre['cleaned'] = data_pre['Text Input'].apply(lambda x: remove_url(x))
    
    with st.spinner('Reducing html code...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: remove_html(x))
    
    with st.spinner('Reducing punctuation...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: remove_punct(x))
    
    with st.spinner('Reducing emoji...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: remove_emoji(x))
    
    with st.spinner('Reducing number...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: remove_angka(x))
    
    with st.spinner('Reducing duplicate item...'):
      data_pre['cleaned'].drop_duplicates(inplace=True)
    
    with st.spinner('Lowercasing and Tokenization...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: x.lower().split())
    
    with st.spinner('Reducing stopword...'):
      data_pre['cleaned'] = data_pre['cleaned'].apply(lambda x: [word for word in x if word not in stop_words])
        
    def stem():
        return data_pre['cleaned'].apply(lambda x: stem_text(x))
    

    data_pre['cleaned'] = stem()
    data = data_pre['cleaned']
    st.session_state['testing'] = data
        
    show_data()
    
def train_plus_input():
  input = st.session_state['testing'][0]
  dataku = st.session_state['training'][0]
  # dataku.append(input)
  # dataku = pd.DataFrame(dataku)
  # st.session_state['dataku'] = dataku

  st.markdown('## \'Clean\' Training + Test/Input Data')
  st.write(dataku)

if 'testing' in st.session_state:
  train_plus_input()

num = st.session_state['nB'] if 'nB' in st.session_state else 0
num




