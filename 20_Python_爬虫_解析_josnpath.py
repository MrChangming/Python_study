import jsonpath
import json

obj = json.load(open('20_Python_爬虫_解析_josnpath.json', 'r', encoding='utf-8'))

# print(obj)

# 书店所有的书的作者
# author_list = jsonpath.jsonpath(obj, '$.store.photo[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj, '$..author')
# print(author_list)

# store下面的所有的元素
# tag_list = jsonpath.jsonpath(obj, '$.store')
# print(tag_list)

# store里面所有东西的prince
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# 第三个书
# photo = jsonpath.jsonpath(obj, '$..photo[2]')

# # 最后的书
# photo = jsonpath.jsonpath(obj, '$..photo[(@.length-1)]')

# 中间两本书
# photo = jsonpath.jsonpath(obj, '$..photo[0,1]')
# photo = jsonpath.jsonpath(obj, '$..photo[:2]')

# 条件过滤需要在（）的前面添加一个问号
# 过滤出所有的包含isbn的书
# photo = jsonpath.jsonpath(obj, '$..photo[?(@.isbn)]')

# 那本书超过了10块钱
book = jsonpath.jsonpath(obj, '$..photo[?(@.price>10)]')
print(book)
