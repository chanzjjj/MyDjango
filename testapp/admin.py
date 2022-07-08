from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_title = "登录 | xx后台管理系统"
admin.site.site_header = "xx后台管理系统"
admin.site.index_title = "后台管理系统"


class ControlPersonInfo(admin.ModelAdmin):
    list_display = ("qq", "name", "age")
    list_display_links = ("age",)
    list_filter = ("qq",)
    list_per_page = 10
    list_editable = ("name",)
    search_fields = ("qq","name")
    ordering = ("-age",)

# 注册PersonInfo
admin.site.register(models.PersonInfo, ControlPersonInfo)