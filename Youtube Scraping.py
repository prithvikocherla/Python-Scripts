#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests


# In[53]:


base = "https://www.youtube.com/results?search_query="
qstring = "video-name"


# In[54]:


r = requests.get(base+qstring)


# In[55]:


page = r.text
soup=bs(page,'html.parser')


# In[56]:


soup


# In[57]:


vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})


# In[58]:


vids


# In[59]:


videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)


# In[60]:


videolist


# In[61]:


from pytube import YouTube
import pytube


# In[ ]:


yt = YouTube(videolist[0])


# In[87]:


yt.streams.filter(progressive=True).first().download()


# In[ ]:





# In[ ]:




