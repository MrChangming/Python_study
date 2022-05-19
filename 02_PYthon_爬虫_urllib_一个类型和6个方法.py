import urllib.request

url = "http://www.baidu.com"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)

# content = response.read(5)
# print(content)

# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回状态吗 如果是200了  那么证明我们的逻辑没有问题
# pirnt(response.getcode))

# 返回的是url的地址
print(response.geturl)

# 获取的是状态信息
print(response.getheader())