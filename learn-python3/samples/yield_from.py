
def htest():
    i = 1
    while i < 5:
        n = yield i
        # return n
        # print (n)
        # if i == 3 :
        #     return n
        i += 1
        #print (i)

def itest():
    val = yield from htest()
    #print (val)

'''
yield  生成器
yield  再次使用生成器
生成器优点：一个函数如果是生成一个数组，就必须把数据存储在内存中，如果使用生成器，则在调用的时候才生成数据，可以节省内存。
'''
a = htest()
print (a)
for i in a:
    print (i)

b = itest()
print (b)
for i in b :
    print (i)

# t = itest()
# t.send(None)
# j = 0
# while j < 3 :
#     j += 3
#     try:
#         t.send(j)
#     except StopIteration as e:
#         print ("异常")
#


