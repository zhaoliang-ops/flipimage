import os
from utils.rabbitmq import RabbitMq
# read_config.py文件
import configparser
config = configparser.ConfigParser()
curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath, '../../config.ini')
config.read(path,encoding="utf-8")
# 读取变量信息
user = config.get("rabbitmq", "user")
port = config.get("rabbitmq", "port")
host = config.get("rabbitmq", "host")
pwd = config.get("rabbitmq", "pwd")
push_queue = config.get("rabbitmq", "push_queue")
class Publish():
    def public(url):
        mq = RabbitMq(user=user, pwd=pwd, host=host, port=port)
        queue = push_queue
        mq.send(routing_key=queue,body = url)
