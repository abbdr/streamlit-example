import streamlit as st
import pandas as pd

if 'dataku' in st.session_state:
  clean_data = st.session_state['dataku']
  clean_data[-1]

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
    
  d
  doc_frame = pd.DataFrame(doc_clean, columns=['Terms'])
  for i in range(1,402):
    doc_frame[f'd{i}'] = d[i-1]

  
  # doc_frame['d1'] = d1
  # doc_frame['d2'] = d2
  # doc_frame['d3'] = d3
  # doc_frame['d4'] = d4
  # doc_frame['d5'] = d5
  # doc_frame['d6'] = d6
  # doc_frame['d7'] = d7

  doc_frame
