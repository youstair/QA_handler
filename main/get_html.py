# -*- coding: utf-8 -*-

import urllib3


import urllib.request as url
import random
from bs4 import BeautifulSoup
import collections
import re
import pymysql

user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {"User-Agent":user_agent, "Referer":"http://www.runoob.com/"}


proxy_list = []


class Technique:
    def __init__(self,name):
        self.name = name
        self.table = collections.defaultdict()

    def __add__(self, other):
        self.table.update(other)


def get_html(host):
    """
    通过网址获取HTML文件
    :param host:
    :return:
    """

    try:
        # proxy = random.choice(proxy_list).replace("\n","")
        # print(proxy)
        # proxy_handler = url.ProxyHandler({"http" : proxy})
        proxy_handler = url.ProxyHandler({})
        opener = url.build_opener(proxy_handler)
        request = url.Request(host, headers=header)
        response = opener.open(request, timeout=4)

        # print(response.read().decode('utf-8'))

        return response.read()

    except Exception as e:
        # print(proxy, "failed")
        return None


def analyze_main_page(code):
    html = BeautifulSoup(code)
    middle_columns = html.find_all(name= "div", attrs={"class":re.compile(r"codelist codelist-desktop cate")})
    p = re.compile('<[^>]+>')
    q = re.compile(r"【(学习)*(.*?)】")
    with open("href_list.txt","w") as f:
        for middle_column in middle_columns:
            h2 = middle_column.find(name="h2")
            title = p.sub("", str(h2))
            for item_top in middle_column:
                if(item_top.name == "h2" or item_top == "\n"):
                    continue

                h4 = item_top.find(name="h4")
                title_2 = p.sub("",str(h4))
                print(title," ",re.findall(q, title_2)[0][1])
                f.write(title.replace(" ","")+" "+re.findall(q, title_2)[0][1].replace(" ","")+'\n')
                href = item_top['href']
                print("http:"+href)
                f.write("http:"+href+'\n')
                shortdesc = item_top.find(name="strong").string
                print(shortdesc)
                f.write(shortdesc+'\n')
                img_url = item_top.find(name="img")['src']
                print(img_url)
                f.write(img_url+'\n')
                print('\n')


def get_all_html_href():
    head = "http://www.runoob.com"
    p = re.compile(r"http://www.runoob.com/(.*?)")
    db = pymysql.connect(host = "localhost", user = "root", password = "du045174du", db = "runoob")
    cursor = db.cursor()
    with open("href_list.txt", "r",encoding='GBK') as f:
        title = f.readline()
        while(title != "" and title != None):
            if(title == '\n'):
                continue

            href = f.readline()
            shortdesc = f.readline()
            img_url = f.readline()
            # print(title.replace("\n","").split(" "),href,img_url,shortdesc)

            class_filed = title.replace("\n","").split(" ")[0]
            skill = title.replace("\n","").split(" ")[1]

            # print(class_filed,skill)

            html_code = get_html(href)
            if(html_code == None):
                continue
            html = BeautifulSoup(html_code)
            sidebar = html.find(name="div", attrs={"class":"design", "id":"leftcolumn"})
            for bar in sidebar:
                if(bar == "\n" or bar == None or bar.name != "a"):
                    continue
                side_href = bar["href"]
                try:
                    bar_title = bar["title"]
                except Exception as e:
                    bar_title = bar.string
                if(re.match(p,side_href)):
                    pass
                else:
                    side_href = head + side_href

                sql = """insert into href_list (`href`,`class`,`skill`, `item`) values 
                            ("%s","%s","%s","%s")""" % (side_href, class_filed, skill, bar_title.replace("\n",""))
                print(sql)
                cursor.execute(sql)
                # print(bar_title)
                # print(side_href)
            # print(title)
            title = f.readline()
    db.commit()
    db.close()


if __name__ == '__main__':
    # with open("proxy_list.txt","r") as f:
    #     line = f.readline()
    #     while(line != "" and line != None):
    #         proxy_list.append(line)
    #         line = f.readline()
    #     f.close()
    #
    # print(proxy_list)

    # analyze_main_page(get_html("http://www.runoob.com/")) //获取所有链接简介等

    get_all_html_href()

    # print(get_html("http://www.runoob.com/"))

