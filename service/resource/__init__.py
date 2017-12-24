# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

default_app_config = 'service.resource.RConfig'


class RConfig(AppConfig):
    name = 'service.resource'
    verbose_name = (u'资源管理')
