import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1649147593405_104&jsoncallback=jsonp105&action' \
      '=cityAction&n_s=new&event_submit_doGetAllRegion=true '

headers = {
    # ':authority': ' dianying.taobao.com',
    # ':method': ' GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1649147593405_104&jsoncallback=jsonp105&action=cityAction&n_s=new'
    #          '&event_submit_doGetAllRegion=true',
    # ':scheme': ' https',
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9',
    'cookie': '_m_h5_tk=6cb9b02b43227065fba83d983750e0ba_1649152938570; '
              '_m_h5_tk_enc=74110e62f851b74f330ca046e06b8e22; cna=Rq7KGqt871gCAbfZmjlfK370; xlly_s=1; '
              't=3bcfdc4e59dcb98910263a82cd3ba0d2; cookie2=1391a4c633c32c74298deb71dace2cfc; v=0; '
              '_tb_token_=587555e1d6358; tfstk=c-0PBB2_XULrhyUBXzaeFOsTH9rRaWy3CZPaq0Lh6khMjOEuQsmApS27wSPFg9ql.; '
              'l=eBOVALuuLRVLGxS3BO5Zlurza77OFIOb8sPzaNbMiInca61RtFsNuNC3saNJSdtjgt5b2etzHj297Rn2rxUU'
              '-NsWHpfuKtyuJI9w8e1..; isg=BIqKYz9E3I7OplAis7g1r0Nt23Asew7VLay1oBTCGF1oxyuB_A4D5CY51zMbN4Zt',
    'referer':' https://dianying.taobao.com/',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36',
    'x-requested-with': ' XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf8")

# split 切割
content = content.split('(')[1].split(')')[0]

with open('21_Python_爬虫_解析_josnpath解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('21_Python_爬虫_解析_josnpath解析淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)



