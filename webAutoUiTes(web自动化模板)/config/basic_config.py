# 1.导包
import logging.handlers


# 2.定义日志配置的方法
def log_config():
    # 3.创建日志器，并且设置日志的级别
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 4.创建处理器
    ls = logging.StreamHandler()  # 输出到控制台的处理器
    lht = logging.handlers.TimedRotatingFileHandler(filename="../log/test.log", when='midnight', interval=1,
                                                    backupCount=2)
    # 5.创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 6.给处理器设置格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 7.给日志器添加处理器
    logger.addHandler(ls)
    logger.addHandler(lht)
