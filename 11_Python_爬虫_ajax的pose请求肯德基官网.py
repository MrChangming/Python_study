# 1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10


# 2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.parse
import urllib.request


# base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

def create_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        "cname": '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.84 Safari/537.36 '
    }

    request = urllib.request.Request(url=base_url, headers=headers, data=data)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码：'))
    end_page = int(input('请输入结束的页面：'))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page, content)
