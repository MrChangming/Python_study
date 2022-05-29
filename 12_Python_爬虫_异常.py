import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/sulixu/article/details/119818949'

url = 'https://www.babayyy.com'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}
try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode("utf8")

    print(content)

except urllib.error.HTTPError:
    print('系统正在升级...')
except urllib.error.URLError:
    print('不要急，还在升级...')
