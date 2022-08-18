#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


# In[4]:


age_x=[25,26,27,29,33,32,35,28,35,39]
devop=[3525,3326,3627,3129,3633,3032,3115,3628,3435,3009]
javadop=[4525,5326,5627,5129,5633,5032,6115,6628,6435,6009]
age_x.sort()
devop.sort()
javadop.sort()
plt.plot(age_x,devop,marker="*",label="All deveop")
plt.plot(age_x,javadop,marker="*",label="All Java dop ")
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.legend()


# In[ ]:





# In[ ]:




