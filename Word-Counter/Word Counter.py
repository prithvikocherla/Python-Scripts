#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from collections import OrderedDict

df = pd.read_csv('input.txt', header=None)
df=df[0]

text_list = []
for i in df:
    words = i.split()
    for x in words:
        text_list.append(x)  


# In[2]:


dict_words = {}
for i in text_list:
    dict_words.update({i:text_list.count(i)})
dict_words_sorted = OrderedDict(sorted(dict_words.items(), key=lambda x: x[1], reverse=True))


# In[7]:


def freqcount(x):    
    for x, y in list(dict_words_sorted.items())[0:x]:
        print("{}: {}".format(x,y))


# In[8]:


var = input('Please specify the number of top words to be displayed: ')
print("")
freqcount(int(var))


# In[ ]:




