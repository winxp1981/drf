# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20171026_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]