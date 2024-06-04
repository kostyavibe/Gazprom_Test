from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'send-birthday-notifications-every-day': {
        'task': 'notifications.tasks.send_birthday_notifications',
        'schedule': crontab(hour=0, minute=0),  # Выполнять каждый день в полночь
    },
}
