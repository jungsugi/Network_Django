# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessGame', '0005_auto_20160607_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominfo',
            name='turn',
            field=models.IntegerField(default=0),
        ),
    ]
