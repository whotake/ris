# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-16 18:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20161216_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 18, 59, 32, 94362, tzinfo=utc)),
        ),
    ]
