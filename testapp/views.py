from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time
from testapp.models import PersonInfo

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


def get_info(request):
    '''查询'''
    if request.method == 'GET':
        querystring = request.GET
        print("获取get请求提交的参数", querystring)
        qq_value = request.GET.get("qq")
        name_value = request.GET.get("name")
        try:
            info = PersonInfo.objects.get(qq=qq_value)
            print("返回的object", info)
        except:
            info = {"code": 1}
        context = {
            "info": info,
            "code": 0
        }
    return render(request, "info.html", context=context)


def add_info(request):
    '''修改数据'''
    context = {
        "info": ""
    }
    if request.method == "GET":
        return render(request, "add_info.html")
    if request.method == "POST":
        body = request.POST
        print("获取到post提交的数据：", body)
        qq_value = request.POST.get("qq", '')
        name_value = request.POST.get("name", '')
        age_value = request.POST.get("age", 0)
        print("获取到的数据：", qq_value,name_value,age_value)
        info = PersonInfo.objects.filter(qq=qq_value)
        print("info信息",info)
        if len(info) >= 1:
            # 数据已经存在，并修改
            if name_value:
                info[0].name = name_value
            if age_value:
                info[0].age = age_value
            info[0].save()
            context = {
                "info": "qq号已经存在，修改成功"
            }
        else:
            if not age_value:
                PersonInfo.objects.create(qq=qq_value,
                                          name=name_value)
                context = {
                    "info": "新增成功"
                }
            else:
                PersonInfo.objects.create(qq=qq_value,
                                        name=name_value,
                                        age=int(age_value))
                context = {
                    "info": "新增成功"
                }
        return render(request, "add_info.html", context=context)