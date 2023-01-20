#!/usr/bin/env python
# coding: utf-8

# In[534]:


import csv
import pandas as pd
import numpy as np


# In[535]:


df_portmis = pd.read_csv("C:/Users/user/Desktop/항만운영정보시스템data/port-mis선박입출항조회.csv", encoding = 'cp949')


# In[536]:


df_portmis


# ### 선박용도 필터: 국제카페리, 여객선, 기타선 삭제

# In[537]:


df_portmis['선박용도'].unique()


# In[538]:


len(df_portmis['선박용도'].unique())


# In[539]:


df_portmis.drop(df_portmis[(df_portmis['선박용도'] == '여객선') | (df_portmis['선박용도'] == '국제카페리') | (df_portmis['선박용도'] == '기타선') ].index, inplace=True)


# In[540]:


df_portmis['선박용도'].unique()


# ### 입출항 필터: 입항/출항 中 출항 삭제

# In[541]:


df_portmis['입출'].unique()


# In[542]:


df_portmis = df_portmis.drop(index = df_portmis[df_portmis['입출'] == '출항'].index)
df_portmis


# In[543]:


df_portmis['입출'].unique()


# ### 구분 필터: 최종/최초 中 최초 삭제 

# In[544]:


df_portmis = df_portmis.drop(index = df_portmis[df_portmis['구분'] == '최초'].index)
df_portmis.reset_index(drop=True, inplace = True)


# In[545]:


df_portmis


# ### 열 삭제: 입항횟수, 입항횟수.1 삭제

# In[546]:


df_portmis = df_portmis.drop(['입항횟수', '입항횟수.1'], axis = 1)


# In[547]:


df_portmis


# In[548]:


df_portmis['호출부호'].to_csv('C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/호출부호.csv', encoding = 'cp949')


# ### mmsi 정보 불러와서 df_ mmsi 만들기
# + 01.20 교수님 확인 위해 수작업. 차주 크롤링 예정

# In[549]:


df_mmsi = pd.read_csv("C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/(완)호출부호_mmsi매칭.csv", encoding = 'cp949', index_col=0)


# In[550]:


df_mmsi.isnull().sum()


# In[551]:


df_mmsi


# ### df_mmsi, df_portmis 합치기 => df_ais

# In[552]:


# df_portmis의 3번째 열에 df_mmsi 추가 
df_portmis.insert(2, 'mmsi', df_mmsi['mmsi'])


# In[553]:


df_portmis


# In[554]:


df_portmis.info()


# In[555]:


df_portmis


# ### df_portmis = df_mmsi + df_portmis // Null값 제거

# In[556]:


df_portmis.isnull().sum()


# In[559]:


df_portmis.dropna().reset_index(drop=True)


# ### port-mis 입출항정보 csv저장

# In[560]:


df_portmis_sample.to_csv("C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/portmis.csv", sep = ',',encoding = 'cp949')

