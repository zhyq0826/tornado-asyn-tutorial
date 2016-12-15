#-*- coding:utf-8 -*-
import tornado.gen
from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop

from util import start_loop, stop_loop


def fetch_coroutine_callback(future):
    print('coroutine callback')
    # print(future.result())
    print(future.exception())
    stop_loop(1)


@tornado.gen.coroutine
def divide(x, y):
    return x / y


def bad_call():
    # This should raise a ZeroDivisionError, but it won't because
    # the coroutine is called incorrectly.
    divide(1, 0)


@tornado.gen.coroutine
def good_call():
    # yield will unwrap the Future returned by divide() and raise
    # the exception.
    yield divide(1, 0)


if __name__ == '__main__':
    bad_call() # no exceptions
    result_future = good_call() # raise exceptions
    result_future.add_done_callback(fetch_coroutine_callback)
    start_loop()