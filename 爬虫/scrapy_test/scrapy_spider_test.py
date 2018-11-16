
import scrapy
from lxml import etree
class Test(scrapy.Spider):
    name = 'test1'
    start_urls = ['https://www.julyedu.com/category/index']
    def parse(self,response):
        print("我是测试parse")
        print (type(response))
        #print (response.xpath('//div[@class="course_info_box"]/a/h4/text()'))
        i= 0
        for test_class in response.xpath('//div[@class="course_info_box"]'):
            title = test_class.xpath('a/h4/text()').extract_first('Default Image')
            desc = test_class.xpath('a/p/text()').extract_first('Default Image')
            desc_time = test_class.xpath('a[1]/p[2]/text()').extract_first('Default Image')
            i= i+1
            print (i,":",title.strip(),"简介：",desc.strip(),desc_time.strip())

            #yield  { 'title':test_class.xpath('a/h4/test()').extract_first()     }

# 命令行 执行
#scrapy runspider scrapy_spider_test.py