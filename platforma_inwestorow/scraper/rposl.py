from scp_cls import *

rpo = ScraperFromLink("https://scp-slask.pl/strefa_beneficjenta/?category=4")
rpo.get_link("div", {"class": "media-body"}, "", "czytaj")
print(rpo.link_lib)
rpo.get_content_rposl_link()
for c in rpo.content:
    print(c)
'''sprawdzic czy link nie byl na liscie - jesli nie to pobrac tresc'''
