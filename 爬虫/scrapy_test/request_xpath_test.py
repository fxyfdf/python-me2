#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lxml import etree
"""
url1 = "https://www.julyedu.com/category/index"
url_content = requests.get(url1)

# 把获取到的网页  保存在文件中
with open('requests_xpath.html','wb+') as f:
    f.write(url_content.content)

#获取到的内容转换格式后，使用 xpath 提前所需内容
selector=etree.HTML(url_content.content)
aa = selector.xpath('//div[@class="course_info_box"]')
aa = selector.xpath('//div[@class="course_info_box"]/a/h4/text()')
print (aa)
for i in aa[0]:
    print (i.xpath('///a/h4/text()'))
data_a= selector.xpath('//*[@id="item_12"]/div[20]/div/a[1]/img/@src')
#data_a= selector.xpath('//*[@id="item_12"]/div[20]/div/a[1]/img[1]/@src')
# for i in data_a:
#     print (i)

# for i in data_a:
#     #print (i)
#     print (i.xpath('a'))
#title= selector.xpath('//dev[@class="course_info_box"]/a[2]')
#data= selector.xpath('//*[@id="item_12"]/div[1]/div/a[1]/p[1]/text()')
#data= selector.xpath('//*[@id="item_12"]/div[1]/div/a[1]/p[2]/text()')
#print (title)
#print (data)
#url2 = 'https://www.julyedu.com' + block1[0]


url1 = "https://www.julyedu.com/category/index"
url_content = requests.get(url1)

# 把获取到的网页  保存在文件中
with open('requests_xpath.html','wb+') as f:
    f.write(url_content.content)

#获取到的内容转换格式后，使用 xpath 提前所需内容
selector=etree.HTML(url_content.content)
aa = selector.xpath('//div[@class="course_info_box"]')
aa = selector.xpath('//div[@class="course_info_box"]/a/h4/text()')









#text一般用于返回的文本  content的一般用于对返回的其他数据类型
#print (url_content)
#print (url_content.text)
#print (url_content.content.decode('utf-8'))



#content2 = requests.get(url2).content.decode('gb2312')

# url1 = "https://www.julyedu.com/category/index"
# url_content = requests.get(url1)
# selector=etree.HTML(url_content.content)
# block1= selector.xpath('/html/body/div[1]/div[2]/ol/li[2]/ol/li[6]/ul/li[1]/a/@href')
# url2 = 'https://www.julyedu.com' + block1[0]
# print (url2)
# #print (block1)

"""
############################################################

url1 = "https://book.douban.com/top250"
url_content = requests.get(url1)

# # 把获取到的网页  保存在文件中
# with open('requests_xpath.html','wb+') as f:
#     f.write(url_content.content)

#获取到的内容转换格式后，使用 xpath 提前所需内容
selector=etree.HTML(url_content.content)
#aa = selector.xpath('//div[@class="course_info_box"]')
aa = selector.xpath('//*[@id="content"]/h1/text()')

print (aa)