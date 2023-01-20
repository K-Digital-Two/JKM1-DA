#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import csv


# In[302]:


# 로컬 경로
# C:/Users/user/Desktop/항만운영정보시스템data


# In[2]:


# # txt파일 csv로 바꾸기 

# obsList = ['인천송도', '태안', '영흥도', '대산', '안산', '평택', '인천', '덕적도']
# for i in range(len(obsCode)):
#     f_in=open(f'C:/Users/user/Desktop/항만운영정보시스템data/data_202212_{obsList[i]}.txt','r')
#     f_out=open(f'C:/Users/user/Desktop/항만운영정보시스템data/data_202212_{obsList[i]}.csv','w')

#     for line in f_in:
#         line_replace=line.replace("\t",",")
#         f_out.write(line_replace)
#     f_in.close()
#     f_out.close()


# In[171]:


# 부끄러워.... 누가 중복안되게 수정좀...

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


# In[172]:


# 데이터프레임 확인
df.info()


# In[173]:


# 컬럼 중 "-" 값 갯수 확인 
(df== '-').sum()


# ### 필요없는 컬럼 제거(수온, 염분, 유의파고, 유의파주기, 최대파고, 최대파주기, 시정)

# In[174]:


df = df.drop(df.iloc[:,5:11], axis=1)


# In[175]:


df.drop(['시정(m)'], axis = 1, inplace = True)


# ### 결측치 처리

# In[176]:


# df 값 중 "-"값을 None으로 처리 후 dropna 
df= df.replace("-", None)


# In[177]:


df.isnull().sum()


# In[178]:


df = df.dropna(axis = 0)


# In[179]:


df.isnull().sum()


# In[180]:


df = df.reset_index(drop=True)
df


# ### 컬럼명 변경

# In[181]:


# 풍향 컬럼명 변경
df.rename(columns={'Unnamed: 12':'풍향'}, inplace = True)


# In[182]:


df.info()


# In[183]:


# 전처리에 편리하게 바꾼다. 마지막에 다시 단위 포함시킨 컬럼명으로 변경예정
df.columns = ['관측소명', '관측시간', '위도', '경도','조위', '풍속', '풍향', '풍향_각도', '기온', '기압']


# In[184]:


df


# In[185]:


df.T.index.values


# ### 데이터 타입 변경

# In[186]:


# 관측시간 타입변경 string -> datetime 
df['관측시간'] = pd.to_datetime(df['관측시간'])

# 조위, 풍속, 풍향, 기온, 기압 타입변경 string -> double
df = df.astype({ '조위' : 'float64',                '풍속': 'float64',                '풍향_각도':'float64',                '기온': 'double',                '기압': 'double'})


# In[187]:


df


# ### 컬럼명 초기화 (단위 추가)

# In[188]:


df.columns = ['관측소명', '관측시간', '위도', '경도', '조위(cm)', '풍속(m/s)', '풍향', '풍향(deg)', '기온(℃)','기압(hPa)']


# In[189]:


df.head()


# ### 풍향 컬럼 포함 데이터프레임
# dfWeather

# In[190]:


dfWeather = df
dfWeather


# ### 풍향 컬럼 삭제 데이터프레임
# df_weather

# In[191]:


df_weather = df.copy()


# In[192]:


df_weather.drop(['풍향'], axis = 1, inplace = True)


# In[193]:


df_weather


# ### df_weather CSV파일로 저장

# In[200]:


df_weather.to_csv("C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/weather.csv", sep = ',',encoding = 'cp949')

