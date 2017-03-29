#!/usr/bin/env python
# coding=utf-8

import urllib.parse
import urllib.request

request = urllib.request.Request("http://www.flycold.cn/python/test_post.html")
response = urllib.request.urlopen(request)
page = response.read().decode("utf8")
print (page)


values = {"username":"www.flycold.cn","passwd":"python"}
date = urllib.parse.urlencode(values).encode(encoding='UTF8')
url = "http://www.flycold.cn/python/check.php"
request = urllib.request.Request(url,date)
response = urllib.request.urlopen(request)
page = response.read().decode("utf8")
print(page)


values = {"username":"www.flycold.cn","passwd":"python"}
date = urllib.parse.urlencode(values)
url = "http://www.flycold.cn/python/check.php"
get_url = url + "?" + date
request = urllib.request.Request(get_url)
response = urllib.request.urlopen(request)
page = response.read().decode("utf8")
print(page)
