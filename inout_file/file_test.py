
#python   逐行读取文件内容：

#1

f1 = open("E:/PYTHON/PyCharm/txt-file/1.txt","w")

f = open("foo.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    print (line,)                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()
#2


for line in open("foo.txt"):
    print (line,)
#3


f = open("c:\\1.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:
    print (line)