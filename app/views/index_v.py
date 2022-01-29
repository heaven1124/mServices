import json
from tornado.web import RequestHandler


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

    # 跨域请求时，会被客户端请求，表示服务器是否支持跨域请求
    def options(self):
        self.set_status(200)