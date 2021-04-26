#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from IPython.display import display,HTML
get_ipython().run_line_magic('matplotlib', 'inline')
import datetime
import matplotlib.pyplot as plt


# In[2]:


#COVID SOURCE : https://github.com/CSSEGISandData/COVID-19


# # Covid19 Confirmed Global

# In[3]:


url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
covid19_confirmed_global = pd.read_csv(url)
covid19_confirmed_global.head()


# In[4]:


covid19_confirmed_global.nunique()


# In[5]:


covid19_confirmed_global.isna().sum()


# In[6]:


column_retain = ["Province/State","Country/Region","Lat","Long"]
ccg = covid19_confirmed_global.melt(id_vars = column_retain)


# In[7]:


ccg.rename(columns = {"variable":"Date","value":"Confirmed" },inplace = True)
ccg.head(10)


# In[8]:


ccg.Date = pd.to_datetime(ccg.Date,format='%m/%d/%y')
ccg.tail()


# In[9]:


Latest_date = ccg[ccg.Date == "2021-04-25"]
Latest_date.nunique()


# In[10]:


Latest_date.shape


# In[11]:


Latest_date.isna().sum()


# In[12]:


Latest_date["Country/Region"].value_counts()


# In[13]:


Latest_date[Latest_date["Country/Region"]== "China"].head()


# In[14]:


Latest_date_country = Latest_date.groupby("Country/Region").agg({"Confirmed":"sum"}).reset_index()
Latest_date_country.plot.bar(x = "Country/Region",y = "Confirmed" ,figsize=(20, 10))


# In[22]:


Latest_date_country = Latest_date_country.sort_values(["Confirmed"],ascending=False).head(10)
display(Latest_date_country)
plt.figure(figsize = (15,10))
plt.bar(Latest_date_country["Country/Region"],Latest_date_country["Confirmed"])

plt.xticks(rotation = 45)

plt.title("World Confirmed Cases")
plt.xlabel("County")
plt.ylabel("COVID 19")


# In[16]:


country_date_confirmed = ccg.groupby(by = ["Country/Region","Date"]).agg({"Lat":"first","Long":"first","Confirmed":"sum"}).reset_index()
country_date_confirmed.tail()


# # INDIA COVID 19

# In[17]:


India = country_date_confirmed[country_date_confirmed["Country/Region"] == "India"]
display(India.tail())


# In[18]:


India.nunique()


# In[19]:


India.plot.line(x = 'Date' ,y = 'Confirmed',)


# In[ ]:




