# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_driver_profile_driver_license'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver_profile',
            old_name='driver_license',
            new_name='license_number',
        ),
    ]