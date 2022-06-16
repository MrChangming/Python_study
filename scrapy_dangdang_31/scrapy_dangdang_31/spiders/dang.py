import scrapy
from scrapy_dangdang_31.items import ScrapyDangdang31Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果是多页下载的话，那么必须要调用的是allowed_domains的范围,一般情况下只能写域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipelines     下载数据
        # items         定义数据结构
        # src = //ul[@id="component_59"]/li//img/@src
        # alt = //ul[@id="component_59"]/li//img/@alt
        # price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 所有的select的对象都可以再次调用xpath的方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他图片标签的属性是不一样的
            # 第一张的src是可以使用的，其他图片的地址是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdang31Item(src=src, name=name, price=price)

            # 获得一个book就将book交给pipelines
            yield book

        # 每一个页的爬取的业务逻辑全都是一样的，我们只需要执行那个网页的请求再次调用parse方法就可以了
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            # 怎么调用parse方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback是你要执行的那个函数，注意不需要加括号
            yield scrapy.Request(url=url, callback=self.parse)
