# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_auto_20180520_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['seat_capacity']},
        ),
        migrations.RenameField(
            model_name='car',
            old_name='seats_available',
            new_name='seat_capacity',
        ),
    ]