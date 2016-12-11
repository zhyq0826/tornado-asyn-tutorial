#-*- coding:utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen

from util import stop_loop, start_loop


# 异步调用
def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        callback(response)
    http_client.fetch(url, callback=handle_response)


# 异步回调
def asynchronous_fetch_callback(result):
    print('asynchronous_callback')
    print(result.request.url, result.code, result.reason, result.request_time)
    stop_loop(2)



if __name__ == '__main__':
    """
    ioloop start
    asynchronous_callback
    """
    asynchronous_fetch('http://163.com', asynchronous_fetch_callback)
    asynchronous_fetch('http://baidu.com', asynchronous_fetch_callback)
    start_loop()
