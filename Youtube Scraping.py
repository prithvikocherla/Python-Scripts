#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
import requests
from pytube import YouTube
import pytube

base = "https://www.youtube.com/results?search_query="
string = "video-name"
qstring = urllib.parse.quote(string)

r = requests.get(base+qstring)

page = r.text
soup=bs(page,'html.parser')
soup

vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
vids

videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)

videolist
yt = YouTube(videolist[0])
yt.streams.filter(progressive=True).first().download()
