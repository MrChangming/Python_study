# # 1.导入selenium
# from selenium import webdriver
# # 2.创建浏览器操作对象
# browser = webdriver.Chrome(r'd:\Python储存文件\chromedriver.exe')
# # 3.访问网址
# url = 'https://www.baidu.com'
# browser.get(url)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.baidu.com')

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# url = 'https://www.csdn.net/'
# driver.get(url)
# driver.maximize_window()

# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# time.sleep(3)
# driver.quit()
