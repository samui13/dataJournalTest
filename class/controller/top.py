#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/02/21 06:28:15 by samui>

import webapp2
import jinja2

from viewbase import JINJA_ENVIRONMENT


class Top:
    class Main(webapp2.RequestHandler):
        def get(self):
            # Config 設定をよみこみ
            #self.response.write(self.app.config['data']['id'])
            base = JINJA_ENVIRONMENT.get_template('Top/index.html')
            # View に変数をわたす
            contents = {'name':'John'}
            self.response.write(base.render(contents))
            
    class Index(webapp2.RequestHandler):
        def get(self):
            base = JINJA_ENVIRONMENT.get_template('Top/index.html')
            self.response.write(base.render())
