# import sys
# sys.path.append("/Users/maciek/Library/Mobile Documents/com~apple~CloudDocs/django/platforma_inwestorów/platforma_inwestorow")
# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platforma_inwestorow.settings')
# django.setup()
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import requests
# from background_task import background

class ScraperFromLink():
    '''bazuje na stronie NCBR.
    Szuka po nazwie działania (np. "nabór", "umowa" itp.) w linku'''

    def __init__(self, url):
        self.url = url
        self.tag_lib = []
        self.link_lib = []
        self.paragraphs = []
        self.content = []
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def list_to_string(self, bs4_content):
        str1 = " "
        return (str1.join(bs4_content))


    def get_link(self, type, name, main_link, lookup):
        www = urllib.request.urlopen(self.url, context=self.ctx).read()
        soup = BeautifulSoup(www, 'html.parser')
        div = soup.find_all(type, name)
        for elem in div:
            self.paragraphs.append(str(elem))
        soup = BeautifulSoup((self.list_to_string(self.paragraphs)), 'html.parser')
        tags = soup('a')
        for tag in tags:
            self.tag_lib.append(tag.get('href', None))
        for tag in self.tag_lib:
            if lookup in tag:
                link = main_link + tag
                self.link_lib.append(link)

    def new_ncbr_scraper(self):
        www = urllib.request.urlopen(self.url, context=self.ctx).read()
        soup = BeautifulSoup(www, 'html.parser')
        content = soup.findAll('li')
        lists = []
        for c in content:
            lists.append(c.get_text())
        position = []
        for list in lists:
            if list.find("ogłasza") != -1:
                position.append(lists.index(list))
                self.content.append(list)
        for pos in position:
            x = content[pos]
            tags = x('a')
            for tag in tags:
                self.link_lib.append("https://www.gov.pl"+tag.get('href', None))

    def get_content_ncbr_link(self):
        for link in self.link_lib:
            www = urllib.request.urlopen(link, context=self.ctx).read()
            soup = BeautifulSoup(www, 'html.parser')
            descr = soup.find("meta", property="og:description")
            self.content.append(descr["content"])

    def get_content_rposl_link(self):
        new_content = []
        for link in self.link_lib:
            www = urllib.request.urlopen(link, context=self.ctx).read()
            soup = BeautifulSoup(www, 'html.parser')
            descr = soup.find("div", {"class": "article"})
            self.content.append(descr)
        for c in self.content:
            soup = BeautifulSoup((c.get_text()),
                'html.parser').find(text=True)
            new_content.append(soup)
        self.content = new_content[:]

class ParpScraper():

    def __init__(self, url, data):
        self.url = url
        self.requests_content = None
        self.content = []
        self.header_content = []
        self.links = []
        self.data = data
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Language': 'en-gb', 'Accept-Encoding': 'br, gzip, deflate',
            'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'http://www.google.com/'}

    def get_links_parp(self):
        self.requests_content = requests.post(self.url, data=self.data,
            headers = self.headers).text
        self.requests_content = self.requests_content.replace('{}'.format("/"), '')
        soup = BeautifulSoup(self.requests_content, 'html.parser')
        lists = []
        lists2 = []
        tags = soup('a')
        for tag in tags:
            lists.append(tag.get('href', None))
        for s in lists:
            if "grants" in s:
                lists2.append(s)
        lists3 = []
        for s in lists2:
            s = (s.replace("{}".format("\\\\"), "{}".format("\\")))
            z = s.split("\\component\\grants\\grants\\")
            lists3.append(z)
        lists4 = []
        for s in lists3:
            lists4.append(s[1])
        lists5 = []
        for s in lists4:
            z = s[:-2]
            self.links.append("https://www.parp.gov.pl/component/grants/grants/"+z)

    def get_header_parp(self):
        '''we względu na dziwactwa PARP pobieram tylko nagłówki z linków'''
        for l in self.links:
            current_link = requests.get(l, headers = self.headers).text
            soup = BeautifulSoup(current_link, 'html.parser')
            descr = soup.find("title")
            if descr.text == "PARP - Centrum Rozwoju MŚP - www.parp.gov.pl":
                pass
            else:
                self.content.append(l)
                self.header_content.append(descr.text)
