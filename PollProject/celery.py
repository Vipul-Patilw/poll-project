from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PollProject.settings')

celery_app = Celery('PollProject')
celery_app.conf.enable_utc = False
celery_app.conf.update(timezone="Asia/Kolkata")
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
   
    'run-every-5minute': {
        'task': 'Poll.tasks.delete_old_polls',
        'schedule': crontab(minute=5),
        'args': (),
    },
}

celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
	print(f"Request: {self.request!r}")
	
	
