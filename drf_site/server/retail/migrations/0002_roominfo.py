# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='rooms')),
            ],
        ),
    ]
