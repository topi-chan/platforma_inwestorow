import sys
sys.path.append("/Users/maciek/Library/Mobile Documents/com~apple~CloudDocs/django/platforma_inwestorów/platforma_inwestorow")
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platforma_inwestorow.settings')
django.setup()
from django.core.mail import send_mail
from background_task import background
from django.contrib.auth.models import User
import itertools
from scraper.models import *
from datetime import date

class MailExtractor:
    '''wyciąga listę do mailingu pod instytucję/lookup'''

    def __init__(self):
        self.users = User.objects.all()
        self.news = News.objects.all()
        self.recipient_list = []
        self.content_list = []
        self.link_list = []

    def sorted(self, agency):
#        lub: interest = Institution.objects.get(name = agency)
        for user in self.users:
            if user.interest1 is not None and user.interest1.name == agency:
                interest = Institution.objects.get(name = agency)
                for news in self.news:
                    if news.agency==interest and news.date_added==date.today():
                        self.recipient_list.append(user.mail)
                        self.content_list.append(news.content)
                        self.link_list.append(news.link)
            elif user.interest2 is not None and user.interest2.name == agency:
                interest = Institution.objects.get(name = agency)
                for news in self.news:
                    if news.agency==interest and news.date_added==date.today():
                        self.recipient_list.append(user.mail)
                        self.content_list.append(news.content)
                        self.link_list.append(news.link)
            elif user.interest3 is not None and user.interest3.name == agency:
                interest = Institution.objects.get(name = agency)
                for news in self.news:
                    if news.agency==interest and news.date_added==date.today():
                        self.recipient_list.append(user.mail)
                        self.content_list.append(news.content)
                        self.link_list.append(news.link)

def create_content(content_list):
    content = ""
    content += '\n'.join(content_list)
    return content



mailing = MailExtractor()
mailing.sorted("NCBR")
cwl = list(itertools.chain.from_iterable(zip(list(dict.fromkeys
    (mailing.content_list)),list(dict.fromkeys(mailing.link_list)))))
content = create_content(cwl)

send_mail(
    'Nowe informacje - NCBR',
    content,
    'maciej.topolewski@gmail.com',
    set(mailing.recipient_list),
    fail_silently=False,
)


mailing = MailExtractor()
mailing.sorted("RPOSL")
cwl =  list(itertools.chain.from_iterable(zip(list(dict.fromkeys
   (mailing.content_list)),list(dict.fromkeys(mailing.link_list)))))

content = create_content(cwl)

send_mail(
    'Nowe informacje - RPOSL',
    content,
    'maciej.topolewski@gmail.com',
    set(mailing.recipient_list),
    fail_silently=False,
)


mailing = MailExtractor()
mailing.sorted("PARP")
cwl =  list(itertools.chain.from_iterable(zip(list(dict.fromkeys
   (mailing.content_list)),list(dict.fromkeys(mailing.link_list)))))

content = create_content(cwl)

send_mail(
    'Nowe informacje - PARP',
    content,
    'maciej.topolewski@gmail.com',
    set(mailing.recipient_list),
    fail_silently=False,
)
