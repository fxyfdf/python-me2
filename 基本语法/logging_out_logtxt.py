import logging  # 引入logging模块
import os.path
import time
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
#rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
rq = time.strftime('%Y%m%d', time.localtime(time.time()))
print (rq)
#log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_path = ''
log_name = log_path + rq +  '.log'
logfile = log_name
# mode a 追加写入， w  覆盖写入
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  #输出到控制台

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

#日志输出到控制台：
ch.setFormatter(formatter)
logger.addHandler(ch)

# 第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')


