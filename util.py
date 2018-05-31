# -*-coding:utf-8-*-
import datetime, threading, re


def getTimeMillis():
    import time
    return int(round(time.time() * 1000))


def create_log_str(msg, log_level):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    log_template = [
            '[' + log_level.upper() + ']',
            ' ',
            time,
            ' ',
            '[' + threading.current_thread().name + ']',
            ' ', msg
                    ]
    return ''.join(log_template)


'''
    importment:
    格式化日志核心逻辑：例如logger.info('test format logs first params is {},sencond  params is {}', 'one',222)
    输出样式为：[INFO] 2018-05-25 18:11:52.343942 [MainThread] test format logs first params is one,sencond  params is 222
        
'''


def format_log(*args):
    if len(args) != 1:
        arrayStar = []
        for i in args:
            if isinstance(i, basestring):
                arrayStar.append(i)
            else:
                arrayStar.append(str(i))
        argsTuple = tuple(arrayStar)
        newTuple = argsTuple[1:len(argsTuple)]
        replaceStr = re.sub(r"[{}]+", '%s', args[0])
        logs = replaceStr % newTuple
        return logs
    else:
        formatMsgs = args[0] if isinstance(args[0], basestring) else str(args[0])
        return formatMsgs

