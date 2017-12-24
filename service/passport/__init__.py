# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'service.passport.PassportConfig'


class PassportConfig(AppConfig):
    name = 'service.passport'
    verbose_name = _(u'Passport 认证')
