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
  for i in range(len(doc_clean)):
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
  st.write(len(doc_clean))
  doc_clean
  clean_data
  # d1, d2, d3, d4, d5, d6, d7 = d[0], d[1], d[2], d[3], d[4], d[5], d[6]

  # doc_frame = pd.DataFrame(doc_clean, columns=['Terms'])
  # doc_frame['d1'] = d1
  # doc_frame['d2'] = d2
  # doc_frame['d3'] = d3
  # doc_frame['d4'] = d4
  # doc_frame['d5'] = d5
  # doc_frame['d6'] = d6
  # doc_frame['d7'] = d7

  # doc_frame
