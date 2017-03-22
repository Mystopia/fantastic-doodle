from service.settings.base import *

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security: SSL/HTTPS
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https

## Set SECURE_SSL_REDIRECT to True, so that requests over HTTP are redirected to HTTPS.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

## Use ‘secure’ cookies.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

## Use HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
