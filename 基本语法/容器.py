
'''
list：数组
tuple：只读数组
set：没有重复元素的数组
dict：字典（哈希表）
数组切片
字符串与数组的关系!!!
'''

li = []
#变历
for i in li:
    print (i)
# 用 range 模拟for (i=0;i<x ;++i)
# range(x) => [0,x,-1]
#range(x,y) => [x,y -1]
# range(x,y,z) => [x,x+z,..., < y]
for i in range(len(li)):
    #print (li[i])
    pass

for i in  range(1,10,2):
    li.append(i)
    print (i)
print (li)
#负数所用
print (li[-1])
for i in range(3,-1 ,-1):
    print (i)

#添加元素
li = []
li.append(1)
li.append('asb')
li.append([1,2,'a'])
print (li)
li_2 = [2,3,4]
li.extend(li_2)
print (li)
#按照元素添加元组

#删除 元素
li = [1,2,3,4,5,2,3]
li.pop()  # 删除
li.pop(2)
li.sort()
print ('lambda sort')
li2 = [[3,4],[2,6],[22,3],[1,7],[33,3]]
print (li2)
#li2.sort(key = lambda x:x[0])  #参数名字,按照列表中的列表 的 第一个值排序
#等价写法
def item_key(x):
    return x[0]
li2.sort(key = item_key)
print (li2)
print (li2)

###############字典####################################

# key<->value对应的hash表
di = {'k1': 'v1', 'k2': 'v2'}
di['k3'] = 'v3'
di['k4'] = 'v4'

for k in di:
    print(di[k])
for k, v in di.items():
    print(k, v)
###############set####################################

s = set([1, 2, 2, 3, 3, 4, 5])
print(s)
s.add(77)
print(s)
s = set((2, 3, 4, 5, 6, 2, 1, 9))
print(s)

