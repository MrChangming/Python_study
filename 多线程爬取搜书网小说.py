import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
import time


def geturl(url):
    page_text = requests.get(url=url, headers=headers).content
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[2]/div[4]/div[6]/dl')
    for dl_list in li_list:
        dd = dl_list.xpath('./dd')
        for a in dd:
            title = a.xpath('./a/text()')[0]
            if "**" in title:
                title = title.replace('**', '星星')
            all_title.append(title)
            url = a.xpath('./a/@href')[0]
            detail_url = 'https://www.soshuw.com/' + url
            all_detail_url.append(detail_url)


def response(urls):
    detail_response = requests.get(url=urls, headers=headers).content
    detail_tree = etree.HTML(detail_response)
    detail_page = detail_tree.xpath('/html/body/div[3]/div[6]')
    for br in detail_page:
        data = br.xpath('./text()')
        data = data[1:]
        data = ''.join(data)
        data.split()
        data = ''.join(data)
        all_page.append(data)


def write_all(all_title, all_page):
    i = 1
    for x in range(len(all_title)):
        file_name = dir_name + str(i) + all_title[x] + '.txt'
        i = i + 1
        print(all_title[x], 'over!!!')
        fp = open(file_name, 'w', encoding='utf-8')
        fp.write(all_page[x])


def write_page(all_title, all_page, o):
    for x in range(len(all_title)):
        if o == x:
            x = x - 1
            file_name = dir_name + all_title[x] + '.txt'
            print(all_title[x], 'over!!!')
            fp = open(file_name, 'w', encoding='utf-8')
            fp.write(all_page[x])
        else:
            pass


def select_page(o):
    write_page(all_title, all_page, o)
    while True:
        con = input("是否想要继续下载（yes/no）")
        if con == 'yes':
            o = int(input('请输入你想要爬取的章节:'))
            write_page(all_title, all_page, o)
            continue
        elif con == 'no':
            print("下载完成！")
            break


if __name__ == '__main__':

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'
    }
    y = input('创建储存文件夹：')
    dir_name = f'/pythonProject1/no/{y}/'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    all_detail_url = []
    all_title = []
    all_page = []
    while True:
        x = input('搜索小说，写入小说名称（每个字首字母大写)：')
        url = f'https://www.soshuw.com/{x}/'
        geturl(url)
        print(f'共有{len(all_title)}章')
        if len(all_title) == 0:
            print("输入错误，请重新输入！")
            continue
        else:
            break
    with ThreadPoolExecutor(80) as t:
        for urls in all_detail_url:
            t.submit(response, urls)
            time.sleep(0)
    ad = input('你是否需要爬取所有章节（yes/no）或退出（任意键）:')
    if ad == 'yes':
        write_all(all_title, all_page)
    elif ad == 'no':
        o = int(input('请输入你想要爬取的章节:'))
        select_page(o)
    else:
        print("已退出")
