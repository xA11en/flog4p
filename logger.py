# -*-coding:utf-8-*-
import util, os, threading, thread, traceback,datetime

if thread:
    _lock = threading.RLock()
else:
    _lock = None


def _acquireLock():
    """
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    """
    if _lock:
        _lock.acquire()


def _releaseLock():
    """
    Release the module-level lock acquired by calling _acquireLock().
    """
    if _lock:
        _lock.release()


_log_type = ('info', 'error', '/', '.log')
_number = (10000, 1000)
_role = ('master', 'slave')
_day, _timeMills = datetime.datetime.now().strftime('%Y-%m-%d'), util.getTimeMillis()


class Constant(object):
    LOG_INFO = _log_type[0]
    LOG_ERROR = _log_type[1]
    FILE_SEPARATOR = _log_type[2]
    FILE_EXTENSIONS = _log_type[3]
    LOCK_ACQUIRE, LOCK_RELEASE = _acquireLock(), _releaseLock()
    MASTER = _role[0]
    SLAVE = _role[1]
    DEQUE_MAX_LEN = _number[0]
    WRITE_LOG_TIME_INTERVAL = _number[1]


class LoggerManager(object):
    def __init__(self):
        try:
            import collections
        except:
            raise ImportError
        self.currentMsg = None
        self.dequeMaster = collections.deque(maxlen=Constant.DEQUE_MAX_LEN)
        self.dequeSlave = collections.deque(maxlen=Constant.DEQUE_MAX_LEN)
        self.role = Constant.MASTER
        self.nextWriteTime = None

    def _putMsgsToDeque(self, logStrMsgs):
        if self.role == Constant.MASTER:
            self.dequeMaster.append(logStrMsgs)
        else:
            self.dequeSlave.append(logStrMsgs)

    def _productLog(self, isFile, logPath, logLevel, *args):
        try:
            _acquireLock()
            if len(args) == 0 or args is None:
                raise TypeError
            logStrMsgs = util.create_log_str(util.format_log(*args), logLevel)
            if not isFile:
                print logStrMsgs
            else:
                self._putMsgsToDeque(logStrMsgs)
                self.nextWriteTime = _timeMills + Constant.WRITE_LOG_TIME_INTERVAL
                if logPath is None:
                    logDir = os.getcwd() + Constant.FILE_SEPARATOR + _day
                    self._create_dir(logDir, logLevel)
                else:
                    logDir = logPath + Constant.FILE_SEPARATOR + _day
                    self._create_dir(logDir, logLevel)
        finally:
            _releaseLock()

    def _create_dir(self, logDir, logLevel):
        folder = os.path.exists(logDir)
        if not folder:
            os.makedirs(logDir)
            self._write_log(logDir, logLevel)
        else:
            self._write_log(logDir, logLevel)

    def _wLog(self, file_log):
        print self.role
        if self.role == Constant.MASTER:
            if self.dequeMaster is None or len(self.dequeMaster) == 0:
                raise Exception('dequeMaster is null at least one value')
            else:
                for msgs in self.dequeMaster:
                    with open(file_log, 'a+') as f:
                        f.write(msgs + '\n')
                self.role = Constant.SLAVE
                self.dequeMaster.clear()
        elif self.role == Constant.SLAVE:
            if self.dequeSlave is None or len(len(self.dequeSlave)) == 0:
                raise Exception('dequeSlave is null at least one value')
            else:
                print self.dequeSlave,'BBBBBBB'
                for msgs in self.dequeSlave:
                    with open(file_log, 'a+') as f:
                        f.write(msgs + '\n')
                self.role = Constant.MASTER
                self.dequeSlave.clear()

    def _write_log(self, logDir, logLevel):
        try:
            import time
        except:
            raise ImportError
        while True:
            _currentTimeMills = int(round(time.time() * 1000))
            try:
                _acquireLock()
                file_log = logDir + Constant.FILE_SEPARATOR + logLevel + Constant.FILE_EXTENSIONS
                if _currentTimeMills >= self.nextWriteTime:
                    self._wLog(file_log)
                else:
                    continue
            except:
                traceback.format_exc()
                break
            finally:
                _releaseLock()


class Logger(object):
    import threading
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, "_instance"):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance"):
                    Logger._instance = object.__new__(cls)
        return Logger._instance

    def __init__(self, isFile, logPath):
        self.is_file = isFile
        self.log_path = logPath
        self.manager = LoggerManager()

    def info(self, *args):
        LoggerManager()._productLog(self.is_file, self.log_path, Constant.LOG_INFO, *args)

    def error(self, *args):
        LoggerManager()._productLog(self.is_file, self.log_path, Constant.LOG_ERROR, *args)
