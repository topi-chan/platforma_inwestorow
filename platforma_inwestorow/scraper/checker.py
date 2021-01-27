from scp_cls import *
from datetime import date
import sys
sys.path.append("/Users/maciek/Library/Mobile Documents/com~apple~CloudDocs/django/platforma_inwestorów/platforma_inwestorow")
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platforma_inwestorow.settings')
django.setup()
from scraper.models import *

ncbr = ScraperFromLink('https://www.gov.pl/web/ncbr/wydarzenie?page=1')
ncbr.new_ncbr_scraper()

lookup_dict = {ncbr.link_lib[i]: ncbr.content[i] for i in range(len(ncbr.link_lib))}

for l in sorted(lookup_dict):
    try:
        news = News.objects.get(link=l)
    except:
        agency = Institution.objects.get(name="NCBR")
        news = News(link=l, content = lookup_dict.get(l),
            type="ogloszenie", date_added = date.today(), agency = agency)
        news.save()


rpo = ScraperFromLink("https://scp-slask.pl/strefa_beneficjenta/?category=4")
rpo.get_link("div", {"class": "media-body"}, "", "czytaj")
rpo.get_content_rposl_link()
lookup_dict = {rpo.link_lib[i]: rpo.content[i] for i in range(len(rpo.link_lib))}
print(lookup_dict)

for l in sorted(lookup_dict):
    try:
        news = News.objects.get(link=l)
    except:
        agency = Institution.objects.get(name="RPOSL")
        news = News(link=l, content = lookup_dict.get(l),
            type="ogloszenie", date_added = date.today(), agency = agency)
        news.save()


url = "https://www.parp.gov.pl/component/grants/grantss"
data_parp = {"module": "grants",
    "data" :"category%3D0%26term%255B%255D%3D1%26term%255B%255D%3D2",
    "option": "com_ajax", "site": 1, "title": 2, "limit": 0, "format": "json"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept-Language': 'en-gb', 'Accept-Encoding': 'br, gzip, deflate',
    'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'http://www.google.com/'}

parp = ParpScraper(url, data_parp)
parp.get_links_parp()
parp.get_header_parp()

lookup_dict = {parp.content[i]: parp.header_content[i] for i in range(len(parp.content))}
print(lookup_dict)

for l in sorted(lookup_dict):
    try:
        news = News.objects.get(link=l)
    except:
        agency = Institution.objects.get(name="PARP")
        news = News(link=l, content = lookup_dict.get(l),
            type="ogloszenie", date_added = date.today(), agency = agency)
        news.save()


#do zrobienia dla przeszukiwania kilku stron z ncbr - iterate_scraper
#działa jednak na razie ze starą stroną:
#from ncbr import iterate_scraper
# content, links = iterate_scraper(7,
# 'https://www.ncbr.gov.pl/o-centrum/aktualnosci/', "ogloszenie")
# lookup_dict = {links[i]: content[i] for i in range(len(links))}
#
# for l in sorted(lookup_dict):
#     try:
#         news = News.objects.get(link=l)
#     except news.DoesNotExist:
#         agency = Institution.objects.get(name="NCBR")
#         news = News(link=l, content = lookup_dict.get('l'),
#             type="ogloszenie", date_added = date.today(), agency = agency)
#         news.save()
