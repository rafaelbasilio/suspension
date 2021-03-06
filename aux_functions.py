# -*- coding: utf-8 -*-
"""
Autor: Rafael Basilio Chaves
"""
import numpy as np
import math

def skew_symmetric(r):
    r = r.T
    A = np.array([[   0 , -r[0,2] ,  r[0,1]],
                  [ r[0,2],    0  , -r[0,0]],
                  [-r[0,1],  r[0,0] ,   0 ]])
    return A

def trigon(a,b,c):
    if b < 0:
        psi = math.asin(-c/math.sqrt(a**2+b**2))- math.atan2(-a,-b)
    else:
        psi = math.asin(c/math.sqrt(a**2+b**2))- math.atan2(a,b)
        
    return psi


