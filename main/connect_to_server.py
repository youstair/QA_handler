import pymysql

# -*- coding: utf-8 -*-

db = pymysql.connect(host = "localhost",
                     user = "root",
                     password = "du045174du",
                     db = "runoob",
                     cursorclass=pymysql.cursors.DictCursor)

remote_db = pymysql.connect(host = "132.232.164.211",
                            user = "zzh",
                            password = "123456",
                            db = "runoob")


cursor = db.cursor()

sql = "show tables;"
cursor.execute(sql)

result = cursor.fetchall()
for i in result[:-1]:
    print(i["Tables_in_runoob"])

create_sql = """create table  %s (`id` int auto_increment, `question` text, `answer` text, `link` text, primary key(`id`)) engine = Innodb default charset = utf8;"""
truncate_sql = """truncate table %s"""
insert_sql = """insert into %s (question ,answer, link) value ("%s","%s", "%s")"""


for i in result[:-1]:
    table_name = i['Tables_in_runoob']
    remote_cursor.execute(truncate_sql%table_name)
    print(table_name)
    sql2 = "select question,answer,link from %s"%table_name
    if(table_name=="href_list"):
        continue;
    cursor.execute(sql2)
    items = cursor.fetchall()
    for j in items:
        # print(j['question'], j['answer'], j['link'])
        remote_cursor.execute(insert_sql%(table_name, pymysql.escape_string(j['question']), pymysql.escape_string(j['answer']), j['link']))
    remote_db.commit()
    # break