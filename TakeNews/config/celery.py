from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker="redis://localhost:6379", backend="redis://localhost:6379")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# CELERY BEAT TASK

app.conf.beat_schedule = {
    'zoomit_loader': {
        'task': 'news.tasks.update_news',
        'schedule': 3 * 60 * 60 # Once every 3 hours 
    }
}