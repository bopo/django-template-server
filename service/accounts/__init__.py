# -*- coding: utf-8 -*-
default_app_config = 'service.accounts.AccountsConfig'
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'service.accounts'
    verbose_name = _(u'用户管理')
