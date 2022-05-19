# 使用urllib来获得百度首页的源码
import urllib.request

# 1.定义一个url，要访问的网站
url = "http://www.baidu.com"

# 2.限制浏览器想服务器发送请求 response响应
response = urllib.request.urlopen(url)

# 3.获得响应中的页面的源码
content = response.read().decode("utf-8")

# 4.打印数据
print(content)