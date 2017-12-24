# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'nick', 'gender', 'idcard', 'phone',)
    search_fields = ('name', 'nick', 'phone')
    list_filter = ('gender',)

