# -*- coding:utf-8 -*-

# 有参装饰器


#test 无参 装饰器, 没有参数的装饰器

def deco2(func(**arg)):
    print ("我是装饰器 deco2")
    return func


@deco2
def func(arg1,arg2):
    print (arg1)
    print (arg2)
    print ("我是func")


#func = deco2(deco2(func))
print (func("abc","def"))

# 有参数 装饰器

