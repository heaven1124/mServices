from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://localhost:8080'

    def test_index_post(self):
        url = self.base_url + '/'
        # 发起post请求, 表单参数是json数据
        resp = requests.post(url, json={
            'name': 'disen',
            'pwd': '123456'
        })
        # 读取响应的json数据
        print(resp.json())
