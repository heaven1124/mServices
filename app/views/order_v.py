from tornado.web import RequestHandler


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