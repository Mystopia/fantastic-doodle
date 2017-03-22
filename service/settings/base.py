from datetime import timedelta

import dj_database_url

from service.settings import *

BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

SECRET_KEY = None

DEBUG = False

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES['default'] = dj_database_url.config()
