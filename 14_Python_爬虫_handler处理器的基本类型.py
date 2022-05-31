# 需要使用handler来访问百度，获取网页源代码

import urllib.request

url = 'http://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 "
                  "Safari/537.36 "
}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

print(content)