import datetime



# 保存书本信息到数据库
import time

from spider.db.sql import get_mysql_db, addbook


def save_book_info(one_book_dict):
    # 获取链接对象
    db = get_mysql_db()
    # 获取游标对象
    cursor = db.cursor()

    if not one_book_dict:
        return
    # 获取书名
    book_name = one_book_dict.get('name')
    # 获取书本的作者
    book_author = one_book_dict.get('author')
    # 获取书本的简介
    book_introduce = one_book_dict.get("introduce")
    # 执行存入数据库的操作

    addbook(db,book_name,book_author,book_introduce)
    # strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # str = ','.join(book_introduce)
    # sql = r'INSERT INTO mybook_bookinfo (book_name,book_author,book_introduce,) VALUES("%s","%s","%s");' \
    #       % (book_name, book_author, str)
    # try:
    #     cursor.execute(sql)
    #     db.commit()
    #     print(datetime.datetime.now())
    #     print("success save book")
    #     cursor.close()
    #     db.close()
    #     return 1
    # except:
    #     db.rollback()
    #     print(datetime.datetime.now())
    #     print("rollback once")
    #     cursor.close()
    #     db.close()
    #     return 0



# 根据书名获取数据库中的id
def get_book_id_by_name(book_name):
    db = get_mysql_db()
    cursor = db.cursor()

    sql = 'SELECT book_id FROM mybook_bookinfo WHERE book_name="%s";' % book_name

    cursor.execute(sql)

    res = cursor.fetchone()

    cursor.close()
    db.close()

    if res:
        return res[0]
    else:
        return 0


# 根据name,查询数据库并更改intro的值设
def set_book_introduce_by_book_name(book_name,book_introduce):
    db = get_mysql_db()
    cursor = db.cursor()
    sql = r'update mybook_bookinfo set book_introduce="%s"  where book_name="%s";' % (book_introduce,book_name)
    try:
        cursor.execute(sql)
        db.commit()
        print(datetime.datetime.now())
        print("set has_chapter value success")
    except:
        db.rollback()

    cursor.close()
    db.close()


# 根据one_chapter字典保存信息到chapter表中
def save_chapter(one_chapter):
    # 获取传值
    bookinfo_id = one_chapter.get("book_id")
    chapter_name = one_chapter.get("chapter_name")[0]
    chapter_path = one_chapter.get("chapter_path")
    # 获取db
    db = get_mysql_db()
    cursor = db.cursor()
    sql = r"INSERT INTO mybook_chapterinfo (bookinfo_id,chapter_name,chapter_path) VALUES(%s,'%s','%s');" \
          % (bookinfo_id, chapter_name, chapter_path)
    try:
        cursor.execute(sql)
        db.commit()
        print(datetime.datetime.now())
        print("success save one chapter")
    except:
        db.rollback()

    cursor.close()
    db.close()
