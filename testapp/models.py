from django.db import models

# Create your models here.

class PersonInfo(models.Model):
    '''个人信息'''
    name = models.CharField(max_length=30, blank=True, null=True, default='', verbose_name="姓名")
    age = models.IntegerField(blank=True, null=True, verbose_name="年龄")
    qq = models.CharField(max_length=30,blank=True, null=True,default='',verbose_name="QQ")
    def __str__(self):
        return self.__doc__ + "qq：" + self.qq

    class Meta:
        verbose_name_plural = "用户个人信息"


class PersonInfo_a(models.Model):
    '''个人信息'''
    id_x = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class PersonInfo_b(models.Model):
    '''个人信息'''
    id_x = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    age_x = models.BigIntegerField()
    body = models.TextField(null=True, blank=True, default='')
    data = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    datatime = models.DateTimeField(auto_now=True)
    img = models.ImageField(blank=True, null=True, default='')
    file = models.FileField(blank=True, null=True, default='')
    is_true = models.BooleanField(default=True)
