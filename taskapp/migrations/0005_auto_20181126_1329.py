# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-26 07:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_auto_20181126_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(default='', upload_to='', verbose_name='Project file'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 13, 29, 31, 19035)),
        ),
        migrations.AlterField(
            model_name='task',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 13, 29, 31, 18940)),
        ),
    ]
