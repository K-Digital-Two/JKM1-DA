#!/usr/bin/env python
# coding: utf-8

# In[340]:


import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import csv


# In[302]:


# 로컬 경로
# C:/Users/user/Desktop/항만운영정보시스템data


# In[431]:


# txt파일 csv로 바꾸기 

# obsList = ['인천송도', '태안', '영흥도', '대산', '안산', '평택', '인천', '덕적도']
# for i in range(len(obsCode)):
#     f_in=open(f'C:/Users/user/Desktop/항만운영정보시스템data/data_202212_{obsList[i]}.txt','r')
#     f_out=open(f'C:/Users/user/Desktop/항만운영정보시스템data/data_202212_{obsList[i]}.csv','w')

#     for line in f_in:
#         line_replace=line.replace("\t",",")
#         f_out.write(line_replace)
#     f_in.close()
#     f_out.close()


# In[470]:


# 부끄러워.... 누가 중복안되게 수정좀...부탁드려요... 
df1 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_인천송도.csv', encoding = 'cp949')
df2 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_태안.csv', encoding = 'cp949')
df3 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_영흥도.csv', encoding = 'cp949')
df4 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_대산.csv', encoding = 'cp949')
df5 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_안산.csv', encoding = 'cp949')
df6 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_평택.csv', encoding = 'cp949')
df7 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_인천.csv', encoding = 'cp949')
df8 = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather/data_202212_덕적도.csv', encoding = 'cp949')

print("*** Merging multiple csv files into a single pandas dataframe ***")
df = pd.concat(
   [df1, df2, df3, df4, df5, df6, df7,df8], ignore_index=True)
df.to_csv('C:/Users/user/Desktop/항만운영정보시스템data/weather.csv', encoding = 'cp949', sep = ",") 

df


# In[475]:


df['관측시간'] = pd.to_datetime(df['관측시간'])


# In[476]:


pd.isnull(df[])

