#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/02/21 08:09:32 by samui>

import webapp2
import jinja2
from viewbase import JINJA_ENVIRONMENT

from data import jsonData,maxJsonNum
import cgi
import json
from geoCalc import distSphea,distSpheas,SphiaSquare
import logging
def makeJsonData(row):
    """
    rowData = "{"+\
              '"comment":"{0}",'.format(row['comment'])+\
              '"comment":"{0}",'.format(row['comment'])+\
              "}"
    """
    rowData = json.dumps(row)
    return rowData

class JsonWrite:
    class AllData(webapp2.RequestHandler):
        def get(self):
            limit = (self.request.get("l"))
            limit = cgi.escape(limit)
            if limit == '':
                limit = maxJsonNum
            limit = int(limit)
            
            self.response.headers['Content-Type'] = 'application/json'
            data = []
            for ins in jsonData[:limit]:
                data.append(makeJsonData(ins))
            text = "["+','.join(data[1:])+"]"
            self.response.write(text)

    class radius(webapp2.RequestHandler):
        def get(self):
            lat = 36.0349
            lng = 136.1306
            Oradius = 8.0 #km
            Oradius = cgi.escape(self.request.get('r'))
            if Oradius == '':
                Oradius = 0
            Oradius = float(Oradius)
            
            areaInfo = SphiaSquare(lat,lng,radius = Oradius)
            self.response.headers['Content-Type'] = 'application/json'
            data = []
            for ins in jsonData:
                if not areaInfo.isAreaRow(float(ins['lat']),float(ins['lng'])):
                    continue
                data.append(makeJsonData(ins))
            text = "["+','.join(data[1:])+"]"
            self.response.write(text)
            

def main():
    pass

if __name__  == "__main__":
    main()
