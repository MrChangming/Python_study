# 通过登录，然后进入主页

# __VIEWSTATE: xhCTBgcw1K024UAkLgGff3Gl5Cn4nCY7B7vR/ksUj4T+FfDfXLkOfOVKx8nMdlj+CUv1Ktt6oeP2JZNFIhCJw62zB9ZaFLaF+zqDkSyzfMR12uwkzs+bFZchhQQ=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 18770650504
# pwd: a1786131912
# code: r209
# denglu: 登录

# 我们观察到__VIEWSTATE __VIEWSTATEGENERATOR code是一个可以变化的量

# 难点：1.__VIEWSTATE __VIEWSTATEGENERATOR 一般情况看不到数据，都是在页面的源代码中
#      我们观察到这两个数据在页面的源代码中，所以我们需要获取页面的源代码，然后进行解析就可以获取了
#      2.验证码

import requests

# 这是登录界面的url的地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.84 Safari/537.36 "
}

response = requests.get(url=url, headers=headers)
content = response.text
# print(content)

# 解析页面源码 然后获取 __VIEWSTATE __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(viewstategenerator)
# print(viewstate)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
# print(code_url)

# 有坑
# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# request里面有一个方法 session（）通过session的返回值，就能使用请求变成一个对象

session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
# 注意刺客要使用二进制数据，因为我们要使用的 是图片下载
content_code = response_code.content
# wb的模式就是二进制数据写人到文件
with open('code.jpg', 'wb')as fp:
    fp.write(content_code)

# 获取了验证码的图片之后，下载到本地，然后观察验证码，观察之后，在控制台输入这个验证码，就可以将这个值给
# code的参数，就可以登录
code_name = input('请输入你的验证码:')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '18770650504',
    'pwd': 'a1786131912',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)
