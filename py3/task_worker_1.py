#!/usr/bin/env python
# coding=utf-8

import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只能从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

def jiecheng(a):
    s = 1
    for i in range(1,a+1):
        s *= i
    return s

#连接到服务器
server_addr = '127.0.0.1'
print('连接到服务%s...' % server_addr)
#端口号及验证码
m = QueueManager(address=(server_addr,5050),authkey=b'abc')
#网络连接
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
#从task队列取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('运行任务%d!...' % n)
        r = '%d! = %d' % (n,jiecheng(n))
#        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('任务队列空了。')
print('work exit.')
