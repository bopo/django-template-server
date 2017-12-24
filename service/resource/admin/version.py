# -*- coding: utf-8 -*-
from django.contrib import admin
from ..models import Version
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'version',
        'depends',
        'install',
        'sha1sum',
        'channel',
        'summary',
        'platform',
        'constraint',
    )
    list_filter = ('created', 'modified', 'constraint')
