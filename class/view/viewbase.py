#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/24 04:04:37 by samui>

import jinja2
import os
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/../../views"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

