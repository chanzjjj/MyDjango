# Generated by Django 2.0.3 on 2022-06-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20220610_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
