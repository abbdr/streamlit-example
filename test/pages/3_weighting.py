import streamlit as st
import pandas as pd
import numpy as np

# @st.experimental_memo
@st.cache_data
def weighting():
  clean_data = st.session_state['dataku']
  # clean_data
  length = len(clean_data)
  # length
  # return

  doc = []
  for nums in clean_data:
    for val in nums:
      doc.append(val)

  doc_clean = [item for n, item in enumerate(doc) if item not in doc[:n]]

  d = []
  a = 0
  for i in range(length):
      list = []
      for j in doc_clean:
          if a>=len(clean_data):
              break
          if j in clean_data[a]:
              # print('1')
              list.append(1)
          else:
              # print('0')
              list.append(0)
      a += 1
      
      # print()
      d.append(list)
    
  # d
  doc_frame = pd.DataFrame(doc_clean, columns=['Terms'])
  for i in range(1,length+1):
    doc_frame[f'd{i}'] = d[i-1]
  '## Term Frequency'
  with st.spinner('Calculating Term Frequency...'):
    st.write(doc_frame.iloc[:,1:])

  # df
  df = []
  a,b = 0,1
  for i in range(len(doc_frame.iloc[:,:1])):
      df.append(doc_frame.iloc[a:b,1:].values.sum())
      a += 1
      b += 1
  doc_frame['df'] = df
  '## Document Frequency'
  with st.spinner('Calculating Document Frequency...'):
    st.write(doc_frame.iloc[:,length+1:])

  # idf
  idf = []
  for i in doc_frame['df']:
      idf.append(np.log10(len(clean_data)/i))
  doc_frame['idf'] = idf
  '## inverse Document Frequency'
  with st.spinner('Calculating Inverse Document Frequency...'):
    st.write(doc_frame.iloc[:,length+2:])

  # wdi
  Wd = []
  for i in range(1,length+1):
      a = []
      n = 0
      for j in doc_frame[f'd{i}']:
          a.append(j*idf[n])
          n += 1
      Wd.append(a)

  for i in range(1,length+1):
    doc_frame[f'Wd{i}'] = Wd[i-1]
  '## Weighting Document inverse'
  with st.spinner('Calculating Weighting Document inverse...'):
    st.write(doc_frame.iloc[:,length+3:])

  # query*wdi
  WdLength_di = []
  for i in range(1,length):
      a = []
      n = 0
      for j in doc_frame[f'Wd{i}']:
          a.append(doc_frame[f'Wd{length}'][n]*j)
          n += 1
      WdLength_di.append(a)

  for i in range(1,length):
    doc_frame[f'WdLength_d{i}'] = WdLength_di[i-1]
  '## Query*WDi'
  with st.spinner('Calculating Query*WDi...'):
    st.write(doc_frame.iloc[:,(length+3)+(length):])

  # length vector
  for i in range(1,length+1):
    doc_frame[f'v_d{i}'] = doc_frame[f'Wd{i}'].apply(lambda x: x**2)
  '## Length Vector'
  with st.spinner('Calculating Length Vector...'):
    st.write(doc_frame.iloc[:,(length+3)+(length)+(length+1):])

  # query*wdi sum
  '## query*wdi sum'
  WdLength_di = []
  with st.spinner('Calculating query*wdi sum...'):
    for i in range(1,length):
      WdLength_di.append(doc_frame[f'WdLength_d{i}'].values.sum())
  WdLength_di_ = pd.DataFrame(WdLength_di, columns=['query*wdi sum'])
  WdLength_di_

  # length vector sum
  '## length vector sum'
  vs_di = []
  with st.spinner('Calculating length vector sum...'):
    for i in range(1,length):
      vs_di.append(np.sqrt(doc_frame[f'v_d{i}'].values.sum()))
    vs_dLength = np.sqrt(doc_frame[f'v_d{length}'].values.sum())
  vector = pd.DataFrame(WdLength_di, columns=['length vector sum'])
  vector

  # cosine similarity
  '## cosine similarity'
  c = []
  a = 0
  with st.spinner('Calculating cosine similarity sum...'):
    for i in WdLength_di:
        if a >= len(vs_di):
          break
        b = vs_di[a]*vs_dLength
        if not b:
            c.append(0)
            a += 1
            
            continue

        c.append(i/b)
        a += 1
        st.session_state['c'] = c
  c = pd.DataFrame(WdLength_di, columns=['cosine similarity'])
  c


if 'dataku' in st.session_state:
  nA = st.session_state['nA']
  nB = st.session_state['nB']
  if nA != nB:
    if nB-1 != nA:
      st.session_state['nA'] = st.session_state['nB']-1
    st.session_state['nA'] += 1
    weighting.clear()
  weighting()
  st.write(nB)

else:
  num = st.session_state['nB'] if 'nB' in st.session_state else 0
  st.write(num)


