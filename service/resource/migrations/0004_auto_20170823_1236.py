# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_catalog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resource.Catalog', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(blank=True, choices=[('ios', 'IOS'), ('android', 'Android')], max_length=50, null=True, verbose_name='类型'),
        ),
    ]
