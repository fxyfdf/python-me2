
from functools import reduce
a = lambda s:s+2
print (a(3))

#map
l1=[1,2,3,3,2,1]
b = lambda s:s+2
b = map(b,l1)
print (list(b))

#reduce
l2=[1,2,3,3,2,1]
c = lambda x,y:x+y
c = reduce(c,l2)
print (c)