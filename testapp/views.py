from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time

# Create your views here.

def yoyo(request, year, month):
    print("url参数",year, month)
    result = {
        "code":0,
        "data":{
            "year": year,
            "month": month
        }
    }
    return JsonResponse(result)

def hello(request):
    result = {
        "code": 200,
        "message": "success成功",
        "data": {
            "token": "xxxxxxxx",
            "name": "aaa"
        }
    }
    return JsonResponse(result)
    # return HttpResponse("hello world!")

def login_demo(request):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if request.method == "GET":
        return render(request, "login.html", context={"current_time": current_time})
    elif request.method == "POST":
        result = {
            "code": 200,
            "message": "success成功",
            "data": {
                "token": "xxxxxxxx",
                "name": "aaa"
            }
        }
        return JsonResponse(result)
    else:
        return render(request, "login.html")


def personalView(request):
    context = {
        "name": "chanzjj",
        "n_name": "zj",
        "age": 20,
        "fancy": ["python", "selenium", "django"],
        "blog":
            {
                "url": "https://www.cnblogs.com/yoyoketang/tag/",
                "img": "/static/122.jpg"
            }
    }
    class MyBlog():
        def __init__(self):
            self.name = "chanzjj"
            self.age = 20

        def guanzhu(self):
            return 100

        def fensi(self):
            return 1000

    blog = MyBlog()
    context["myblog"] = MyBlog()
    return render(request, "personal.html", context=context)


def navView(request):
    context = {}
    name_list = [
        {
            "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算机网络",
            "value": ["Java", "Python", "C语言"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        },
        {
            "type": "医药",
            "value": []
        }
    ]
    context["nav_list"] = name_list
    return render(request, "nav.html", context)
