from celery import Celery

# set the default Django settings module for the 'celery' program.
import os
import sys
sys.path.append("/Users/maciek/Library/Mobile Documents/com~apple~CloudDocs/django/platforma_inwestorów/platforma_inwestorow")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platforma_inwestorow.settings')

app = Celery('platforma_inwestorow',
             broker='amqp://',
             backend='rpc://',
             include=['platforma_inwestorow.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

# if __name__ == '__main__':
#     app.start()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
