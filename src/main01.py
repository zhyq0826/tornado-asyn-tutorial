#-*- coding:utf-8 -*-
from tornado.httpclient import HTTPClient


# 同步方法调用
def synchronous_fetch(url, callback):
    http_client = HTTPClient()

    def handle_response(response):
        callback(response)
    http_client.fetch(url, callback=handle_response)


# 同步回调
def synchronous_fetch_callback(result):
    print('synchronous_callback')
    print(result.request.url, result.code, result.reason, result.request_time)


if __name__ == '__main__':
    synchronous_fetch('http://baidu.com', synchronous_fetch_callback)
    synchronous_fetch('http://www.163.com', synchronous_fetch_callback)
