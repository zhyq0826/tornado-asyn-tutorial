#-*- coding:utf-8 -*-
from tornado.concurrent import Future
from tornado import gen
import time
from concurrent.futures import ThreadPoolExecutor

from util import start_loop, stop_loop


EXECUTOR = ThreadPoolExecutor(max_workers=4)


def fetch_coroutine_callback(future):
    print('coroutine callback')
    print(future.result())
    stop_loop(2)


def sleep_func(t):
    print('sleep_func call')
    time.sleep(t)
    return 'blocking func result'


@gen.coroutine
def blocking():
    result = yield EXECUTOR.submit(sleep_func, *(4, ))
    raise gen.Return(result)


@gen.coroutine
def not_blocking():
    future = Future()
    future.set_result('not blocking func result')
    result = yield future
    raise gen.Return(result)

@gen.coroutine
def bad_not_blocking():
    """future 得不到执行的结果，这个 coroutine 将一直被挂起，等待执行完毕
    """
    _ = yield Future()
    raise gen.Return('not blocking func result')


if __name__ == '__main__':
    """
    用多线程的方式借助协程实现异步调用
    """
    blocking().add_done_callback(fetch_coroutine_callback)
    not_blocking().add_done_callback(fetch_coroutine_callback)
    start_loop()

