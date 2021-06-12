#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


students = ['Karteek','Sowjanya','Kiran','Madhuri']


# In[3]:


pd.Series(students)


# In[4]:


numbers = [1,2,3,4]
pd.Series(numbers)


# In[5]:


students = ['Karteek','Sowjanya','Kiran',None]


# In[6]:


pd.Series(students)


# In[7]:


numbers = [1,2,3,None]
pd.Series(numbers)


# In[11]:


import numpy as np


# In[12]:


np.nan ==None


# In[13]:


np.nan == np.nan


# In[14]:


np.isnan(np.nan)


# In[15]:


student_scores = {'Karteek': 'Physics',
                 'Sowjanya': 'Biology',
                 'Madhuri': 'English'}


# In[16]:


s = pd.Series(student_scores)


# In[17]:


s


# In[19]:


s.index


# In[20]:


students=[('Karteek','Yadavilli'),('Sowjanya','Mangalampalli')]


# In[21]:


pd.Series(students)


# In[22]:


pd.Series(['Karteek','Sowjanya'], index = ['Yadavilli','Mangalampalli'])


# In[25]:


pd.Series(['Karteek','Sowjanya','Madhuri'], index = ['Yadavilli','Mangalampalli','Yadavilli'])


# In[26]:


student_scores = {'Karteek': 'Physics',
                 'Sowjanya': 'Biology',
                 'Madhuri': 'English'}


# In[27]:


s = pd.Series(student_scores,index = ['Karteek','Madhuri','Kiran'])
s


# In[ ]:




