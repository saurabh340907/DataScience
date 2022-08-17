#!/usr/bin/env python
# coding: utf-8

# In[6]:


def mode(listS):
    from scipy.stats import mode
    mod = mode(listS)
    return(mod[0])


# In[7]:


def average(listS):
    total = sum(listS)
    n = len(listS)
    average= total/n
    return(average)


# In[8]:


def std_dev(listS):
    import numpy as np
    from math import sqrt
    listS = np.array(listS)
    x = listS.mean()
    y = len(listS)
    num = np.repeat(0,len(listS))
    for i in range(0,y):
        num[i] = (listS[i]-x)**2
    var = sum(num)/y
    sd = sqrt(var)
    return(sd)


# In[20]:


def skewness(random):
    avg = average(random)
    mod = mode(random)
    sd = std_dev(random)
    skewness = (avg-mod)/sd
    return(int(skewness))


# In[23]:


random = np.random.normal(loc=0,scale=1,size=500)
    skewness(random)


# In[ ]:





# In[ ]:




