import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

from handlers import IndexHandler, PicHandler, TemplateHandler

define('port', default='8888', help='Listening Port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/pic', PicHandler),
            (r'/temp', TemplateHandler),
        ]
        settings = dict(
            debug=True,     # 代码有改动时会自动重启
            static_path='static',    # 配置静态目录
            template_path='templates',
        )
        super().__init__(handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()    # 相当于日志管理器
    app = Application()
    app.listen(options.port)
    print('server start on port {}'.format(options.port))
    tornado.ioloop.IOLoop.current().start()
