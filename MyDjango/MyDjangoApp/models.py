from django.db import models

# Create your models here.
# 对数据库表进行设置

from django.db import models
class Check(models.Model):  # 定义一个类，用于后面对数据库的操作,下面是我的一个例子，里面有表格的字段和数据类型，具体操作可查阅文档
    id = models.AutoField(primary_key=True)
    numb = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

#设计card表
class Card(models.Model):
    card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
    card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")
    class Meta:
        verbose_name_plural = '银行卡账户'
        verbose_name = '银行卡账户—基本信息'
    def __str__(self):
        return self.card_id