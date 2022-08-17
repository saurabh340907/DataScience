#!/usr/bin/env python
# coding: utf-8

# In[9]:


def SD_VAR(listX):
    import numpy as np
    from math import sqrt
    listX = np.array(listX)
    m = listX.mean()
    n = len(listX)
    num = np.repeat(0,len(listX))
    for i in range(0,n):
        num[i] = (listX[i]-m)**2
    var = sum(num)/n
    sd = sqrt(var)
    return(var,sd)


# In[10]:


num_list = [4,5,2,4,5,6,2,5]
v,s = SD_VAR(num_list)


# In[11]:


print (v)


# In[12]:


print (s)


# In[ ]:




