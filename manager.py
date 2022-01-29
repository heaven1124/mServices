from tornado.ioloop import IOLoop
import tornado.options

from app import make_app

if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port', default=8080, type=int, help='bind socket port')
    tornado.options.define('host', default='localhost', type=str, help='设置host name')

    # 解析命令行参数
    tornado.options.parse_command_line()

    app = make_app(tornado.options.options.host)
    # 使用命令行参数
    app.listen(tornado.options.options.port)
    print('starting web server http://%s:%s' % (
        tornado.options.options.host,
        tornado.options.options.port
    ))
    IOLoop.current().start()