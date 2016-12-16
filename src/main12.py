# -*- coding:utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado import gen
import motor

from util import stop_loop, start_loop


db = motor.MotorClient().test

@gen.coroutine
def loop_example():
    cursor = db.test.find(limit=10)
    as_list = []
    while (yield cursor.fetch_next):
        doc = cursor.next_object()
        as_list.append(doc)

    raise gen.Return(as_list)


def fetch_coroutine_callback(future):
    print('coroutine callback ==> ', future.result())
    stop_loop(1)


if __name__ == '__main__':
    future = loop_example()
    future.add_done_callback(fetch_coroutine_callback)
    start_loop()