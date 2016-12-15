# -*- coding:utf-8 -*-
import tornado.gen
import tornado.ioloop


@tornado.gen.coroutine
def divide(x, y):
    return x / y


if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(lambda: divide(1, 0))
