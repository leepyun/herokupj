#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import telegram
import time
import os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[10]:


bot = telegram.Bot(token='1718079986:AAGLLEjAZPhPh-xPhyQtRt4s_0NdDPmhFf4')
me = bot.getMe()
print(me)


# In[26]:


updates = bot.getUpdates()
print(updates)


# In[28]:


for i in updates:
    print(i)
    
print('start telegram chat bot')


# In[29]:


bot.sendMessage(chat_id = '1642486508', text = "Hello World")


# In[32]:



if __name__ == '__main__':

    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    while True:
        req = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("tr", {"class" : "list1"})
        post_num = posts.find("td", {"class" : "eng list_vspace"}).text


        # 제일 최신 게시글 번호와 30초 마다 크롤링한 첫번째 게시글의 번호 비교
        # 비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        if latest_num != post_num :
            latest_num = post_num
            link = 'http://www.ppomppu.co.kr/zboard/'+posts.find("td", { "valign" : "middle"}).find("a").attrs['href']
            title = posts.find("font", {"class" : "list_title"}).text

            text = '<뽐뿌 게시글 업데이트>'+'\n'+title+'\n'+link  
            bot.sendMessage(1642486508, text)
            # 프롬프트 로그
            print(post_num)
            print(title)
            print(link)
        time.sleep(30) # 30초 간격으로 크롤링
        print('bot 동작 중 현재 게시글 번호' + latest_num)


# In[ ]:




