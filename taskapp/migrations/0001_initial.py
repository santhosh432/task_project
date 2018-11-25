# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-25 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(help_text='Student Roll number', max_length=10)),
                ('course_name', models.CharField(help_text='Student ciurse name', max_length=50)),
                ('task_name', models.CharField(help_text='Student task/project name', max_length=300)),
                ('submitted', models.DateTimeField(default=datetime.datetime(2018, 11, 25, 13, 24, 50, 803733))),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
