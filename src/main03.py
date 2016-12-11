#-*- coding:utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen

from util import stop_loop, start_loop


# fetch 返回的是 future
def asyn_fetch_future(url):
    http_client = AsyncHTTPClient()
    return http_client.fetch(url)


def asyn_fetch_future_callback(future):
    result = future.result()
    print('future_callback')
    print(result.request.url, result.code, result.reason, result.request_time)
    stop_loop(1)


if __name__ == '__main__':
    result_future = asyn_fetch_future('http://www.apple.com/cn/')
    result_future.add_done_callback(asyn_fetch_future_callback)
    start_loop()
