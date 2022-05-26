# get请求
# 获取豆瓣电影的第一页的数据，并且保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

# 数据下载到本地
# open方法默认情况下使用的是gbk的编码，如果要想保存汉族，那么需要在open方法中指定编码格式为utf-8
# （一）fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)

with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)





