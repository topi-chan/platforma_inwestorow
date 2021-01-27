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


@background(schedule=60)
def checker_action():
    os.system('python3 mailing.py')

checker_action()
