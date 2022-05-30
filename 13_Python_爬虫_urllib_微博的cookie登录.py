# 适用的场景，数据采集的时候，需要绕过登录。然后进入到某个页面
# 个人信息页面是utf-8。但还是报错了
# 那么登录页面不是utf-8所以报错

# 访问不成功就是信息不够
import urllib.request

url = 'https://weibo.com/u/7532783660'

headers = {
    # ':authority':' weibo.com',
    # ':method':' GET',
    # ':path':' /u/7532783660',
    # ':scheme':' https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9',
    'cache-control': ' max-age=0',
    # cooike中携带着你的个人信息，如果有登录之后的从尼克，那么我们就可以携带着cooike进入到任何页面
    'cookie': 'SINAGLOBAL=6017069757181.41.1648542856205; XSRF-TOKEN=HRhFhj9UFaH3MN_JDAgCjTjn; '
              'login_sid_t=fe74ae5c628bad4078c0546eab8780a0; cross_origin_proto=SSL; _s_tentry=weibo.com; '
              'Apache=9264603445704.127.1648890072153; ULV=1648890072157:2:1:2:9264603445704.127.1648890072153:'
              '1648542856334; wb_view_log=1536*8641.25; ALF=1680426158; SSOLoginState=1648890159; '
              'SUB=_2A25PTGF_DeRhGeFL6FAW-C3KzTyIHXVsONW3rDV8PUNbmtB-LVatkW9NQiVOrVndbWBB67BZEKEBFIU24b-tM2UH; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5U9JCz4eEI-LC4fNsx9B5D5JpX5KzhUgL'
              '.FoMfe0zN1hecSo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSKeES0n0Soq7; '
              'WBPSESS=D9XkFtGB_kQY1AaQKjY4K7iOJnRVwED_sU5DxpnFMd_1m2H48bQ4BA4isP_5xBz0axpP_HRj71UtJc7HDXGEG4UUxM9r'
              '-r5q29 '
              '-go_TzI6kvm4B-Xluh4k8FdSz0zB7aHuNlMTSUKtwfef1q0r8Yjg==; WBtopGlobal_register_version=2022040217',
    # refere-判断当前路径是不是有上一个路径进来的，一般情况下，是做图片防盗链的
    'referer': 'https://weibo.cn/',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' document',
    'sec-fetch-mode': ' navigate',
    'sec-fetch-site': ' same-origin',
    'sec-fetch-user': ' ?1',
    'upgrade-insecure-requests': ' 1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 '
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

# 将数据保存到本地
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
