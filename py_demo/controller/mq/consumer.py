
import os
from utils.rabbitmq import RabbitMq
from utils.flipImage import FlipImage
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
recive_queue = config.get("rabbitmq", "recive_queue")

class Consumer():
    def consumer(self):
        mq = RabbitMq(user=user, pwd=pwd, host=host, port=port)
        queue = recive_queue
        def callback(ch, method, properties, body):
            print(ch)
            print(method)
            print(properties)
            print(body)
            # 翻转图片
            FlipImage.flipImage(str(body, "utf-8"))
        mq.received(routing_key=queue, fun=callback)
        mq.consume()
        

