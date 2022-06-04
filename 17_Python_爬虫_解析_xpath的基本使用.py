from lxml import etree

# xpath解析
# 1.本地文件                                                etree.parse
# 2.服务器响应的数据 response.read().decode('utf-8') ******   etree.HTML()

tree = etree.parse('17_Python_爬虫_解析_xpath的基本使用.html')

# li_list = tree.xpath('//body/ul/li')

# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为1的li标签
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找id为l1的标签，注意引号的问题
li_list = tree.xpath('//ul/li[@id="l1"][@class="s1"]/text()')

# 查询id中包含l的li标签
# li_list = tree.xpath('//ul/li[contains(@id, "l")]/text()')

# 插叙id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')

print(li_list)
print(len(li_list))