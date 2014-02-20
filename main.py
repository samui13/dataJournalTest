#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/02/21 06:21:57 by samui>

import os
import cgi
import sys
import webapp2
from webapp2_extras import config as webapp2_config
from werkzeug import SharedDataMiddleware

from functools import wraps
sys.path.append(os.path.dirname(__file__)+"/venders")


sys.path.append(os.path.dirname(__file__)+"/class/view")
from viewbase import JINJA_ENVIRONMENT

sys.path.append(os.path.dirname(__file__)+"/class/model")
sys.path.append(os.path.dirname(__file__)+"/class/controller")
from top import Top

sys.path.append(os.path.dirname(__file__)+"/config")
from sdata import myConfig

app = webapp2.WSGIApplication([
    webapp2.Route(r'/',handler=Top.Main,name='home'),
    webapp2.Route(r'/',handler=Top.Index,name='index')
],debug=True)

app.config = webapp2_config.Config(myConfig)
app = SharedDataMiddleware(app, {
    '/static': os.path.dirname(__file__)+"/static"
})

