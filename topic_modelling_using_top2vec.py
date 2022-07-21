# -*- coding: utf-8 -*-
"""topic_modelling_using_top2vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgqfUeZ6_hG_NU_jXJ8qKhgFeP2QoJb3
"""

!pip install -q numpy
!pip install -q pandas
!pip install -q gensim
!pip install -q pynndescent>=0.4
!pip install -q umap-learn
!pip install -q hdbscan
!pip install -q wordcloud
!pip install -q tensorflow
!pip install -q tensorflow_hub
!pip install -q tensorflow_text
!pip install -q torch
!pip install -q sentence_transformers
!pip install -q hnswlib
!pip install -q joblib<1.0.0

!pip install -q top2vec[sentence_transformers]

import numpy as np
import pandas as pd
from copy import deepcopy
from top2vec import Top2Vec
import csv

filer=open('/content/drive/MyDrive/out.txt', 'r')

file1=filer.readlines()
rows_to_write=['Transcript']
with open('file2.csv','w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(rows_to_write)
  for i in file1:
    csvwriter.writerow([i.lower()])

df=pd.read_csv("/content/file2.csv")

df.shape

docs = list(df.loc[:, "Transcript"].values)

docs[0]

model = Top2Vec(docs, embedding_model='universal-sentence-encoder')

rows_to_write=['Topic Number','Topic words']

topic_number=model.get_num_topics()

topic_words, word_scores, topic_nums=model.get_topics()

topic_words[2]

with open('document1_file.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(rows_to_write)
    for k in range(0,topic_number):
      topic='topic'+str(k)
      csvwriter.writerow([topic, topic_words[k]])

lk=model.topic_sizes

dictionary={}

for i in range(0,topic_number):
  li_statement=model.search_documents_by_topic(i, num_docs=lk[i])
  topic_name='topic '+str(i)
  dictionary[topic_name] = li_statement[0]

dictionary['topic 0']

rows_to_write=['topic number','document']

with open('document2_file.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(rows_to_write)
    for j in range(0,len(docs)):
      for i in range(0,topic_number):
        topic_name='topic '+str(i)
        if docs[j] in dictionary[topic_name]:
            csvwriter.writerow([topic_name, docs[j]])

