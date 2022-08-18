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


# In[18]:


from scipy.stats import norm
p=.95
value=norm.ppf(p)
print(value)


# In[19]:


import pandas as pd
from scipy import stats


# In[20]:


df1=pd.read_csv("C/DataScience/out.csv")
df1


# In[23]:


stats.ttest_rel(df1['0'],df1['1'])


# In[29]:


import pandas as pd
import numpy as np
path = path = 'C:\DataScience\C\DataScience'
filename = 'out'
df2 = pd.read_csv(path+'\\'+filename+'.csv')
df2.rename(columns={'0':'x'},inplace=True)
expected_value = lambda values: sum(values)/len(values)
standard_deviation = lambda values,expected_value: np.sqrt(sum([(v - expected_value)**2 for v in values])/len(values))


# In[35]:


exp = expected_value(df2['x'])
std_d = standard_deviation(df2['x'],exp)
print(f'Expected Value : {exp},Standard deviation : {std_d}')


# In[33]:


df2['Z_Score'] = (df2['x'] - exp)/std_d
import matplotlib.pyplot as plt
plt.hist(df2['Z_Score'])
plt.xlabel('Z_Score')
plt.title('Z_Score of Normal Distribution')
plt.show()


# In[34]:


import scipy.stats as stats
z_score = stats.zscore(df2['x'])
import matplotlib.pyplot as plt
plt.hist(z_score)
plt.xlabel('Z_Score')
plt.title('Z_Score of Normal Distribution')
plt.show()


# In[ ]:




