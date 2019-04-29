#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import urllib.request
import pandas as pd


# In[2]:


sauce = urllib.request.urlopen('https://www.python.org/').read()


# In[3]:


sauce


# In[4]:


soup = bs.BeautifulSoup(sauce,'lxml')


# In[5]:


soup


# In[6]:


soup.title


# In[7]:


soup.title.name


# In[8]:


soup.title.text


# In[9]:


soup.p


# In[10]:


soup.find_all('p')


# In[11]:


for p in soup.find_all('p'):
    print(p.text)


# In[12]:


soup.get_text()


# In[13]:


for url in soup.find_all('a'):
    print(url.get('href'))


# In[14]:


body = soup.body
for p in body.find_all('p'):
    print(p)


# In[15]:


for div in soup.find_all('div'):
    print(div.text)


# In[16]:


for div in soup.find_all('div', class_=body):
    print(div.text)


# In[17]:


soup.find_all('a')


# In[18]:


table = soup.table


# In[19]:


table


# In[20]:


soup.find('table')


# In[21]:


table_rows = table.find_all('tr')


# In[22]:


for tr in table_rows:
    td = tr.find_all('td')
    row =[i.text for i in td]
row


# In[23]:


df = pd.read_html('https://www.python.org/', header=0)


# In[24]:


print(df)


# In[25]:


for url in soup.find_all('loc'):
    print(url.text)


# In[ ]:




