import codecs
import json

from django.core import serializers
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view

from Mybook.models import Bookinfo, Chapterinfo, Versioninfo, Recommendinfo
startnum = 0
@api_view(['GET','POST'])
def getBookList(request):
    if request.method =="GET":
        result = Bookinfo.objects.all().values()
        page1 = request.GET.get('page')
        page = int(page1)
        if(page==None):
            result = Bookinfo.objects.all().values()
        # elif(page==1):
        #     result = Bookinfo.objects.all().values()[0:20]
        else:
            result = Bookinfo.objects.all().values()[((page-1)*30):page*30]
        print(result)
        # return
        # response = json.dumps(list(result.values()))
        info_get = {'code': 200,'msg':'scucces','data':list(result.values())}
        return HttpResponse(json.dumps(info_get))
        # return HttpResponse(json.dumps(result))


@api_view(['GET','POST'])
def getCatalogList(request):
    if request.method =="GET":
        book_id = request.GET.get('book_id')
        result = Chapterinfo.objects.filter(bookinfo_id=book_id)
        bookinfo = Bookinfo.objects.filter(book_id=book_id).first()
        order_no = bookinfo.order_no
        Bookinfo.objects.filter(book_id=book_id).update(order_no=order_no+1)
        info_get = {'code': 200,'msg':'scucces','data':list(result.values())}
        return HttpResponse(json.dumps(info_get))
        # return HttpResponse(json.dumps(result)

@api_view(['GET','POST'])
def getBookDetails(request):
    if request.method =="GET":
        path = request.GET.get('path')
        f = open(path, 'r+', encoding='utf-8')
        # f = codecs.open(path, mode='r', encoding='utf-8')  # 打开txt文件，以"utf-8'编码读取
        line = f.read()  # 以行的形式进行读取文件
        info_get = {'code': 200,'msg':'scucces','data':line}
        return HttpResponse(json.dumps(info_get))

@api_view(['GET','POST'])
def getSearchBookList(request):
    if request.method =="GET":
        keyword = request.GET.get('keyword')
        # todo 搜索次数加1
        result = Bookinfo.objects.filter(book_name__contains=keyword)
        if not result:
            result = Bookinfo.objects.filter(book_author=keyword)
        info_get = {'code': 200,'msg':'scucces','data':list(result.values())}
        return HttpResponse(json.dumps(info_get))

@api_view(['GET','POST'])
def getVersion(request):
    if request.method =="GET":
        result = Versioninfo.objects.last()
        data = Versioninfo.toJSON(result)
        print("启动------")
        return HttpResponse(data)
@api_view(['GET','POST'])
def saveRecommendBook(request):

    if request.method == "POST":
        tel = request.POST.get('tel')
        name = request.POST.get('name')
        # print(title, type(title))
        # 对数据库进行增加信息操作(增加操作)
        if (name != ""):
            recommendinfo = Recommendinfo(tel=tel,recommend_name=name)
            recommendinfo.save()
            info_get = {'code': 200,'msg':'succes','data':'insert success'}
            answer = json.dumps(info_get)
        else:
            answer = json.dumps({'code': '112'})
        return HttpResponse(answer)
@api_view(['GET','POST'])
def isMarketPass(request):
    if request.method == "GET":
        info_get = {'code': 200,'msg':'','data':''}
        answer = json.dumps(info_get)
    return HttpResponse(answer)
#
#     elif request.method == "POST":
#         title = request.POST.get('title')
#         name = request.POST.get('name')
#         publisher_id = request.POST.get('publisher_id')
#         # print(title, type(title))
#         # 对数据库进行增加信息操作(增加操作)
#         if (title != ""):
#             chapterinfo = Chapterinfo(name=name)
#             chapterinfo.save()
#             op = Bookinfo(title=title, publisher_id=publisher_id)
#             op.chapterinfo = chapterinfo
#             op.save()
#
#             info_get = {'code': 200,'msg':'succes','data':'insert success'}
#             answer = json.dumps(info_get)
#         else:
#             answer = json.dumps({'statu': '0'})
#         return HttpResponse(answer)
