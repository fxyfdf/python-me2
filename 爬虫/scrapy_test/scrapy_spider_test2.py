
import scrapy
# 多个地址池
class Test(scrapy.Spider):
    name = 'test1'
    start_urls = ['https://www.cnblogs.com/pick/#p%d' % p for p in range(1,5)]
    def parse(self,response):
        for blog in response.xpath('//div[@class="post_item"]'):
            yield {
                'recommend1': blog.xpath('div[@class="digg"]/div/span/text()').extract_first('Default Image').strip(),
                'title':blog.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first('Default Image').strip(),
                'title_url':blog.xpath('div[@class="post_item_body"]/h3/a/@href').extract_first('Default Image').strip(),
                'title_read':blog.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span/a/text()').extract_first(
                    'Default Image').strip(),
                'title_time':blog.xpath('//*[@id="post_list"]/div[1]/div[2]/div/text()').extract()[1].strip()
            }
            #  no  推荐  title  title_url  title_read   title_time
            recommend1 = blog.xpath('div[@class="digg"]/div/span/text()').extract_first('Default Image').strip()
            title = blog.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first('Default Image').strip()
            title_url = blog.xpath('div[@class="post_item_body"]/h3/a/@href').extract_first('Default Image').strip()
            title_read = blog.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span/a/text()').extract_first('Default Image').strip()
            title_time = blog.xpath('//*[@id="post_list"]/div[1]/div[2]/div/text()').extract()[1].strip()
            print (recommend1,title,title_url,title_read,title_time)
            # with open('aaaaaa.txt', 'wb+') as f:
            #     f.write(aa_str)
            #yield recommend1,title,title_url,title_read,title_time
            #yield  { 'title':test_class.xpath('a/h4/test()').extract_first()     }
# 命令行 执行
#scrapy runspider scrapy_spider_test2.py