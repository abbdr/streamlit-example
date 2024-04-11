import streamlit as st
import pandas as pd

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

  df = []
  a,b = 0,1
  for i in range(len(doc_frame.iloc[:,:1])):
      df.append(doc_frame.iloc[a:b,1:].values.sum())
      a += 1
      b += 1
  
  doc_frame['df'] = df

  idf = []
  for i in doc_frame['df']:
      idf.append(np.log10(7/i))
  
  doc_frame['idf'] = idf

  doc_frame




