import json
import os

import MySQLdb
import pymysql

from conf.config import global_config

def addbook(self, book_name, book_author,book_introduce):
    cur = self.conn.cursor()
    cur.execute("insert into novel(book_name,book_author,book_introduce) values(%s , '%s' , '%s')" % (book_name, book_author,book_introduce))
    lastrowid = cur.lastrowid
    cur.close()
    self.conn.commit()
    return lastrowid

def addchapters(self, chapter_name, chapter_path,book_id):
    cur = self.conn.cursor()
    cur.execute("insert into chapter(chapter_name,chapter_path,book_id) values(%s , '%s' , '%s' )" % (
    chapter_name, chapter_path,book_id))
    cur.close()
    self.conn.commit()

# 链接数据库,返回db对象
def get_mysql_db():
    #链接数据库
    connection=pymysql.connect(host=global_config.getRaw('dbconfig', 'host'),user=global_config.getRaw('dbconfig', 'user'),
                                password=global_config.getRaw('dbconfig', 'password'),port=global_config.getRaw('dbconfig', 'port'),
                                db=global_config.getRaw('dbconfig', 'db'))
    return connection