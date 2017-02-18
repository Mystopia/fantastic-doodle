from service.settings.base import *

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
