#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last-Updated : <2014/02/21 07:42:41 by samui>
import math
def distSpheas(A,B):
    """
    A = [lat,long]
    B = [lat,long]
    distSpheas(J,I)      
    """
    return distSphea(A[0],B[0],A[1],B[1])
    
def distSphea(lat1,lat2,long1,long2):
    R = 6378.137
    if lat1 == lat2 and long1 == long2:
        return 0;
    lat1 = lat1*math.pi/180
    lat2 = lat2*math.pi/180
    long1 = long1*math.pi/180
    long2 = long2*math.pi/180

    calc = math.acos(math.sin(long1)*math.sin(long2)+
                     math.cos(long1)*math.cos(long2)*
                     math.cos(lat1-lat2))*R
    return calc

    

class SphiaSquare:
    """
    a =  SphiaSquare(F[0],F[1],radius = r)
    
    """
    lat = 0.0
    long = 0.0
    radius = 0.5 # 0.5km
    #delta = 0.0002
    delta = 0.0002
    def __init__(self,lat,long,**kwdargs):
        self.lat = lat
        self.long = long
        self.__dict__.update(kwdargs)
        #self.radius = kwdargs['r']
        self.delLat,self.delLong = self.getEpsLat()
    def isArea(self,spotA):
        lat,long = spotA
        if (lat > self.lat-self.delLat and lat < self.lat+self.delLat)\
           and (long > self.long-self.delLong and long < self.long+self.delLong):
            return True
        else:
            return False
    def isAreaRow(self,lat,long):
        if (lat > self.lat-self.delLat and lat < self.lat+self.delLat)\
           and (long > self.long-self.delLong and long < self.long+self.delLong):
            return True
        else:
            return False
        
    def getEpsLat(self):
        r = [0,self.radius*500,self.radius*1000]#range(0,int(self.radius*100))
        self.epsFunc = self.epsLat
        epslat =  self.ThreeRange(r)*self.delta

        #r = range(0,int(self.radius*100))
        r = [0,self.radius*500,self.radius*1000]#range(0,int(self.radius*100))
        self.epsFunc = self.epsLong
        epslong =  self.ThreeRange(r)*self.delta
        return epslat,epslong

    def epsLat(self,eps):
        return [self.lat-eps*self.delta,self.long]
    def epsLong(self,eps):
        return [self.lat,self.long-eps*self.delta]
        
        
    def ThreeRange(self,r):
        if abs(r[1]-r[2]) <= 1 or abs(r[1]-r[0])<=1:
            return r[1]
        #m = func(r)
        m = r
        A =  distSpheas([self.lat,self.long],
                        self.epsFunc(m[0]))
        B =  distSpheas([self.lat,self.long],
                        self.epsFunc(m[1]))
        C =  distSpheas([self.lat,self.long],
                        self.epsFunc(m[2]))


        if A < self.radius and B > self.radius:
            return self.ThreeRange([m[0],m[1]/2,m[1]])
        elif B < self.radius and C > self.radius:
            return self.ThreeRange([m[1],int((m[1]+m[2])/2),m[2]])
        else:
            return m[1]
        
        
