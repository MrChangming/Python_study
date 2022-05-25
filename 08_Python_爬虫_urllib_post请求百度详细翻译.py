import urllib.request
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'Accept': ' */*',
    # 'Accept-Encoding': ' gzip, deflate, br',
    'Accept-Language': ' zh-CN,zh;q=0.9',
    'Connection': ' keep-alive',
    'Content-Length': ' 135',
    'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=F0392C65E48931BAF918E3CD2B777CD0; PSTM=1648293679; '
              'BAIDUID=F0392C65E48931BA43237D34A659614C:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'H_PS_PSSID=36176_31254_36166_34584_36142_36120_36192_36075_35801_35321_26350_36102_36061; '
              'BA_HECTOR=8181010hak0h0l8h981h480v40q; BAIDUID_BFESS=F0392C65E48931BA43237D34A659614C:FG=1; delPer=0; '
              'PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1648624640; REALTIME_TRANS_SWITCH=1; '
              'FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; '
              'ab_sr=1.0'
              '.1_NmRkODUyYzlhOWQ1OWMwMTBmY2I0NzMxM2VjZThkMWQwZjk4OGUxZmE4M2M3ZjAzZWRkYWM5NjBiMDhiZjlkZTcxZmNmMjUxMjljZWVmNTM2MjdhZTEzMDE5ZTc0NWU4MTE3ZTA1NDRjMzNlOGNhZGZmNDk3ZmNmZDJiZjliZWNjMjg2NjVmYzdhMzgxYzczODI4NDc2MzgyZGVlN2E4MA==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1648627560',
    'Host': ' fanyi.baidu.com',
    'Origin': ' https: //fanyi.baidu.com',
    'Referer': ' https: //fanyi.baidu.com/?datatype=16047',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'Sec-Fetch-Dest': ' empty',
    'Sec-Fetch-Mode': ' cors',
    'Sec-Fetch-Site': ' same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36',
    'X-Requested-With': ' XMLHttpRequest',
}

data = {
    'from': ' en',
    'to': ' zh',
    'query': ' love',
    'trans-type': 'realtime',
    'simple_means_flag': ' 3',
    'sign': ' 198772.518981',
    'token': ' 9230efd483fbff8e24af7c227b4e523b',
    'domain': ' common'
}

# post请求的参数，必须进行编码，并且要调用encode的方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

print(content)

obj = json.loads(content)
print(obj)
