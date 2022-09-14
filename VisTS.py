#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


data = pd.read_csv('AAPL.csv')
data.head


# In[12]:


data.tail


# In[13]:


type(data)


# In[14]:


data.info()


# In[15]:


data.describe()


# In[19]:


data['Date']


# In[17]:


data['Date'] = data['Date'].apply(pd.to_datetime)


# In[20]:


data['Date']


# In[21]:


pd.to_datetime('2021-09-14')


# In[22]:


data.info()


# In[25]:


data.set_index('Date' , inplace = True) 


# In[26]:


data.head()


# In[30]:


data['Open'].plot()


# In[31]:


data['Close'].plot()


# In[32]:


data.head()


# In[ ]:




