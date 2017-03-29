#!/usr/bin/env python
# coding=utf-8

import os
print('进程（%s）开始..' % os.getpid())

pid = os.fork()
if pid == 0:
    print('我是子进程（%s）,我的父进程是 %s。' % (os.getpid(),os.getppid()))
else:
    print('我（%s）创建了一个(%s)的子进程。' % (os.getpid(),pid))
