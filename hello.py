import tornado.ioloop
import tornado.web


class Mainhandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello, world')


def make_app():
    return tornado.web.Application([
        (r'/', Mainhandler),
    ],
        debug=True,     # 改动代码后会自动重启
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('hello, world')
    tornado.ioloop.IOLoop.current().start()
