# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ksxx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkh', models.CharField(max_length=10, verbose_name='报名号')),
                ('ksxm', models.CharField(max_length=6, verbose_name='考生姓名')),
                ('ksbh', models.CharField(max_length=16, verbose_name='考生编号')),
                ('zjhm', models.CharField(max_length=19, verbose_name='证件号码')),
                ('bkdw', models.CharField(max_length=20, verbose_name='报考单位名称')),
                ('kczw', models.CharField(max_length=20, verbose_name='考场座位')),
                ('lh', models.CharField(max_length=20, verbose_name='楼号')),
                ('kch', models.CharField(max_length=3, verbose_name='考场号')),
                ('zwbh', models.CharField(max_length=3, verbose_name='座位编号')),
                ('dyjs', models.CharField(max_length=10, verbose_name='对应教室')),
                ('zydm', models.CharField(blank=True, max_length=5, verbose_name='专业代码')),
                ('bkzy', models.CharField(blank=True, max_length=10, verbose_name='报考单位名称')),
            ],
        ),
    ]
