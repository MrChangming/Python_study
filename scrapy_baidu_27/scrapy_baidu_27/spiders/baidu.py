import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，用于使用爬虫的时候使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url的地址，知道是第一次访问的域名
    # statr_urls 是在allowed_domains等等前面添加的一个http//，
    #            在allowed_domains的构面添加一个/
    start_urls = ['http://www.baidu.com/']

    # 是执行了start_urls之后，执行的方法，方法中的response就是返回的就是那个对象
    # 相当于 response = urllib,request.urlopen()
    #       response = requests.get()
    def parse(self, response):
        print('成功')
