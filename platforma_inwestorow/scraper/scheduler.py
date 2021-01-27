import sys
sys.path.append("/Users/maciek/Library/Mobile Documents/com~apple~CloudDocs/django/platforma_inwestorów/platforma_inwestorow")
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platforma_inwestorow.settings')
django.setup()
from background_task import background
from background_task.models import Task
from datetime import datetime
import time

date_action = datetime(2021, 10, 5)


@background(schedule=60)
def checker_action():
    os.system('python3 checker.py')

checker_action(repeat=Task.HOURLY, repeat_until=date_action)

time.sleep(180)

@background(schedule=60)
def mailing_action():
    os.system('python3 mailing.py')

mailing_action(repeat=Task.HOURLY, repeat_until=date_action)
