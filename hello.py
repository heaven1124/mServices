from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

# 创建处理web请求的处理器
class IndexHandler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        self.write('<h3>hello, tornado</h3>')


if __name__ == '__main__':
    # 创建web应用，绑定处理器
    app = Application([
        ('/', IndexHandler)
    ])
    # 绑定端口
    app.listen(8080)
    # 启动web服务
    IOLoop.current().start()
