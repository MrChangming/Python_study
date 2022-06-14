import scrapy


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['nc.58.com']
    start_urls = ['http://nc.58.com/job']

    def parse(self, response):
        # content = response.text
        # content = response.body
        # print('================')
        # print(content)

        span = response.xpath('//div[@class="list_head"]/div[@class="list_top clearfix"]/span/a/text()')[0]
        print('================')
        print(span)
