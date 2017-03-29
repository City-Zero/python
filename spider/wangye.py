#!/usr/bin/env python
# coding=utf-8

import urllib.parse
import urllib.request
import random
import re
zh="先帝创业未半而中道崩殂今天下三分益州疲弊此诚危急存亡之秋也然侍卫之臣不懈于内忠志之士忘身于外者盖追先帝之殊遇欲报之于陛下也诚宜开张圣听以光先帝遗德恢弘志士之气不宜妄自菲薄引喻失义以塞忠谏之路也宫中府中俱为一体陟罚臧否不宜异同若有作奸犯科及为忠善者宜付有司论其刑赏以昭陛下平明之理不宜偏私使内外异法也侍中侍郎郭攸之费祎董允等此皆良实，志虑忠纯是以先帝简拔以遗陛下愚以为宫中之事事无大小悉以咨之然后施行必能裨补阙漏有所广益将军向宠性行淑均晓畅军事试用于昔日先帝称之曰能是以众议举宠为督愚以为营中之事悉以咨之必能使行阵和睦优劣得所亲贤臣远小人此先汉所以兴隆也亲小人远贤臣此后汉所以倾颓也先帝在时每与臣论此事未尝不叹息痛恨于桓灵也侍中尚书长史参军此悉贞良死节之臣愿陛下亲之信之则汉室之隆可计日而待也臣本布衣躬耕于南阳苟全性命于乱世不求闻达于诸侯先帝不以臣卑鄙猥自枉屈三顾臣于草庐之中咨臣以当世之事由是感激遂许先帝以驱驰后值倾覆受任于败军之际奉命于危难之间尔来二十有一年矣先帝知臣谨慎故临崩寄臣以大事也受命以来夙夜忧叹恐托付不效以伤先帝之明故五月渡泸深入不毛今南方已定兵甲已足当奖率三军北定中原庶竭驽钝攘除奸凶兴复汉室还于旧都此臣所以报先帝而忠陛下之职分也至于斟酌损益进尽忠言则攸之祎允之任也愿陛下托臣以讨贼兴复之效不效则治臣之罪以告先帝之灵若无兴德之言则责攸之祎允等之慢以彰其咎陛下亦宜自谋以咨诹善道察纳雅言深追先帝遗诏臣不胜受恩感激今当远离临表涕零不知所言"
suc = 0
fail = 0
print("当前第",(suc+fail),"次,成功：",suc," 失败：",fail)
l = [i for i in zh]
s_l = len(l)
for i in range(99999):
    name = ""
    tel = "158"
    for j in range(random.randint(3,6)):
        name+=(l[random.randint(0,len(l)-1)])
    for k in range(8):
        tel+=str(random.randint(0,9))

    values = {"name":name,"tel":tel,"email":tel+"@qq.com"}

    date = urllib.parse.urlencode(values).encode(encoding='UTF8')
    url = "http://www.xiyounet.org/2017wangye/file_submit/php/signup.php"
    request = urllib.request.Request(url,date)
    response = urllib.request.urlopen(request)
    page = response.read().decode("utf8")
    ss = re.search("报名成功",page)
    if(ss):
        suc+=1
    else:
        fail+=1
    if(i % 21 == 0):
        print("当前第",(suc+fail),"次,成功：",suc," 失败：",fail)


print("共",(suc+fail),"次,成功：",suc," 失败：",fail)
