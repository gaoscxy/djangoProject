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

2、接口调用：
----------
进入到MyDjango目录，执行python manage.py runserver 你的ip:8000
在浏览器输入http://ip:8000/ 加上url.py里的方法名和参数即可访问

3、从数据库中读取数据转成json
----------
1、使用values进行调用返回的是valueQuerySet字段，而浊QuerySet,所以先转成list然后再使用json.dumps转成json
2、使用filter进行调用返回在是QuerySet对象，那么就可以直接使用serializers.serialize() 方法转化为json

def search(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        obj = models.Book.objects.filter(host_ip=keyword).values('title','id')
        # obj = models.Book.objects.filter(host_ip=keyword)
        # data = serializers.serialize('json', obj)
        data = json.dumps(list(obj))
    return HttpResponse(data)