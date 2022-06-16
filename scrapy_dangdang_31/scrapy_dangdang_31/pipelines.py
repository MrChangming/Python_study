# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道，那么就必须在settings中开启管道
class ScrapyDangdang31Pipeline:
    # 在爬虫文件执行之前执行的方法
    def open_spider(self, spider):
        self.fp = open('photo.json', 'w', encoding='utf-8')

    # items就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式不推荐，因为每一个传递过来的对象，那么就打开一次文件，对文件的操作过于频繁
        # # 1.write方法必须要写一个字符串，而不是其他的对象
        # # 2.w模式会对没一个对象打开一次文件，覆盖之前的内容
        # with open('photo.json', 'a', encoding='utf-8')as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行之后执行的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request


# 多条管道同时开始
#   1.定义管道类
#   2.在settings中开启管道
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './photo/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
