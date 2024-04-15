import streamlit as st
import pandas as pd
if 'c' in st.session_state:
  st.write('### input : ', st.session_state['input_df'])
  k = st.number_input("Masukkan nilai k di sini (ganjil):",3,201,value=3,step=2)
  k = k+1 if not k%2 else k
  st.session_state['k'] = k
  st.write('### k : ',st.session_state['k'])
  ck = sorted(zip(st.session_state['c'], st.session_state['id'], st.session_state['data_awal'], st.session_state['sentiment']),  reverse=True)[:st.session_state['k']]
  ck = pd.DataFrame(ck)
  ck.rename(columns = {0:'Relevancy', 1:'Id', 2:'terms', 3:'Sentiment'}, inplace = True)
  '### Output'
  ck
  positif,negatif = [],[]
  for i in ck['Sentiment'].values:
    if i == 'positive':
      positif.append('')
    else:
      negatif.append('')
  st.write(len(positif))
  st.write(len(negatif))
  st.write('### Kesimpulan: ', 'positif' if positif>negatif else 'negatif')
n = st.session_state['nB']  if 'nB' in st.session_state else 1
st.write(n)
