#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:23:24 2017

@author: lixiang
"""
 
import requests
import urllib
import json
import time
import prettytable
import sys
import math

#进度条
def view_bar(cur, total):
    percent = '{:.2%}'.format(cur / total)  
    sys.stdout.write('\r')  
    sys.stdout.write('抓取进度:'+'[%-50s] %s'% ( '=' * int(math.floor(cur * 50 /total)),percent))
    sys.stdout.flush()  
    if cur == total:  
        sys.stdout.write('\n')  
time_start=time.time()
# 榜单歌曲批量下载
# r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')  #网易原创歌曲榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=19723756')  #网易飙升歌曲榜
# r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  #网易热歌榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')  #新歌榜
 
# 歌单歌曲批量下载
r = requests.get('http://music.163.com/api/playlist/detail?id=123415635')   # 云音乐歌单——【华语】中国风的韵律，中国人的印记
# r = requests.get('http://music.163.com/api/playlist/detail?id=122732380')# 云音乐歌单——那不是爱，只是寂寞说的谎
 
html=r.content.decode('utf-8')
arr=json.loads(html)
totalmusic=len(arr['result']['tracks'])
total=0
table=prettytable.PrettyTable()
table.field_names=['排名','歌名','歌手']
for i in range(totalmusic):        # 遍历
    name = str(i+1)+'.'+arr['result']['tracks'][i]['name'] +'-'+arr['result']['tracks'][i]['artists'][0]['name']+ '.jpg'
    link = arr['result']['tracks'][i]['album']['picUrl']
    urllib.request.urlretrieve(link,'/Users/lixiang/Desktop/网易云抓取/'+name)        # 提前要创建文件夹，在此文件目录下创建“网易云音乐”文件夹
    total=total+1
    table.add_row([i+1,arr['result']['tracks'][i]['name'],arr['result']['tracks'][i]['artists'][0]['name'],]) 
    view_bar(total, totalmusic)
    #print(str(100*(total/totalmusic))+'%')  
print (table)
#显示爬虫历时
time_end=time.time()
print('耗时：%.2f'%(time_end-time_start)+'s')