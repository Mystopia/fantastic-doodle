import os

from service.settings.production import *

DEBUG = { 0: False, 1: True }[int(os.getenv('DEBUG'))]

# SSL/HTTPS Security

## Set SECURE_SSL_REDIRECT to True, so that requests over HTTP are redirected to HTTPS.
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False

## Use ‘secure’ cookies.
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

## Use HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    INTERNAL_IPS = (
        '127.0.0.1',
        # Docker IPs
        # '172.20.0.1',
        # '172.20.0.5',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': 'service.settings.local.show_toolbar',
    }

def is_running_in_docker(*args):
    import subprocess
    return 'docker' in subprocess.getoutput('cat /proc/1/cgroup')

def show_toolbar(request):
    if request.is_ajax():
        return False
    return True
