# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0009_auto_20170829_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display_url',
            field=models.URLField(blank=True, verbose_name='展示url'),
        ),
    ]
