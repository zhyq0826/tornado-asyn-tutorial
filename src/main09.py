# -*- coding:utf-8 -*-
import tornado.gen
import tornado.ioloop

from util import start_loop, stop_loop


@tornado.gen.coroutine
def call_task():
    result = yield tornado.gen.Task(some_function, 1, 2)
    raise tornado.gen.Return(result)


def fetch_coroutine_callback(future):
    print('coroutine callback ==> ', future.result())
    stop_loop(1)


def some_function(x, y, callback=None):
    print('some_function called')
    callback(x * y)


if __name__ == '__main__':
    future = call_task()
    future.add_done_callback(fetch_coroutine_callback)
    start_loop()