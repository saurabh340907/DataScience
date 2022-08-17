#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from scipy import stats


# In[10]:


df=pd.read_csv("Hypothesis.csv")
df


# In[11]:


stats.ttest_rel(df['Before Class'],df['After Class'])


# In[ ]:





# In[ ]:




