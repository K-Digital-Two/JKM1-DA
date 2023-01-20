#!/usr/bin/env python
# coding: utf-8

# In[100]:


import csv
import pandas as pd
import numpy as np


# In[437]:


df_portmis = pd.read_csv("C:/Users/user/Desktop/항만운영정보시스템data/port-mis선박입출항조회.csv", encoding = 'cp949')


# In[438]:


df_portmis


# ### 선박용도 필터: 국제카페리, 여객선, 기타선 삭제

# In[439]:


df_portmis['선박용도'].unique()


# In[440]:


len(df_portmis['선박용도'].unique())


# In[441]:


df_portmis.drop(df_portmis[(df_portmis['선박용도'] == '여객선') | (df_portmis['선박용도'] == '국제카페리') | (df_portmis['선박용도'] == '기타선') ].index, inplace=True)


# In[442]:


df_portmis['선박용도'].unique()


# ### 입출항 필터: 입항/출항 中 출항 삭제

# In[443]:


df_portmis['입출'].unique()


# In[444]:


df_portmis = df_portmis.drop(index = df_portmis[df_portmis['입출'] == '출항'].index)
df_portmis


# In[445]:


df_portmis['입출'].unique()


# ### 구분 필터: 최종/최초 中 최초 삭제 

# In[446]:


df_portmis = df_portmis.drop(index = df_portmis[df_portmis['구분'] == '최초'].index)
df_portmis.reset_index(drop=True, inplace = True)


# ### 열 삭제: 입항횟수, 입항횟수.1 삭제

# In[447]:


df_portmis = df_portmis.drop(df_portmis.iloc[:,3:5], axis = 1)


# In[448]:


df_portmis


# In[449]:


# df_portmis['호출부호'].to_csv('C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/호출부호.csv', encoding = 'cp949')


# ### mmsi 정보 불러와서 df_ mmsi 만들기
# + 01.20 교수님 확인 위해 수작업. 차주 크롤링 예정

# In[450]:


df_mmsi = pd.read_csv("C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/호출부호_sample.csv", encoding = 'cp949')


# In[451]:


df_mmsi = df_mmsi.dropna()


# In[452]:


df_mmsi.iloc[:,2]


# ### df_mmsi, df_portmis 합치기 => df_ais

# In[454]:


df_portmis.insert(2, 'mmsi', df_mmsi.iloc[:,2])


# In[455]:


df_portmis


# In[456]:


df_portmis_sample = df_portmis.dropna()


# In[458]:


df_portmis_sample.reset_index(drop=True)

