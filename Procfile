web: gunicorn service.wsgi --log-file -
worker: celery -A service worker --loglevel=info -B
