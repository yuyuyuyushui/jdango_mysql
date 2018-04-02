from django.db import models
#创建数据表的类
# Create your models here.


class Book(models.Model):# 继承数据库模块
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()