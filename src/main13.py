#-*- coding:utf-8 -*-
import tornado.gen
from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop
from tornado.concurrent import Future, return_future
from tornado import gen


# How to simulate next next chunk
#Coroutine patterns
#Interleaving

RESULT = []

@gen.coroutine
def get():
    fetch_future = fetch_next_chunk()
    fetch_future.send(None)
    while True:
        chunk = yield fetch_future.next()
        print('while', chunk)
        if chunk is None: break
        write(chunk)

    result = yield flush()
    raise gen.Return(result)

def write(chunk):
    RESULT.append(chunk)

def fetch_coroutine_callback(future):
    print('coroutine callback')
    print(future.result())

@gen.coroutine
def flush():
    raise gen.Return(RESULT)


def fetch_next_chunk():
    print('fetch_next_chunk called')
    count = 0
    while count <= 10:
        count += 1
        future = Future()
        future.set_result(count)
        yield future


if __name__ == '__main__':
    result_future = get()
    result_future.add_done_callback(fetch_coroutine_callback)
    print('ioloop start')
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()
    print('ioloop end')