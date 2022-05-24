#
# # urlencode的应用场景：多个参数的场景
#
# # https://www.baidu.com/s?wd=周杰伦&sex=男
# import urllib.parse
#
# data = {
#     'wd': "周杰伦",
#     'sex': "男",
#     'location': "中国台湾"
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

import urllib.request
import urllib.parse

base_url = "https://www.baidu.com/s?"
data = {
    'wd': "周杰伦",
    'sex': "男",
    'location': "中国台湾"
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 "
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取晚归源码的数据
content = response.read().decode("utf-8")

# 打印数据
print(content)