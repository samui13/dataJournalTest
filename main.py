#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/02/21 07:34:14 by samui>

import os
import cgi
import sys
import webapp2
from webapp2_extras import config as webapp2_config
from werkzeug import SharedDataMiddleware

from functools import wraps
sys.path.append(os.path.dirname(__file__)+"/venders")
from data import jsonData

sys.path.append(os.path.dirname(__file__)+"/class/view")
from viewbase import JINJA_ENVIRONMENT

sys.path.append(os.path.dirname(__file__)+"/class/model")
sys.path.append(os.path.dirname(__file__)+"/class/controller")
from top import Top
from jsonwrite import JsonWrite

sys.path.append(os.path.dirname(__file__)+"/config")
from sdata import myConfig

app = webapp2.WSGIApplication([
    webapp2.Route(r'/home',handler=Top.Main,name='home'),
    webapp2.Route(r'/',handler=Top.Index,name='index'),
    webapp2.Route(r'/json/all',handler=JsonWrite.AllData,name='jsonall'),
    webapp2.Route(r'/json/radius',handler=JsonWrite.radius,name='jsonrad')
],debug=True)

app.config = webapp2_config.Config(myConfig)
app = SharedDataMiddleware(app, {
    '/static': os.path.dirname(__file__)+"/static"
})

