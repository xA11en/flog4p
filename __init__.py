# -*-coding:utf-8-*-
import threading, thread, logging, time, util, traceback
from logger import Logger, Constant


def base_config(**kwargs):
    Constant.LOCK_ACQUIRE
    try:
        is_file = kwargs.get('isFile')
        log_path = kwargs.get('path')
        print Logger(is_file, log_path)
        return Logger(is_file, log_path)
    finally:
        Constant.LOCK_RELEASE


def help():
    print '欢迎使用轻量级python log 框架...................'
    print '使用用例: import flog4p'
    print 'logger = flog4p.base_config(isFile=True, path="/Users/didi/Documents/workspace/zstack-autotest/log")'
    print 'isFile: True,False; False:只输出到控制台，True:输出到文件并打印到控制台，只提供 info 和 error 级别'
    print 'path: 如果  isFile 为 True 时 path 要求填写日志到绝对路径 如上'
    print '打印用例：不带参数,带参数'
    print 'logger1.info("test format logs")'
    print 'logger1.info("test format logs first params is {},sencond  params is {}", "one",222)'
    print '输出带参数带样例格式为：[INFO] 2018-05-25 18:11:52.343942 [MainThread] test format logs first params is one,sencond  params is 222'

