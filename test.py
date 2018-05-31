import collections
import threading,report,logging

import time

logger = report.base_config(isFile=True, path='/Users/didi/Documents/workspace/zstack-autotest/log')
logger1 = report.base_config(isFile=True, path='/Users/didi/Documents/workspace/zstack-autotest/log')


def plog2():
    logger.info('test format logs firsttest format logs firsttest format logs first params istest format logs first params i {},sencond  params is {}', 'one',222)
    logger.error('test format logs firsttest format logs firsttest format logs first params is test format logs first params i{},sencond  params is {}', 'one',222)

def plog():
    logger.info('test format logs firsttest format logs firsttest format logs first params istest format logs first params i {},sencond  params is {}', 'one', 222)
    logger.error('test format logs firsttest format logs firsttest format logs first params is test format logs first params i{},sencond  params is {}', 'one', 222)

    #print 123
for i in range(1000):
    t2 = threading.Thread(target=plog)
    t2.start()

import time
'''

class A:

    def __init__(self):
        pass

    def p(self):
        print 123
def decorator(func):
    def wrapper(*args, **kwargs):
        return A()
    return wrapper

@decorator
def func():
    pass


print func().p()
'''



