import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from rest_framework.decorators import api_view

from Mybook.models import Bookinfo, Chapterinfo


class BookApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields= '_all_'

@api_view(['GET','POST'])
def getBookList(request):
    if request.method =="GET":
        result = Bookinfo.objects.all().values()
        # print(result)
        # return
        response = json.dumps(list(result.values()))
        info_get = {'code': 200,'msg':'scucces','data':list(result.values())}
        return HttpResponse(json.dumps(info_get))
        # return HttpResponse(json.dumps(result))


# @api_view(['GET','POST'])
# def saveBook(request):
#
#     if request.method == "GET":
#         title = request.GET.get('title')
#         name = request.GET.get('name')
#         publisher_id = request.GET.get('publisher_id')
#         # print(title, type(title))
#         # 对数据库进行增加信息操作(增加操作)
#         if (title != ""):
#             chapterinfo = Chapterinfo(name=name)
#             chapterinfo.save()
#             op = Bookinfo(title=title,publisher_id=publisher_id)
#             op.publisher=chapterinfo
#             op.save()
#
#             info_get = {'code': 200,'msg':'succes','data':'insert success'}
#             answer = json.dumps(info_get)
#         else:
#             answer = json.dumps({'statu': '0'})
#         return HttpResponse(answer)
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
