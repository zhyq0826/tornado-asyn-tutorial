# -*- coding:utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen

from util import stop_loop, start_loop


@gen.coroutine
def fetch_coroutine(urls):
    http_client = AsyncHTTPClient()
    responses = yield [http_client.fetch(url) for url in urls]
    raise gen.Return(responses)


def fetch_coroutine_callback(future):
    print('coroutine callback')
    for result in future.result():
        print(
            result.request.url,
            result.code, result.reason, result.request_time)
    stop_loop(1)


if __name__ == '__main__':
    """
    使用gen.coroutine 可以很方便让包含 yield 的函数返回future
    """
    result_future = fetch_coroutine(['https://baidu.com', 'https://baidu.com'])
    result_future.add_done_callback(fetch_coroutine_callback)
    start_loop()

