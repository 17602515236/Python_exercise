import logging
from logging.handlers import RotatingFileHandler
#配置日志输出
#level:输出等级
#format:输出格式
#datefmt:日期输出格式
#filename:输出到文件的文件名(不填写就输出到屏幕)
#filemode:文件操作方式
logging.basicConfig(level = logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='myapp.log',
        filemode='w')

#定义一个日志处理对象
logger = logging.getLogger("")

#创建2个Handler(屏幕和文件)
f_h = logging.FileHandler("test.log")
s_h = logging.StreamHandler()

#创建输出到屏幕的Handler的格式化器并添加到Handler
format_s = logging.Formatter("%(asctime)s %(levelname)s %(message)s",datefmt = "%Y %M %D %H %M %S")
s_h.setFormatter(format_s)
#创建输出到文件的Handler的格式化器并添加到Handler
format_f = logging.Formatter("%(asctime)s %(levelname)s %(message)s",datefmt = "%Y-%M-%D-%H-%M-%S")
f_h.setFormatter(format_f)

#设置日志输出等级
f_h.setLevel(logging.WARNING)
s_h.setLevel(logging.INFO)

#添加Handler到日志处理器
logger.addHandler(f_h)
logger.addHandler(s_h)

#5个级别的日志(默认打印到屏幕，默认)
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is waring")
logging.error("this is debug error")
logging.fatal("this is debug fatal")
