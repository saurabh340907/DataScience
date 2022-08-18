#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import random

x= random.normal(size=(2,3))

print (x)


# In[12]:


import pandas as pd
df = pd.DataFrame(x)


# In[13]:


df


# In[14]:


df.to_csv(index=False)


# In[15]:


from pathlib import Path  
filepath = Path('C/DataScience/out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)


# In[17]:


pd.read_csv('C/DataScience/out.csv')  


# In[ ]:




