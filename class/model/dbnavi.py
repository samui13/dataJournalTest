#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/01/24 06:47:52 by samui>

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBNavi:
    engine = create_engine('mysql://huser:acr81uoi@localhost/kyonaviApp?charset=utf8') #,echo=True)
    #engine = create_engine('mysql://bb8aa8bb39bdc8:a7ccf23e@us-cdbr-east-04.cleardb.com/heroku_2360f88bf1d10e5?charset=utf8')
    def __init__(self):
        self.connect = self.engine.connect()
        db_session = sessionmaker(bind=self.engine)
        self.session = db_session()
    def add(self,obj):
        self.session.add(obj)
    def commit(self):
        try:
            self.session.commit()
        except:
            return

def main():
    # mysql -u huser -p kyonaviApp
    t = DBNavi()

if __name__  == "__main__":
    main()

