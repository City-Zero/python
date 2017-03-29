#!/usr/bin/env python3
# coding=utf-8
#使用元组，内容不可变
t1 = ('people',189,19.3)

#使用列表，内容可变
t2 = [1,3,5]
t3 = ['abc',t2,12.5]
print("%d + %d" % (len(t2),len(t3)))
#列表的一些方法 append(),insert(),pop()
print(t3[1])
t2.append(123)
print(t2)
t2.insert(1,"lyt")
print(t2)
t2.pop();
print(t2)
t2.pop(0)
print(t2)
