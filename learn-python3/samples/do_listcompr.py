#!/usr/bin/env python2
# -*- coding: utf-8 -*-

print ([x * x for x in range(2,10)])
print ([x * x for x in range(2,10) if x % 2 == 0])
print ([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A','y':'B','z':'C'}
print ([k + '=' + v for k,v in  d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])