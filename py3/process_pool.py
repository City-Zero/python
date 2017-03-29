#!/usr/bin/env python3
# coding=utf-8

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('运行任务 %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务%s运行了%0.2f秒。' % (name,(end-start)))

if __name__ == '__main__':
    print('父进程 %s。' % os.getpid())
    p = Pool(512)
    for i in range(10240):
        p.apply_async(long_time_task,args=(i,))
    print('等待所有子进程结束...')
    p.close()
    p.join() #等待所有进程结束后继续
    print('所有子进程都完了。')
