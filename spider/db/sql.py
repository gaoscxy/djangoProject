import json
import os

import MySQLdb
import pymysql
import time

# from conf.config import global_config

def addbook(conn, book_name, book_author,book_introduce):
    cur = conn.cursor()
    strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    str = ','.join(book_introduce)
    sql = r'INSERT INTO mybook_bookinfo (book_name,book_author,book_introduce,book_update_time) VALUES("%s","%s","%s","%s");' \
          % (book_name, book_author, str,strtime)
    cur.execute(sql)
    lastrowid = cur.lastrowid
    cur.close()
    conn.commit()
    return lastrowid

def addchapters(conn, chapter_name, chapter_path,book_id):
    cur = conn.cursor()
    cur.execute("insert into mybook_chapterinfo(chapter_name,chapter_path,book_id) values(%s , '%s' , '%s' )" % (
    chapter_name, chapter_path,book_id))
    cur.close()
    conn.commit()

# 链接数据库,返回db对象
def get_mysql_db():
    #链接数据库
    # connection=pymysql.connect(host=global_config.getRaw('dbconfig', 'host'),user=global_config.getRaw('dbconfig', 'user'),
    #                             password=global_config.getRaw('dbconfig', 'password'),port=global_config.getRaw('dbconfig', 'port'),
    #                             db=global_config.getRaw('dbconfig', 'db'))
    connection=pymysql.connect(host='LOCALHOST',user='root',
                                password='123456',port=3306,
                                db='book_database')
    return connection