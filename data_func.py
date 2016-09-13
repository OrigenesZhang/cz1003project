#!/usr/local/bin/python3
# _*_ coding:utf8 _*_

import requests
import time
from bs4 import BeautifulSoup

def html():
    main_url = ['http://ipsmold.wicp.io:81/' ,'http://103.244.103.154/']
    login_url =['http://ipsmold.wicp.io:81/login/x', 'http://103.244.103.154/login/x']
    url = ['http://ipsmold.wicp.io:81/Network/ac_user',"http://103.244.103.154/Network/ac_user"]
    payload={'user':'temp','pass':'4&4+?rpw%akU!AKG'}
    s = requests.Session()
    number = []
    for i in range(len(url)):
        s.get(main_url[i])
        s.post(login_url[i],data=payload)
        r = s.get(url[i])
        html_markup = BeautifulSoup(r.text,'html.parser')
        number.append(len(html_markup.find_all('dd')) - 1)

    with open('database','r+') as f:
        old = f.read()
        f.seek(0)
        new_data = time.strftime("%m-%d,%H:%M:%S",time.localtime())+','
    #print(time.strftime("%m-%d,%H:%M:%S",time.gmtime()),file=data,end=',')
        for i in range(len(number)):
            if i == 0:
                new_data = new_data + str(number[i]) + ',' 
            elif i == 1:
                new_data = new_data + str(number[i]) + '\n'
        f.write(new_data + old)     
    
    return number

def extract(n):
    line = []
    count = n
    data = open('database','r')
    for i in data:
        if n < 1 :
            break
        tmp = i.replace('\n','').split(',')
        line.append(tmp)
        n-=1
    return line

def ma_A(periods):
    data = extract(periods)
    weight,avg=periods,0
    for i in data:
        avg+=(int(i[3])*weight)
        weight-=1
        if weight == 0:
            break
    avg= 2 * avg / (periods*(periods+1))
    return int(avg)

def ma_B(periods):
    data = extract(periods)
    weight,avg=periods,0
    for i in data:
        avg+=(int(i[2])*weight)
        weight-=1
        if weight == 0:
            break
    avg= 2 * avg / (periods*(periods+1))
    return int(avg)
