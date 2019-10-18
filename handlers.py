import tornado.web


HTML_TEMPLATE = """
        <html>
            <head><title>index page</title></head>
            <body>
                {}
            </body>
        </html>
"""


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PicHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(HTML_TEMPLATE.format('<img src="static/images/admin.png">'))


class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('name', '')
        link = '<a href="http://www.baidu.com" target="_blank">百度</a>'
        self.render('base.html', username=username, link=link)