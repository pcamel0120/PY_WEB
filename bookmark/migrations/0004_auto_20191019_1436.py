# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-19 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_bookmark_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date'),
        ),
    ]
