# -*- coding: utf-8 -*-


import requests
import json
import random
import time
!pip install --target=$nb_path googletrans==4.0.0-rc1

from googletrans import Translator

# 原author : 二娃玩转区块链
# 修改：CaoYu
# 视频教程在：YouTube ：https://www.youtube.com/watch?v=XQfhTPm_FJo
# ➡️ 进discord 更多优质内容 ： https://discord.com/invite/RHtf7V6Z5G
# 作者更多优质内容：https://linktr.ee/erwaplayblockchain 
# 获取auth的方法： https://mirror.xyz/0x0000e21205A18756534E904c94D3961BF6000000/BOw8fZJm5LfdShdQ5tYg96pYQeXXEmDtCkL99GCoQqc

def get_context(auth,chanel_id):
    #从给定的channel list里面随机取出100条信息
    headr = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = random.choice(chanel_list)
    url = "https://discord.com/api/v9/channels/{}/messages?limit=50".format(chanel_id)
    print(url)
    res = requests.get(url=url, headers=headr)
    #对取出来的信息进行筛选
    result = json.loads(res.content)
    result_list = []

    keywords = '<,@,http,?,？,吗,！,!,mint,通知,我,你,他,她'  # 这个可以后续再补充————————————————————————————————————————————————————
    
    for context in result:
      count = sum([1 if w in context['content'] and w else 0 for w in keywords.split(',')])
      if count==0 and len(context['content'])<10:
        result_list.append(context['content'])
        
    
    #将信息进行翻译再翻译，通过googletrans库
    translator = Translator(service_urls=['translate.google.com'])
    translation01 = random.choice(result_list)
    
    translation02 = translator.translate(translation01,dest='ko')

    translation03 = translator.translate(translation02.text,dest='en')
    #这个地方如果需要明确发言内容，添加以下语句——————————————————————————————————————————————————
    #translation03 = '需要指定的发言';

    return translation03.text
    



def chat(chanel_list,authorization):
      header = {
          "Authorization": authorization,
          "Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      }
      for chanel_id in chanel_list:
          msg = {
              "content": get_context(authorization,chanel_id),
              "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
              "tts": False,
          }
          url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
          try:
              res = requests.post(url=url, headers=header, data=json.dumps(msg))
              print(res.content)
          except:
              pass
          continue
      time.sleep(random.randrange(1, 3))#这个是在不同频道之间发言的间隔，应该没有什么关系


if __name__ == "__main__":
    chanel_list = [""]  # 这里是群聊号（url最右边）
    authorization_list = "" # 这里auth认证信息
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(500, 600) #发送间隔时间(秒)，这是在频道里面灌水的时间间隔，比较关键————————————————————————————————
            time.sleep(sleeptime)
        except:
            break