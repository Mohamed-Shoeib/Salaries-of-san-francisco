#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv('Salaries.csv')


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


df.describe()


# In[10]:


df['BasePay']


# In[12]:


df['BasePay'] = df['BasePay'].replace('not provided', pd.NA)


# In[20]:


df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[21]:


df


# In[38]:


df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName']


# In[40]:


df[df['TotalPayBenefits'] == df['TotalPayBenefits'].min()]


# In[44]:


df.groupby('Year').mean()


# In[46]:


df['JobTitle'].unique()


# In[51]:


df['JobTitle'].value_counts().tail(10)


# In[57]:


(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1).sum()


# ## How many people have the word chief in their job title ? ('This is pretty Tricky')

# In[77]:


def chief(string):
    if 'chief' in (string.lower()):
        return True
    else:
        return False


# In[78]:


chief('DEPUTY CHIEF OF DEPARTMENTFIRE DEPARTMENT')


# In[79]:


df['JobTitle'].apply(lambda x :chief(x))


# In[80]:


(df['JobTitle'].apply(lambda x :chief(x))).sum()


# In[82]:


df['JobTitle'].apply(len)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




