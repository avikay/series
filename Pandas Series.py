#!/usr/bin/env python
# coding: utf-8

# # Different ways of using Series in Pandas

# In[2]:


import numpy as np 
import pandas as pd


# In[3]:


labels =['a','b','c']
my_data = [10,20,30]
ar = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}


# In[11]:


#series with normal python list(my_data)
pd.Series(data=my_data)


# ### pd.Series(data,index)

# In[10]:


#replacing the original index with another list(here labels)
pd.Series(data=my_data, index=labels)


# In[12]:


pd.Series(my_data,labels)


# In[13]:


#series with numpy arrays(ar)
#series works same for numpy arrays as that of python list
pd.Series(ar)


# In[14]:


pd.Series(ar,labels)


# In[17]:


#using dictionary to create a series
pd.Series(d)#it will automatically take key as index and values as data in the case of dictionary


# ### Built-in functions in Series

# In[18]:


pd.Series(data=[print,sum,len])


# In[19]:


#creating series directly
sr1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])


# In[21]:


sr2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])


# In[22]:


sr2


# In[23]:


sr1['USA']


# In[25]:


sr2['Italy']


# In[29]:


#creating objects(char or string) as data
sr3 = pd.Series(data=labels)


# In[28]:


sr3[2]


# In[30]:


sr1+sr2


# In[ ]:




