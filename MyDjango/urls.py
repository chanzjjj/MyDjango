"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    url(r'^login_demo/$', views.login_demo),
    # path('yoyo/<year>/<month>.html', views.yoyo)
    url(r'yoyo/(?P<year>[0-9]{4})/(?P<month>[0-9]{2}).html', views.yoyo),
    url(r'^personal/$', views.personalView),
    url(r'^nav/$', views.navView),
    url(r'^qq/$', views.get_info),
    url(r'^info/$', views.add_info)
]