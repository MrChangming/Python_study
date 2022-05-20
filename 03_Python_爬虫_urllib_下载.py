import urllib.request

# 下载网页
url_page = "http://www.baidu.com"

# url代表的是下载的路径  filename文件的名字
# 在Puthon中，可以变量的名字，也可以直接写值
urllib.request.urlretrieve(url_page, "baidu.html")

# 下载图片
# url_img = "http://5b0988e595225.cdn.sohucs.com/images/20190401/0040c415689a4488bd7bc707c8aac3e7.jpeg"
# urllib.request.urlretrieve(url=url_img, filename="万民臣服.jpg")
# 下载视频
url_video = "https://vd2.bdstatic.com/mda-ncubbpik242344fi/sc/cae_h264_delogo/1648541286651744057/mda-ncubbpik242344fi.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1648544761-0-0-cad0fec6e2372810caf3f72b6f115613&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=2161526597&vid=2896938686228218180&abtest=100815_2-101130_2-101245_4-17451_2&klogid=2161526597"

urllib.request.urlretrieve(url_video, "bzd.mp4")