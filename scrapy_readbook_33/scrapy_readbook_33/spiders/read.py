import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_33.items import ScrapyReadbook33Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/photo/1188_\d+.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()
            book = ScrapyReadbook33Item(name=name, src=src)
            # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
            # item['name'] = response.xpath('//div[@id="name"]').get()
            # item['description'] = response.xpath('//div[@id="description"]').get()
            yield book
