from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)
#print(soup.p["class"])
#print(soup.a)
#print(soup.find_all('a'))
#print(soup.find(id='link3'))

# #标签选择器
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)

# # 获取名称
# # 当我们通过soup.title.name的时候就可以获得该title标签的名称，即title
# print (soup.title.name)

# # 获取属性  以下两种方式都可以获取p标签的name属性值
# print(soup.a)
# print(soup.a.attrs['id'])
# print(soup.a['href'])

# #获取内容  结果就可以获取第一个p标签的内容：
# print(soup.a.string)

# #嵌套选择  我们直接可以通过下面嵌套的方式获取
# print(soup.head.title.string)

# #子节点和子孙节点  contents的使用
# print(soup.p.contents)

#children的使用 通过下面的方式也可以获取p标签下的所有子节点内容和通过contents获取的结果是一样的，
# 但是不同的地方是soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息

# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)
# #通过contents以及children都是获取子节点，如果想要获取子孙节点可以通过descendants
# #同时这种获取的结果也是一个迭代器
# print(soup.descendants)
#
# print (soup.a)
# print (soup.a.next_siblings)
# print (soup.a.previous_siblings)
# print (soup.a.next_sibling)
# print (soup.a.next_sibling.next_sibling.next_sibling.next_sibling)

# # 标准选择器 find_all  s
# # print (soup.find_all('p'))
# print (soup.find_all('html'))

# # attrs
# # attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，特殊的标签属性可以不写attrs，例如id
# print (soup.find_all(attrs={'id':'link2'}))

# #text
# print (soup.find_all(text='Tillie'))
'''
find

find(name,attrs,recursive,text,**kwargs)
find返回的匹配结果的第一个元素

其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
'''

#CSS 选择器
'''
通过select()直接传入CSS选择器就可以完成选择
熟悉前端的人对CSS可能更加了解，其实用法也是一样的
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签

获取内容
通过get_text()就可以获取文本内容
获取属性
或者属性的时候可以通过[属性名]或者attrs[属性名]
'''
#soup = BeautifulSoup(open('bs4_test.html'),'html.parser')
soup = BeautifulSoup(open('css_test.html'),'html.parser')

# #标签1，标签2 找到所有的标签1和标签2
# print(soup.select('.panel-heading, .panel-body'))
# #标签1 标签2 找到标签1内部的所有的标签2
# print (soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))

# # 获取内容  通过 get_text() 就可以获取文本内容
# for li in soup.select('ul'):
#     print (li.get_text())

#获取属性   获取属性的时候可以通过[属性名] 或者 attrs[属性名]
for ul in soup.select('ul'):
    print(ul['class'])
    print(ul.attrs['id'])


'''
总结
推荐使用lxml解析库，必要时使用html.parser
标签选择筛选功能弱但是速度快
建议使用find()、find_all() 查询匹配单个结果或者多个结果
如果对CSS选择器熟悉建议使用select()
记住常用的获取属性和文本值的方法

'''