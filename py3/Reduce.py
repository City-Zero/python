#!/usr/bin/env python3
# coding=utf-8
#from functools import reduce
def fu(x,y):
    return x*10 + y
l=[1,4,5,0]
print (reduce(fu,l))

#用map将用户输入的不规范英文姓名，改为首字母大写
L1 = ['adam', 'LISA', 'barT']
def normalize(str):
    str = str.lower();
    return str[0].upper()+str[1:]
L2 = list(map(normalize, L1))
print(L2)

#字符串转浮点数
def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    l = s.split('.',1)
    x = reduce(fu,map(char2num,l[0]))
    y = reduce(fu,map(char2num,l[1]))
    return x+y*pow(0.1,len(l[1]))
print(str2float('123.45'))

