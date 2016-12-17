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
from task import add
import time
import datetime

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class GenTaskHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        result = add.apply_async((2, 4))
        if not result.successful():
            tornado.ioloop.IOLoop.current().add_callback(self.on_response, result, time.time())
        else:
            self.write(str(result.result))
            self.finish()

    def on_response(self, result, start):
        if time.time() - start > 5:
            self.write('task timeout')
            self.finish()
            return

        if result.successful():
            self.write(str(result.result))
            self.finish()
        else:
            tornado.ioloop.IOLoop.current().add_callback(self.on_response, result, start)


class HelloHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello world')


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/gentask", GenTaskHandler),
        (r"/", HelloHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print 'http_server start %s' % options.port
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()