#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import geopandas as gpd
from shapely.ops import nearest_points


# #### 1. 항로데이터, 관측소 데이터 가져오기
# https://rightstone032.tistory.com/8

# In[34]:


ship = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/info.csv',sep=',', encoding = 'cp949')
obs = pd.read_csv('C:/Users/user/Desktop/항만운영정보시스템data/ModelingDataset/weather.csv', sep=',' , encoding = 'cp949', index_col = 0)


# #### 2. 가져온 데이터 geopandas로 바꾸기

# In[35]:


ship = gpd.GeoDataFrame(ship, geometry=gpd.points_from_xy(ship['shipLat'], ship['shipLon']))
obs = gpd.GeoDataFrame(obs, geometry=gpd.points_from_xy(obs['위도'], obs['경도']))


# #### 3. geopandas로 바꾼 데이터 위도,경도를 geometry point 로 변환
# 두 getodataFrame의 epsg를 설정해준다

# In[36]:


ship.set_crs(epsg = 4326, inplace = True)


# In[37]:


obs.set_crs(epsg = 4326, inplace = True)


# #### 4. 가장 가까운 좌표 찾는 함수
# https://m.blog.naver.com/jokercsi1/222404117201

# In[38]:


def get_nearest_values(row, other_gdf, point_column='geometry', value_column="geometry"):
    """Find the nearest point and return the corresponding value from specified value column."""
    
    # Create an union of the other GeoDataFrame's geometries:
    other_points = other_gdf["geometry"].unary_union
    
    # Find the nearest points
    nearest_geoms = nearest_points(row[point_column], other_points)
    
    # Get corresponding values from the other df
    nearest_data = other_gdf.loc[other_gdf["geometry"] == nearest_geoms[1]]
    
    nearest_value = nearest_data[value_column].values[0]
    
    return nearest_value


# #### 4-1) 멀티포인트: shapely의 nearest_points처럼 사용하기 위해서
# unary_union: geometry 데이터의 합집합

# In[39]:


unary_union = obs.unary_union
print(unary_union)


# #### 5. get_nearest_values 함수를 적용시켜 가장 가까운 관측소 좌표 출력하기

# In[40]:


ship["가장가까운관측소"] = ship.apply(get_nearest_values, other_gdf=obs, point_column="geometry", axis=1)


# In[41]:


ship.head()


# #### 6. 가장 가까운 관측소의 이름으로 바꿔 출력하기

# In[42]:


ship["가장가까운관측소"] = ship.apply(get_nearest_values, other_gdf=obs, point_column="geometry", value_column="관측소명", axis=1)

ship.head()


# #### 7. 추출한 geopandas dataframe을 csv로 저장

# In[44]:


ship.to_csv('C:/Users/user/Desktop/항만운영정보시스템data/obs-course.csv', encoding = 'cp949', sep=",")

