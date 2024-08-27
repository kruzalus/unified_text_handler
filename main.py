from server.HandledTextRequestHandler import HandledTextRequestHandler
from tornado.ioloop import IOLoop
from tornado.web import Application


def make_app():
    urls = [
        ("/handled_text", HandledTextRequestHandler),
    ]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    print('Before starting')
    IOLoop.instance().start()
