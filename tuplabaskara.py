# -*- coding: utf-8 -*-

import math

def baskara (a,b,c):
    delta = b**2 - 4*a*b

    x1 = (-b + math.sqrt (delta))/2*a
    x2 = (-b - math.sqrt (delta))/2*a

    return x1, x2

#chamada de função
raizes = baskara (1,10,4)

#prints
print (raizes)
print (type(raizes))
print (len(raizes))

x1 = raizes[0]
x2 = raizes[1]

x1_, x2_ = raizes
