import time

from lxml import etree
import requests
import random

from spider.db import sql
from spider.db.save_book import save_book_info, get_book_id_by_name, save_chapter

# url1 = 'http://www.jjwxc.net/onebook.php?novelid=3704522'
# url1 = 'http://www.jjwxc.net/onebook.php?novelid=3373718'
# url1 = 'http://www.jjwxc.net/onebook.php?novelid=3409200'
# url1 = 'http://www.jjwxc.net/onebook.php?novelid=2423737'
# url1 = 'http://www.jjwxc.net/onebook.php?novelid=5502413'
url1 = 'https://www.52shuwu.com/jiakong/16435.html'
url2 = 'https://www.52shuwu.com'

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False

# 爬取HTML的函数
def get_html(url):
    # kv = {'user-agent': user_agent}
    header = {"User-Agent": random.choice(user_agent)}
    re = requests.get(url, headers=header)
    re.encoding = 'utf-8'
    htm1 = re.text
    return htm1


# 根据url获得文章并保存的函数
def get_text(url,name,title):
    html = get_html(url2 + url)
    selector = etree.HTML(html)
    # 得到书的id
    book_id = get_book_id_by_name(name)
    # title = selector.xpath('//*[@class="noveltext"]/div/h2/text()')
    txt = selector.xpath('//*[@class="article-content"]/p/text()')
    print(title)
    mkpath = 'txts\\\\' + name + '\\'
    mkdir(mkpath)
    fp = open(mkpath + '\\' + title + '.txt', 'w',encoding='utf-8')
    # fp = open('txts\\' + title[0] + '.txt', 'w')
    for each in txt:
        fp.write(each + "\n")
    fp.close()
    titlelist = {}
    titlelist[0] = title
    one_chapter = {}
    # 对章节执行保存到数据库的操作
    one_chapter["book_id"] = book_id
    one_chapter["chapter_name"] = titlelist
    one_chapter["chapter_path"] = mkpath + '\\' + title + '.txt'
    # 保存章节信息到章节表
    save_chapter(one_chapter)
    # 延时一秒操作
    time.sleep(1)

def get_url(html):
    # 本书目录信息
    book_info = {}
    selector = etree.HTML(html)
    # /html/body/section/div/div/article/ul/li[1]/a
    # /html/body/section/div/div/article/ul/li[10]/a
    url_list = selector.xpath('//*[@class="column4"]/a/@href')
    # name = selector.xpath('//*[@class="bigtext"]/h1/span/text()')[0]
    # book_info["name"] = name
    # author = selector.xpath('//*[@itemprop="author"]/text()')[0]
    # book_info["author"] = author
    # introduce = selector.xpath('//*[@id="novelintro"]/text()')
    # book_info["introduce"] = introduce
    # 执行存入数据库的操作
    # is_success = save_book_info(book_info)
    # 如果保存书名的时候出错,直接退出本次循环
    # if not is_success:
    #     print("save book faile ,exit this one")

    # for url in url_list:
    #     get_text(url,'不死者')

    for index in range(len(url_list)):
        get_text(url_list[index],"不死者",'第' + (str(index + 1)) + '章')

def save():
    html = get_html(url1)
    get_url(html)


