#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('income.csv')


# In[58]:


plt.figure(figsize=(10, 10))
plt.scatter(df['age'], df['hours-per-week'], alpha=0.2, s=10)

df_iran = df[df['native-country']=='Iran']
plt.scatter(df_iran['age'], df_iran['hours-per-week'], alpha=0.4, color='red', s=50, label='Iran')

plt.xlabel('age')
plt.ylabel('hours-per-week')
plt.legend();


# In[33]:


(df[df['race'] == 'Black'].groupby('native-country').sum() / df.groupby('native-country').sum())['age']


# In[57]:


plt.figure(figsize=(12, 6))
summary = pd.DataFrame()
summary['blacks-percentage'] = (df[df['race'] == 'Black'].groupby('native-country').sum()['age'] / df.groupby('native-country').sum()['age']).fillna(0) * 100
summary = summary.sort_values('blacks-percentage', ascending=False)

plt.bar(summary.head(5).index, summary.head(5)['blacks-percentage'])
plt.xlabel('country')
plt.ylabel('percentage of black workers');

