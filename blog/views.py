from django.shortcuts import render,HttpResponse

# Create your views here.

from blog.models import *


def index(request):
    return render(request,'index.html')


def add_mysql(request):
    b = Book(name='python', price=9898, pub_date='2015-4-4')#创建数据库
    b.save()#保存数据库
    return HttpResponse("添加成功")