# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 21, 12, 32, 43, 644662, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(upload_to='static/uploaded_images/staff_photo'),
        ),
    ]
