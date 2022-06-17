import scrapy
from scrapy_movie_32.items import ScrapyMovie32Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一个名字和第二个的页面
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # 第二页的地址是
            url = 'https://www.ygdy8.net' + href
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # 注意如果拿不到数据的情况下，一定检查你的xpath是否正确

        # src = response.xpath('//div[@id="Zoom"]/span/img/@src')
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 接受到请求的meta参数的值
        name = response.meta['name']
        movie = ScrapyMovie32Item(src=src, name=name)
        yield movie
