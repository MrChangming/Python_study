import urllib.request

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 "
                  "Safari/537.36 "
}

# 因为urlopen方法中不能存储字典，所以headers不能传递进去
# 请求对象的定制
# 注意，因为参数顺序的问题，不能直接写url 和headers 中间还有data 所以我们需要关键字很多

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

print(content)
