
import scrapy

class QQNesSpider(scrapy.spiders):
    name = 'qqnews'
    start_urls = ["https://new.qq.com/ch/visit/"]

    def parse(self,response):
        for url1 in  response.xpath('//*[@id="20181115A10ZO5_5"]/div/h3'):
            full_url = url1.xpath('//*[@id="20181115A10ZO5_5"]/div/h3/a/@href')
            title_name = url1.xpath('//*[@id="20181115A10ZO5_5"]/div/h3/text()')

        def parse_news(self,response):
            print (1)
