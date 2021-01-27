# djangoProject
第一个python程序
=======

1、数据库操作：
-------
迁移到数据库命令：
python manage.py makemigrations
python manage.py migrate

需要注意的是这两个命令默认情况下是作用于全局，也就是对所有最新更改的models或者migrations下面的迁移文件进行对应的操作，如果要想仅仅对部分app进行作用的话  则执行如下命令：

python manage.py makemigrations appname,

python manage.py migrate appname,

如果要想精确到某一个迁移文件则可以使用：

python manage.py migrate appname 文件名
