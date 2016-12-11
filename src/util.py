import tornado.ioloop

COUNTER = 0


def stop_loop(times):
    global COUNTER
    COUNTER += 1
    if COUNTER == times:
        tornado.ioloop.IOLoop.instance().stop()
        print('====> ioloop end')


def start_loop():
    print('====> ioloop start')
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()
