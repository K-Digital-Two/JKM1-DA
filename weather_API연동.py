#!/usr/bin/env python
# coding: utf-8

# In[103]:


import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import csv


# In[157]:


pip install schedule


# In[220]:


DataType = "tideObsRecent"
ObsCode = ['DT_0001', 'DT_0002', 'DT_0008', 'DT_0017', 'DT_0043','DT_0050', 'DT_0052', 'DT_0065']

for i in range(len(ObsCode)):
    # JSON 데이터에 액세스
    if  url.status_code == 200:
        url = requests.get(f"http://www.khoa.go.kr/api/oceangrid/tideObsRecent/search.do?ServiceKey=nQJTgh8TKrnNus3V0Ipeng==&ObsCode={ObsCode[i]}&ResultType=json")
        text = url.text
        data = json.loads(text)
        print("ObsCode", data, df)    
    else:
        print("null")
    df = pd.json_normalize(data['result']['data'])


    print()

