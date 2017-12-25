
try:
    from .base import *
except Exception as e:
    raise e

INSTALLED_APPS += [
    'servuce.passport.registration',
    'servuce.passport',
    'servuce.accounts',
    'servuce.resource',
    'servuce.frontend',
]