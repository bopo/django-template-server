# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_counties'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='链接'),
        ),
    ]