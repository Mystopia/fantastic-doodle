from datetime import timedelta

import dj_database_url

from service.settings import *

BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

SECRET_KEY = None

DEBUG = False

INSTALLED_APPS += [
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Enable WhiteNoise
    # http://whitenoise.evans.io/en/stable/django.html#enable-whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES['default'] = dj_database_url.config()
