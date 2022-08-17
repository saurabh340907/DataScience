#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


df = pd.DataFrame({'Observed':[41,99],'Expected':[13,87]})


# In[13]:


def chi_sq(data,Observed,Expected):
    data['result']=((df[Observed]-df[Expected])**2)/df[Expected]
    chisq = sum(data['result'])
    return(chisq)


# In[14]:


calculated_chi_value = chi_sq(df,'Observed','Expected')


# In[15]:


calculated_chi_value


# In[16]:


chi_value = 3.84
alpha = 0.05


# In[17]:


if calculated_chi_value > chi_value:
    print(f"Significant diffrence in observed and actual data at {alpha} LOS ")
else:
    print(f"No Significant diffrence in observed and actual data at {alpha} LOS ")


# In[ ]:




