"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from MyDjangoApp.views import *
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', indexes),
#     path('MyDjangoApp/', index),
#     path('start/', start_scrapy),
# ]
from Mybook import views

#check是APP名，views是接口所在的文件名

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('saveBook/',views.saveBook),  #在网页上输入127.0.0.1:8000/save即可进入该接口，只需要带入相应参数和请求类型
    path('getBookList/',views.getBookList),  #图书列表
    path('getCatalogList/',views.getCatalogList),  #目录列表
    path('getBookDetails/',views.getBookDetails),  #图书详情
    path('getSearchBookList/',views.getSearchBookList),  #图书搜索
    path('getVersion/',views.getVersion),  #通知
    path('saveRecommendBook/',views.saveRecommendBook),  #保存推荐图书数据
    path('isMarketPass/',views.isMarketPass),  #保存推荐图书数据
    # path('spiderJjwxc/', spider_jjwxc_novel.setData()),  #晋江文学城数据
    # url(r'^card_list_vew',views.card_list_view),
]

