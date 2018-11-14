
import scrapy

class Ju1lyeduSpider(scrapy.Spider):
    name = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index']

    def patse(self,response):
        for julyedt_class in response.xpath('//*[@id="item_12"]/div"]')  #//*[@id="item_12"]/div[2]"]



