# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksxx',
            name='bkzy',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='报考单位名称'),
        ),
        migrations.AlterField(
            model_name='ksxx',
            name='zydm',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='专业代码'),
        ),
    ]