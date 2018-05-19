# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-19 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=40)),
                ('colour', models.CharField(max_length=40)),
                ('plate_num', models.DecimalField(decimal_places=2, max_digits=20)),
                ('seats_available', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'ordering': ['seats_available'],
            },
        ),
        migrations.CreateModel(
            name='Driver_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('departure_time', models.DateTimeField(auto_now_add=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('car_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Car')),
            ],
            options={
                'ordering': ['destination'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', tinymce.models.HTMLField(blank=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_profile', to=settings.AUTH_USER_MODEL)),
                ('rider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rider_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Tag'),
        ),
        migrations.AddField(
            model_name='driver_profile',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Location'),
        ),
        migrations.AddField(
            model_name='driver_profile',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='driver_profile',
            name='pickup_locations',
            field=models.ManyToManyField(related_name='pickup', to='driver.Location'),
        ),
        migrations.AddField(
            model_name='driver_profile',
            name='reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Review'),
        ),
    ]