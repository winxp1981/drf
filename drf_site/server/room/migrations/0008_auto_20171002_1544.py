# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20171002_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_photos', to='room.Room'),
        ),
    ]
