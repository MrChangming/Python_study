# 1.获取网页的源码
# 2.解析的服务器响应的文件 etree.HTML
# 3.打印

import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/99.0.4844.84 Safari/537.36 "
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpatn的返回值是列表类型
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)


