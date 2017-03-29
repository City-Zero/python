#!/usr/bin/env python
# coding=utf-8

import urllib.parse
import urllib.request
import random
suc = 0
fail = 0
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
for i in range(99999999999):
    u = ""
    for j in range(random.randint(6,10)):
        u+=chars[random.randint(0,len(chars)-1)]
        values = {"u":u+"@qq.com","p":u,"hiddenToken":"1058DC547B9D33882C41495AB140D4"}
    date = urllib.parse.urlencode(values).encode(encoding='UTF8')
    url = "http://www.appledneois.com/Home/Save"
    request = urllib.request.Request(url,date)
    response = urllib.request.urlopen(request)
    page = response.read().decode("utf8")
    if(i%9 == 0):
        print("当前第",i)
