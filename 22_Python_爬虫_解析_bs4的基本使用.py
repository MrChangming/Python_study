from bs4 import BeautifulSoup

# 通过解析本地文件，来将bs4的基础语法进行讲解
soup = BeautifulSoup(open('22_Python_爬虫_解析_bs4的基本使用.html', encoding='utf-8'), 'lxml')

# 根据标签名查找结点
# 找到的是第一个符合条件的数据
# print(soup.a)
# # 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# 1.find
# 返回的是第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值里找到的对应的标签对象
# print(soup.find('a', title='a2'))

# 根据class的值找到对应标签对象，注意的是class需要添加下划线
# print(soup.find('a', class_="a1"))

# 2.find_all 返回的是一个列表，并且返回了所有的a标签
# print(soup.find_all('a'))

# 如果想要获取的是多个标签的数据，，那么需要早find_all的参数中添加的是列表的数据
# print(soup.find_all(['a', 'span']))

# limit作用是查找前几个数据
# print(soup.find_all('li', limit=2))

# 3.select
# select返回的是一个列表，并且返回的是多个数据
# print(soup.select('a1'))

# 可以通过.a1的方式代表class,我们把这种操作叫做类选择器
# print(soup.select('.a1'))

# print(soup.select('#l1'))

# 属性选择器--通过属性来寻找对应的标签
# 查找li标签中有id的标签
# print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# 要找的是div下面的li
# print(soup.select('div li'))

# 子代选择器
# 某标签的第一级子标签
# 注意：很多的计算机编程语言中不加红歌不会输出内容，倒在bs4中不会报错
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有的对象
# print(soup.select('a,li'))

# 结点信息
# 获取结点内容
# obj = soup.select('#d1')[0]
# 如果标签对象中，只有内容，那么string和get_text()都可以使用
# 如果标签对象中，除了内容还有标签，那么string就获取不到数据而get_text()是可以获取数据的
# 推荐使用get_text()
# print(obj.string)
# print(obj.get_text())

# 结点的属性
# obj = soup.select('#p1')[0]
# # name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取结点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])