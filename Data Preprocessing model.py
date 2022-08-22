#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('Data.csv')


# In[3]:


x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


# In[4]:


print(x)


# In[5]:


print(y)


# In[6]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])


# In[7]:


print(x)


# In[8]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers =[('encoder', OneHotEncoder(), [0])] ,remainder = 'passthrough')
x = np.array(ct.fit_transform(x))
print(x) 


# In[9]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)


# In[10]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x, y, test_size = 0.2, random_state=1)


# In[11]:


print(x_train)


# In[12]:


print(x_test)


# In[13]:


print(y_train)


# In[14]:


print(y_test)


# In[ ]:




