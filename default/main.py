#!/usr/bin/env python2
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# from google.appengine.api import users
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello D2SI!')


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Frank!')


APPLICATION_HANDLERS = [
    # webapp2.Route("/hello", HelloHandler),
    ('/api/hello', HelloHandler),
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(APPLICATION_HANDLERS, debug=True)
