from tornado import web, ioloop
from controller.api.handler import PublishParamHandler,ConsumerParamHandler
from utils.flipImage import FlipImage
url_handers = [
    ("/publish", PublishParamHandler),
    ("/consumer", ConsumerParamHandler),
]
if __name__ == '__main__':
    app = web.Application(url_handers, debug=True)
    app.listen(8881)
    print("started...")
    # FlipImage.flipImage('../Images')
    ioloop.IOLoop.current().start()