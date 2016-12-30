# -*- coding:utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen
from motor import motor_tornado
import pprint

from util import stop_loop, start_loop

client = motor_tornado.MotorClient()
db = client['test']


@gen.coroutine
def insert_one():
    result = yield db.test.insert_one({'hello': 'world'})
    raise gen.Return(result)


@gen.coroutine
def find_one():
    result = yield db.test.find_one()
    pprint.pprint(result)
    raise gen.Return(result)


def fetch_coroutine_callback(future):
    print('coroutine callback')
    print future.result()
    stop_loop(2)


if __name__ == '__main__':
    """
    使用gen.coroutine 可以很方便让包含 yield 的函数返回future
    """
    result_future = insert_one()
    result_future.add_done_callback(fetch_coroutine_callback)
    result_future = find_one()
    result_future.add_done_callback(fetch_coroutine_callback)
    start_loop()
