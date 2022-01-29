from tornado.web import Application

from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler),
    ], default_host=host) # 使用命令行参数