import streamlit as st
import pandas as pd
import numpy as np

if 'dataku' in st.session_state:
  clean_data = st.session_state['dataku']
  # clean_data[-1]

  doc = []
  for nums in clean_data:
    for val in nums:
      doc.append(val)

  doc_clean = [item for n, item in enumerate(doc) if item not in doc[:n]]

  d = []
  a = 0
  for i in range(len(clean_data)):
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
  for i in range(1,402):
    doc_frame[f'd{i}'] = d[i-1]

  # df
  df = []
  a,b = 0,1
  for i in range(len(doc_frame.iloc[:,:1])):
      df.append(doc_frame.iloc[a:b,1:].values.sum())
      a += 1
      b += 1
  doc_frame['df'] = df

  # idf
  idf = []
  for i in doc_frame['df']:
      idf.append(np.log10(len(clean_data)/i))
  doc_frame['idf'] = idf

  # wdi
  Wd = []
  for i in range(1,402):
      a = []
      n = 0
      for j in doc_frame[f'd{i}']:
          a.append(j*idf[n])
          n += 1
      Wd.append(a)

  for i in range(1,402):
    doc_frame[f'Wd{i}'] = Wd[i-1]

  # query*wdi
  Wd401_di = []
  for i in range(1,401):
      a = []
      n = 0
      for j in doc_frame[f'Wd{i}']:
          a.append(doc_frame['Wd401'][n]*j)
          n += 1
      Wd401_di.append(a)

  for i in range(1,401):
    doc_frame[f'Wd401_d{i}'] = Wd401_di[i-1]

  # length vector
  for i in range(1,402):
    doc_frame[f'v_d{i}'] = doc_frame[f'Wd{i}'].apply(lambda x: x**2)
  
  doc_frame

  # query*wdi sum
  Wd401_di = []
  for i in range(1,401):
    Wd401_di.append(doc_frame[f'Wd401_d{i}'].values.sum())

  # length vector sum
  vs_di = []
  for i in range(1,401):
    vs_di.append(np.sqrt(doc_frame[f'v_d{i}'].values.sum()))
  vs_d401 = np.sqrt(doc_frame['v_d401'].values.sum())

  # cosine similarity
  c = []
  a = 0
  for i in Wd401_di:
      b = vs_di[a]*vs_d401
      if not b:
          c.append(0)
          a += 1
          
          continue
      c.append(i/b)
      a += 1

  st.write('input : ', st.session_state['data'][0])
  c3 = sorted(zip(c, st.session_state['dataku'], st.session_state['sentiment']), reverse=True)[:3]
  c3
  'INDEX : ', st.write(np.argmax(c3[0]))
  


