# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2021-01-31 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20210131_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='horaro_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]