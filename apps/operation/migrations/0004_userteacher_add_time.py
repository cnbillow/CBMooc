# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-30 18:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_userteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='userteacher',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]