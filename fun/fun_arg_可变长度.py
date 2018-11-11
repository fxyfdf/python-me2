
# *和 ** 元组 和 字典


def tupleVarArgs(arg1,arg2='defaultB',*rest,**rest2):
    print ("arg1: %s" ,arg1)
    print ("arg2: %s" ,arg2)
    print (rest)
    for eachXarg in rest:
        print ("rest:",eachXarg)

print (tupleVarArgs("aaaa1"))
#('233', [1, 3, 4, 5, 6], [1, 2, 3, 4], {'aa': 11, 'bb': 22}) 这一串为一个元组，传入
print (tupleVarArgs("aaaa2",'222','233',[1,3,4,5,6],[1,2,3,4],{'aa':11,'bb':22}))


def tupleVarArgs2(arg1,arg2='defaultB',*rest,**rest2):
    print ("arg1: %s" ,arg1)
    print ("arg2: %s" ,arg2)
    print (rest)
    for eachXarg in rest:
        print ("rest:",eachXarg)
    print (rest2)
    for key in rest2:
        print ("rest2 arg %s : %s" % (key,rest2[key]))

print (2222222222222222222222222222222222222222222222222221)
print (tupleVarArgs2('aaa'))
print (2222222222222222222222222222222222222222222222222222)
print (tupleVarArgs2('aaa','bbb'))
print (2222222222222222222222222222222222222222222222222223)
print (tupleVarArgs2('aaa',[1,2,3,4],'aaa'))
print (2222222222222222222222222222222222222222222222222224)
print (tupleVarArgs2('aaa',[1,2,3,4],'aaa',a='1',b='2',c='44'))




