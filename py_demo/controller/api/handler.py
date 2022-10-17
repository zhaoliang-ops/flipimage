
from tornado import web
from utils.flipImage import FlipImage
from controller.mq.consumer import Consumer
from controller.mq.publish import Publish
class PublishParamHandler(web.RequestHandler):
    async def get(self):
        path = self.get_query_argument("fliped_url")
        Publish.public(path)


class ConsumerParamHandler(web.RequestHandler):
    async def get(self):
        # 消费者监听队列
        Consumer.consumer(self)
        