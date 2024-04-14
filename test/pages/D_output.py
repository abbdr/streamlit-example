import streamlit as st
import pandas as pd
if 'c' in st.session_state:
  st.write('### input : ', st.session_state['input_df'])
  st.write('### k : ',st.session_state['k'])
  ck = sorted(zip(st.session_state['c'], st.session_state['id'], st.session_state['data_awal'], st.session_state['sentiment']),  reverse=True)[:st.session_state['k']]
  ck = pd.DataFrame(ck)
  ck.rename(columns = {0:'Relevancy', 1:'Id', 2:'terms', 3:'Sentiment'}, inplace = True)
  '### Output'
  ck
n = st.session_state['nB']  if 'nB' in st.session_state else 1
n