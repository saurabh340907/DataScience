#!/usr/bin/env python
# coding: utf-8

# In[15]:


def SD_VAR(listA):
    import numpy as np
    from math import sqrt
    listA = np.array(listA)
    m = listA.mean()
    n = len(listA)
    num = np.repeat(0,len(listA))
    for i in range(0,n):
        num[i] = (listA[i]-m)**2
    var = sum(num)/n
    sd = sqrt(var)
    return(var,sd)


# In[16]:


num_list = [4,5,2,4,5,6,2,5]
v,s = SD_VAR(num_list)


# In[17]:


print (v)


# In[18]:


print (s)


# In[ ]:




