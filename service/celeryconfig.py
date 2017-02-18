import os

CELERY_ACCEPT_CONTENT = ['json']
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_ENABLE_UTC = True
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {
    'debug-task-every-30-seconds': {
      'task': 'service.celery.debug_task',
      'schedule': 30.0,
    }
}
