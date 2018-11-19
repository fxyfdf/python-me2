#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterator,Iterable
#                          迭代器  可迭代的

def g():
    yield 1
    yield 2
    yield 3
# #  判断是不是可迭代的
# print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
# print('Iterable? \'abc\':', isinstance('abc', Iterable))
# print('Iterable? 123:', isinstance(123, Iterable))
# print('Iterable? g():', isinstance(g(), Iterable))
# # 判断是不是迭代器
# print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
# print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
# print('Iterator? \'abc\':', isinstance('abc', Iterator))
# print('Iterator? 123:', isinstance(123, Iterator))
# print('Iterator? g():', isinstance(g(), Iterator))


# iter list:
# print('for x in [1, 2, 3, 4, 5]:')
# for x in [1, 2, 3, 4, 5]:
#     print(x)

# #iter() 函数用来生成迭代器。
# print('for x in iter([1, 2, 3, 4, 5]):')
# print (type(iter([1,2,3,4,3,2,1])))
# print (iter([1,2,3,4,3,2,1]))
# for x in iter([1, 2, 3, 4, 5]):
#     print(x)

d = {'a':1,'b':2}
# iter each key:
print ('iter key:',d)
for k in d.keys():
    print (k)
# iter each value
print ('iter value:',d)
for v in d.values():
    print (v)
# iter both key and value
print ('iter item:',d)
for k,v in d.items():
    print (k,v)
# iter list with index :
print ('iter enumerate([\'A\',\'B\',\'C\'])')
for i,value in enumerate(['A','B','C']):
    print (i,value)

#iter complex list
print ('iter [(1,1),(2,4),(3,9)]:')
for x,y in [(1,1),(2,4),(3,9)]:
    print (x,y)















