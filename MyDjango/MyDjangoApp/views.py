import json

from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response

from MyDjangoApp.models import Check, Card
from rest_framework.decorators import api_view

class CardAPISerializer(serializers.ModelSerislizer):
    class Meta:
        model = Card
        fields= '_all_'

@api_view(['GET','POST'])
def card_list_view(request):
    cards = Card.objects.all()
    serializers = CardAPISerializer(cards,many=True)
    if request.method == 'GET':
        return Response(serializers.data)
    elif request.method == 'POST':
        verify_data = CardAPISerializer(data = request.data)
        if verify_data.is_valid():
            verify_data.save()
            return Response({"message":"create some data!","data":request.data})
        else:
            return Response(verify_data.errors)
    else:
        return Response({"message":"request method not valid"})

def save(request):
    if request.method == "GET":
        uname = request.GET.get('name')
        unumb = request.GET.get('numb')
        udepartment = request.GET.get('department')
        print(uname, type(uname), unumb, type(unumb), udepartment, type(udepartment))
        # 对数据库进行增加信息操作(增加操作)
        if (uname != "" and unumb != "" and udepartment != ""):
            op = Check(numb=unumb, name=uname, department=udepartment)
            op.save()

            info_get = {'statu': '1'}
            answer = json.dumps(info_get)
        else:
            answer = json.dumps({'statu': '0'})
        return HttpResponse(answer)

    ########################
    # 数据库的查询操作
def getUser(request):
    return HttpResponse()
# try:
#     find = Check.objects.get(numb=unumb)
#     # 查询id为unumb的发票单，返回值为一个对象
# except:
#     info_get = {'statu': '0'}
#     answer = json.dumps(info_get)
#     return HttpResponse(answer)
# else:
#     list_1 = [find.name, find.numb, find.department]
# 通过（object.属性名）获取里面的值在进行后面的操作
