# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_auto_20180520_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_profile',
            name='driver_license',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
    ]