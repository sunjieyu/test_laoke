# host
# 自媒体host地址
import os

mp_host_url = "http://ttapi.research.itcast.cn/mp/v1_0"
# 后台host地址
mis_host_url = "http://ttapi.research.itcast.cn/mis/v1_0"
# app端host地址
app_host_url = "http://ttapi.research.itcast.cn/app/v1_0"
app_host_url_v1_1 = "http://ttapi.research.itcast.cn/app/v1_1"

# 请求头
# 自媒体
mp_login_header = {"Content-Type": "application/json"}
# 后台管理
mis_header = {"Content-Type": "application/json"}
# app
app_header = {"Content-Type": "application/json"}

import logging.handlers

log_path = "./log" + os.sep + "hmtt.log"


# 初始化项目log
def ini_log():
    """日志初始化配置"""
    # 日志器对象
    logger = logging.getLogger()
    # 运行日志级别
    logger.setLevel(logging.INFO)

    # 处理器对象 -控制台
    ch = logging.StreamHandler()
    # 处理器对象 -文件
    fh = logging.handlers.TimedRotatingFileHandler(log_path, backupCount=7, encoding="UTF-8")

    # 格式化器对象
    fmt = "%(asctime)s %(levelname)s [%(filename)s-%(funcName)s:%(lineno)d] -%(message)s"
    fommter = logging.Formatter(fmt)

    # 格式化器 添加到 处理器对象
    ch.setFormatter(fommter)
    fh.setFormatter(fommter)

    # 处理器 添加到 日志器对象
    logger.addHandler(ch)
    logger.addHandler(fh)
