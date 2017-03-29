#!/usr/bin/env python
# coding=utf-8

import http.cookiejar
import urllib.request

filename = 'cookie'
#声明一个CookieJar对象实例来保存cookie
#cookie = http.cookiejar.CookieJar()
cookie = http.cookiejar.MozillaCookieJar(filename)
#利用urllib库创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)

cookie.save(ignore_discard=True,ignore_expires=True)

