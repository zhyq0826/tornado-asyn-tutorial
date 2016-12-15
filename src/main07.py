# -*- coding:utf-8 -*-
import tornado.gen
import tornado.ioloop


from util import start_loop, stop_loop


@tornado.gen.coroutine
def divide(x, y):
    return x / y


if __name__ == '__main__':
    # The IOLoop will catch the exception and print a stack trace in
    # the logs. Note that this doesn't look like a normal call, since
    # we pass the function object to be called by the IOLoop.
    tornado.ioloop.IOLoop.current().spawn_callback(divide, 1, 0)
    tornado.ioloop.IOLoop.current().add_timeout(
        tornado.ioloop.time.time() + 1, stop_loop, 1)
    start_loop()
