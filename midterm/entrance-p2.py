#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


df = pd.read_csv('income.csv')


# In[64]:


df


# In[60]:


new_table = pd.DataFrame()
new_table["count"] = df.groupby('native-country').count()['age']
new_table["average-hours-per-week"] = df.groupby('native-country').mean()['hours-per-week']

males_females = pd.DataFrame()
males_females['males'] = df[df['gender']=='Male'].groupby(['native-country']).count()['age']
males_females['females'] = df[df['gender']=='Female'].groupby(['native-country']).count()['age']
# males_females[males_females['gender'] == 'Female'] / males_females.groupby('native-country').sum()
males_females['percentage'] = males_females['females'] / (males_females['females'] + males_females['males']) * 100
new_table['female-percentage'] = males_females['percentage']


# In[63]:


print(new_table)

