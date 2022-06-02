import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 "
                  "Safari/537.36 "
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http': '106.55.15.244:8889'
    
}

handler = urllib.request.ProxyHandler(proxies=proxies)
#
opener = urllib.request.build_opener(handler)

# response = urllib.request.urlopen(request)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
