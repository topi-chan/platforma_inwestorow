import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def listToString(s):
    str1 = " "
    return (str1.join(s))

lib = []
lib2 = []
url = 'https://www.ncbr.gov.pl/o-centrum/aktualnosci/'
www = urllib.request.urlopen(url, context=ctx).read()
#print(www)
soup = BeautifulSoup(www, 'html.parser')
div = soup.find_all("div", {"class": "read-more-wrapper"})
paragraphs = []
for x in div:
    paragraphs.append(str(x))
#print(paragraphs)
soup = BeautifulSoup(listToString(paragraphs), 'html.parser')
tags = soup('a')
#print(tags)
for tag in tags:
    lib.append(tag.get('href', None))
#print(lib)
for x in lib:
    if "umowy" in x:
        y = "https://www.ncbr.gov.pl" + x
        lib2.append(y)
#print(lib2)
for z in lib2:
    print(z)
    www = urllib.request.urlopen(z, context=ctx).read()
    soup = BeautifulSoup(www, 'html.parser')
    descr = soup.find("meta",  property="og:description")
    print(descr["content"])
