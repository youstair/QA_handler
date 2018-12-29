# -*- coding: utf-8 -*-


import re
import urllib.request as url
import pymysql
from bs4 import BeautifulSoup
import get_html
import nlp_process
import collections
from lxml import etree
import signal
import threading
import sys
import os
import psutil




db = pymysql.connect(host = "localhost", user = "root", password = "du045174du", db = "runoob")
cursor = db.cursor()

qa = collections.namedtuple("qa", "h text")


QA = collections.namedtuple("qa", "question answer")

def _split(article_intro):
    """
    要重写
    :param article_intro:
    :return:
    """
    # print(type(article_intro))

    tag_list = []
    # print(len(tag_list))


    a_h = ""
    for i in article_intro:
        if(i == "\n" or i == None):
            continue
        if(i.name == "h1" or i.name == "h2"):
            if(a_h != ""):
                tag_list.append(a_h)
                a_h = ""
            i = str(i).replace("\n", "")
            i = i.replace(" ", "")
            a_h = a_h + i
        else:
            a_h = a_h + str(i)
    tag_list.append(a_h)
    # print(len(tag_list))



    return tag_list




def f(item):
    """

    :param item:
    :return:
    """
    host = item[1]
    text = get_html.get_html(host)
    xpath = """//*[@id="content"]"""
    html = etree.HTML(text)
    article_intro = html.xpath(xpath)

    article_intro = BeautifulSoup(etree.tostring(article_intro[0]))
    article_intro = article_intro.find(name="div", attrs={"class": "article-intro", "id": "content"})

    p = re.compile('<[^>]+>')

    tag_list = _split(article_intro)

    QAs = []

    for i in tag_list:

        # print(i)
        part = BeautifulSoup(i)
        # print("XXXX"*30)
        title = list(part.find("body").children)[0]
        # print(str(title))
        title = p.sub("", str(title))

        # print("~~~~"*30)


        rowQ = [item[3],item[4],title]
        # print(rowQ)

        # print(rowQ)

        # print(i)
        question = nlp_process.get_question_by_rowQ(rowQ)
        # print(question)
        qa = QA(question, i)
        QAs.append(qa)

    return QAs



if __name__ == '__main__':



    sql = "select class from href_list group by class;"
    create_sql = """create table  %s (`id` int auto_increment, `question` text, `answer` text, `link` text, primary key(`id`)) engine = Innodb default charset = utf8;"""
    cursor.execute(sql)
    class_s = cursor.fetchall()
    table_name = ""
    for i in class_s:
        # 创建数据表
        table_name = i[0]
        table_name = table_name.replace(".","_").replace("/","_")
        cursor.execute(create_sql%table_name)
        db.commit()
    for class_ in class_s:
        sql2 = """select skill from href_list where class = "%s" group by skill;"""%class_[0]
        table_name = class_[0].replace(".", "_").replace("/", "_")
        cursor.execute("truncate table %s;"%table_name)
        # sql2 = """select skill from href_list where class = "服务端" group by skill;"""
        print(sql2)
        cursor.execute(sql2)
        skills = cursor.fetchall()
        print(skills)
        num = 1
        for skill in skills:
            sql3 = """select * from href_list where class = "%s" and skill = "%s";"""%(class_[0],skill[0])
            # sql3 = """select * from href_list where class = "%s" and skill = "%s";"""%("服务端", "Python")
            print(sql3)
            cursor.execute(sql3)
            items = cursor.fetchall()
            print(items)

            insert_sql = """insert into %s (question ,answer, link) value ("%s","%s", "%s")"""
            for item in items:
                # try:
                #     print("~~~~"*30)
                #     print(item)
                #     f(item)
                #     print("~~~~"*30)
                # except Exception as e:
                #     print(repr(e))
                # continue
                # QA = f(item)
                try:

                    QAs = f(item)
                    for i in QAs:
                        print("~~~"*30)
                        print(table_name,num, i.question)
                        num += 1
                        cursor.execute(insert_sql%(table_name,pymysql.escape_string(i.question), pymysql.escape_string(i.answer), item[1]))
                        db.commit()
                except Exception as e:
                    print(repr(e))
                print("-"*50)
            print(class_[0]+" "+skill[0]+"finished")

        print(class_[0]+" finished")

    db.close()