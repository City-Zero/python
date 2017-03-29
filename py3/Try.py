#!/usr/bin/env python
# coding=utf-8

a = int(input());

try:
    print('start trying...')
    r = 10 / a
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('error!')
print('END')
