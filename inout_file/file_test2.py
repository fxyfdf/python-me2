#!/bin/env python

with open("E:/PYTHON/PyCharm/txt-file/1.txt",'w') as f:
    aa = '''1234
    1234
    1233
    asdf
    zxd'''
    f.write(aa)
with open("E:/PYTHON/PyCharm/txt-file/1.txt", 'r') as f:
    for line in f.readlines():
        print (line)

#二进制文件
with open("E:/PYTHON/PyCharm/txt-file/1.txt",'rb') as f:
    for line in f.readlines():
        print (line)