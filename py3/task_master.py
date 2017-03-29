#!/usr/bin/env python
# coding=utf-8
import time
import random
import queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = queue.Queue()

# 接受结果的队列
result_queue = queue.Queue()

# 从BaseMangerj集成QueueManger


class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5050，设置验证码'abc'
manager = QueueManager(address=('', 5050), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放入几个任务
for i in range(10):
    n = random.randint(30,50)
    print('放入任务%d...' % n)
    task.put(n)

# 从result 队列读取结果
print('尝试获取结果...')
for i in range(10):
    r = result.get(timeout=10)
    print('结果是：%s' % r)
# 关闭
manager.shutdown()
print('master exit')
