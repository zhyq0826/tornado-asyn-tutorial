#-*- coding:utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import thread
import tornado.gen
from tasks import add
import time
import datetime

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        print datetime.datetime.now(), 'start'
        self.result = add.delay(9, 4)
        self.timeout_handler = None
        if self.result.ready():
            self.write("Hello, world"+str(self.result.get()))
            self.finish()
        else:
            #这里的timeout时间大于任务时间和小于任务时间的表现是不一样的 add timeout 实现了一个非阻赛的 sleep
            #self.timeout_handler=tornado.ioloop.IOLoop.instance().add_timeout(time.time()+5, self.add)
            tornado.ioloop.IOLoop.instance().add_callback(self.add)

    def add(self):
        print datetime.datetime.now(), 'wake'
        if not self.result.ready():
            tornado.ioloop.IOLoop.instance().add_callback(self.add)
        else:
            #tornado.ioloop.IOLoop.instance().remove_timeout(self.timeout_handler)
            self.write("Hello, world"+str(self.result.get()))
            self.finish()


class HelloMainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


class SleepHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        result = add.apply_async(args=[6, 4], serializer='pickle')
        yield result
        #result = add.delay(4, 4)
        self.write(str(result.get()))
        self.finish()


    def on_response(self, response):
        self.write(response.result)
        self.finish()
        tornado.ioloop.IOLoop.instance().add_timeout()

class HelloHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        response = yield tornado.gen.Task(add.apply_async, args=[2,4], serializer='pickle')
        print response.result
        self.write(str(response.result))
        self.finish()

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/timeout", MainHandler),
        (r"/hello", HelloMainHandler),
        (r"/sleep", SleepHandler),
        (r"/two", HelloHandler),
    ])
    print thread.get_ident()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()