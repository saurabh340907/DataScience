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





# In[6]:


#Bar plot
plt.bar(age_x,devop,label="All deveop")
plt.bar(age_x,javadop,label="All Java dop ")
plt.xlabel("Age")
plt.ylabel("Median Salary (USD)")
plt.legend()
plt.show()


# In[7]:


# Scattered
plt.scatter(age_x,devop,label="All deveop")
plt.scatter(age_x,javadop,label="All Java dop")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.legend()
plt.show()


# In[23]:



import pandas as pd
 
# intialise data of lists.
data = {'age_x' :[25,26,27,29,33,32,35,28,35,39],
'devop' :[3525,3326,3627,3129,3633,3032,3115,3628,3435,3009],
'javadop' :[4525,5326,5627,5129,5633,5032,6115,6628,6435,6009]}
 
# Create DataFrame
df4 = pd.DataFrame(data)
 
# Print the output.
print(df4)


# In[25]:



import pandas as pd
import matplotlib.pyplot as plt
 

 
# hostogram of total_bills
plt.hist(data['age_x'])
plt.hist(data['devop'])
plt.hist(data['javadop'])
 
plt.title("Histogram")
 
# Adding the legends
plt.show()


# In[26]:



# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
 
# draw lineplot
sns.lineplot(x="age_x", y="javadop", data=data)
 
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')
 
plt.show()


# In[ ]:




