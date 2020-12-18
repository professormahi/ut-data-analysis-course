#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.random.seed(0)
a=np.random.randn(10,3)


# In[8]:


a


# In[3]:


distance_mat = np.linalg.norm(a[:, None, :] - a[None, :, :], axis=-1)


# In[9]:


distance_mat


# In[10]:


nn = distance_mat.argmax(axis=0)
print(nn)

