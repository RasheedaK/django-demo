# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170617_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
