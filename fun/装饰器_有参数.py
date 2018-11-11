# -*-- coding:utf-8 -*-
# 有参数 装饰器
from time import ctime,sleep
print (ctime())
def  tsfunc(func):
    def wrappedFunc():
        c_time=ctime()
        print ("[%s] %s() called " % (ctime(),func.__name__))
        print ("我说 tsfunc 嵌套的 tsfunc")
        return func()
    return wrappedFunc
    return ("我是tsfunc")
@tsfunc
def  foo():
    print ("my name is foo foo foo ")
    print ("foo() is invoked")
foo()
sleep(3)
'''
for i in range(1):
    sleep(1)
    foo()
'''

