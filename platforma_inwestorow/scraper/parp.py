import requests
#from requests.auth import HTTPBasicAuth
#auth = HTTPBasicAuth('trial', 'trial') - w razie potrzeby logowania
import json
from scp_cls import ParpScraper

url = "https://www.parp.gov.pl/component/grants/grantss"
#data to slownik z polami
data_parp = {"module": "grants",
    "data" :"category%3D0%26term%255B%255D%3D1%26term%255B%255D%3D2",
    "option": "com_ajax", "site": 1, "title": 2, "limit": 0, "format": "json"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept-Language': 'en-gb', 'Accept-Encoding': 'br, gzip, deflate',
    'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'http://www.google.com/'}
# r = requests.post(url, data=data_parp, headers = headers)
# print(r.text)
# print(r.request.headers)
parp = ParpScraper(url, data_parp)
parp.get_links_parp()
"col-xl-3 col-md-6 col-12 pb-3 wow pulse"
"<title>Program Akceleracyjny: Startup Spark 2.0 - PARP - Centrum Rozwoju MŚP</title>"
#print(parp.links)
parp.get_header_parp()
print(parp.header_content)
print(parp.content)
