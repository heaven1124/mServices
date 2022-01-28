import json

import  tornado.web
from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
import tornado.options


class IndexHandler(RequestHandler):
    def get(self):
        # 从请求处理器对象中获取请求参数
        # self.get_argument('name')
        # self.get_arguments()
        # # 只能查询get请求的参数
        # self.get_query_argument('name')
        # self.get_query_arguments()
        # # 只能查询post请求的表单参数
        # self.get_body_argument()
        # self.get_body_arguments()
        # # 从request对象中获取请求参数
        # req: HTTPServerRequest = self.request
        # # request中获取的数据都是字典类型
        # # 字典key对应的value都是byte字节类型（不建议使用）
        # name = req.arguments.get('name')

        # 判断参数中是否存在name
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            self.write(name)
        # 查看所有cookie
        cookies: dict = self.request.cookies
        html = '<ul>%s</ul>'
        lis = []
        # for key, value in cookies.items():
        #    lis.append('<li>%s: %s</li>' % (key, value))
        for key in cookies:
           lis.append('<li>%s: %s</li>' % (key, self.get_cookie(key)))
        self.write('显示所有cookie' + html % ''.join(lis))
        # resp_data = {
        #     'wd': 'java',
        #     'result': 'java is a popular programming language'
        # }
        # 返回json
        # 设置响应头的数据类型
        # self.set_header('Content-Type', 'application/json;charset=utf-8')
        # self.write(json.dumps(resp_data))
        # self.set_status(200)

        # 重定向时，不需要调用self.write()
        # self.redirect('/order')

    def post(self):
        # 读取json数据(字节数组)
        byte = self.request.body

        # 从请求头中读取上传的数据类型
        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            # 把字节数组转成json字符串
            json_str = byte.decode('utf-8')
            # 反序列化成字典
            json_data = json.loads(json_str)
            # write()函数可接收str, dict, list
            self.write(json_data)
            self.set_header('Content-Type', 'application/json')


        else:
            self.write('upload data must be json data')

    def put(self):
        self.write('I am put method')

    def delete(self):
        self.write('I am delete method')


class OrderHandler(RequestHandler):
    goods = [{
        'id': 1,
        'name': 'python高级开发',
        'author': 'disen',
        'price': 100
    },
    {
        'id': 2,
        'name': 'java高级开发',
        'author': 'alan',
        'price': 200

    }]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }

    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def get(self, order_id, action_code):
        self.write('订单查询')
        self.write(self.query(int(order_id)))
        self.write(self.action_map.get(int(action_code)))

    def initialize(self):
        # 每次请求都会创建一个RequestHandler对象，并调用RequestHandler对象的初始化方法
        print('-----initialize-----')

    def prepare(self):
        # 在初始化之后，调用行为方法之前，调用此方法进行预处理，
        # 主要用于验证权限、参数合法性、读取缓存
        print('-----prepare-----')

    def on_finish(self):
        # 请求处理完成后调用，主要用于释放资源，数据库链接
        print('-----finish-----')


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler),
    ], default_host=tornado.options.options.host) # 使用命令行参数


if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port', default=8080, type=int, help='bind socket port')
    tornado.options.define('host', default='localhost', type=str, help='设置host name')

    # 解析命令行参数
    tornado.options.parse_command_line()

    app = make_app()
    # 使用命令行参数
    app.listen(tornado.options.options.port)
    print('starting web server http://%s:%s' % (
        tornado.options.options.host,
        tornado.options.options.port
    ))
    tornado.ioloop.IOLoop.current().start()