#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd


# #### 1. 선박 위치에서 가장 가까운 관측소 매칭 데이터(nearest_obs), 관측소 시간별 해양기상데이터 (weather_obs) 불러오기

# In[206]:


nearest_obs = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/obs-course.csv',sep=',', encoding = 'cp949',  index_col = 0)
weather_obs = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/weather.csv', sep=',' , encoding = 'cp949',  index_col = 0)


# #### 2. 선박 위치에서 가장 가까운 관측소 매칭 데이터(nearest_obs) 전처리

# **2-1) nearest_obs 확인**

# In[207]:


nearest_obs


# **2-2) dataFrame join을 위해 컬럼명 바꾸기**
# 
# - key: '시간', '관측소명'

# In[208]:


nearest_obs.columns = ['MMSI', '시간', '선박위도', '선박경도', '선박속도', 'geometry', '관측소명']


# **2-3) '시간'컬럼 데이터타입 바꿔주기**
# 
# - object to datetime

# In[209]:


nearest_obs['시간'] = pd.to_datetime(nearest_obs['시간'])
nearest_obs


# #### 3. 관측소 시간별 해양기상데이터 (weather_obs) 전처리

# **3-1) weather_obs 확인**

# In[210]:


weather_obs


# **3-2) dataFrame join을 위해 컬럼명 바꾸기**
# 
# - key: '시간', '관측소명'

# In[211]:


weather_obs.columns = ['관측소명', '시간', '관측소위도', '관측소경도', '조위(cm)', '풍속(m/s)', '풍향(deg)', '기온(℃)', '기압(hPa)']


# **3-3) '시간'컬럼 데이터타입 바꿔주기**
# 
# - object to datetime

# In[212]:


weather_obs['시간'] = pd.to_datetime(weather_obs['시간'])


# #### 4. dataFrame left join 시키기
# 
# - weather_nearest_obs = pd.merge(nearest_obs, weather_obs, ...)
# - on = ('관측소명', '시간)  # 키값
# - how = 'left'  # join 형태 정하기
# - indicator = True  # 해당 컬럼의 값이 어느 데이터프레임을 반영했는지

# In[233]:


weather_nearest_obs = pd.merge(nearest_obs, weather_obs, on = ('관측소명','시간'), how = 'left', indicator = True)
weather_nearest_obs


# In[250]:


weather_nearest_obs.info()


# #### 5. join된 데이터프레임에서 필요없는 컬럼 drop

# In[231]:


weather_nearest_result = weather_nearest_obs.drop(['geometry','관측소위도', '관측소경도', '_merge'], axis = 1)


# In[232]:


weather_nearest_result


# #### 6. 입출항 데이터와 합치기 위해 MMSI 타입을 object로 통일시킨다
# - 실제 도착시간, 선박용도, 총톤수, 전출항지를 학습데이터셋 feature로 만들기 위해서 합쳐야함

# In[261]:


weather_nearest_result['MMSI'] = weather_nearest_result['MMSI'].astype(str)


# #### 7. 선박용도, 전출항지, 총톤수, 전출항지 연결(from portmis, mmsi)

# In[259]:


portmis = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/portmis.csv',sep=',', encoding = 'cp949',  index_col = 0)


# In[260]:


portmis


# In[251]:


portmis.info()


# #### 8. portmis 데이터프레임에서 필요없는 컬럼 drop

# In[302]:


dt_portmis = portmis.drop(['항명','호출부호', '선명', '구분', '외내', '입출', '출항일시'], axis = 1)
dt_portmis


# #### 9. dt_portmis 컬럼명 변경 
# 기존 weather_nearest_result 데이터프레임과 join 하기 위해서 키값("MMSI")을 통일시킨다

# In[290]:


dt_portmis.columns = ['MMSI', '총톤수', '실제도착일시', '전출항지', '선박용도']


# #### 10. join한 데이터 프레임(weather_nearest_result, dt_portmis)

# In[294]:


dataset = pd.merge(weather_nearest_result, dt_portmis, on = 'MMSI', how = 'left')


# In[295]:


dataset


# In[296]:


dataset.info()


# #### 11. 입항일시(실제도착일시) 컬럼명 변경(from portmis, mmsi)

# In[303]:


pd.to_datetime(dataset['실제도착일시'])


# In[305]:


dataset


# #### 12. 학습 dataset csv파일로 저장

# In[306]:


dataset.to_csv("C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/dataset.csv", sep = ',',encoding = 'cp949')

