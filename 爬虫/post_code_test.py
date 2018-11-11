import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

'''
class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    # 处理标签开始
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass


def get_province_entry(url):
    # 获取文本，并用gb2312解码
    content = requests.get(url).content.decode('gb2312')
    print(content)
    # 确定要查找字符串的开始结束位置，并用切片获取内容。
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()
    provinces = []
    # 生成Sax处理器
    handler = DefaultSaxHandler(provinces)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return provinces

def get_province_entery(url):
    # TODO
    content = requests.get(url).content

provinces = get_province_entry('http://www.ip138.com/post')
print(provinces)

'''
f1 = open("E:/PYTHON/PyCharm/txt-file/1.txt",'w')
f2 = open("E:/PYTHON/PyCharm/txt-file/2.txt",'w')
url2 = "http://www.ip138.com/post"
#拿到页面的内容
content2 = requests.get(url2).content.decode('gb2312')
#print (content2)
f1.write(content2)
#提取从哪一行开始
start = content2.find('<map name=\"map_86\" id=\"map_86\">')
end = content2.find('</map>')
content2 = content2[start:end + len('</map>')].strip()
print (content2)
f2.write(content2)
def get_province_entry(url):
    # TODO
    pass