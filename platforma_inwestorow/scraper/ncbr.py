from scp_cls import *

def iterate_scraper(len, first_url, lookup):
    content = []
    links = []
    for i in range(len):
        obj1 = ScraperFromLink(first_url)
        obj1.get_link("div", {"class": "read-more-wrapper"},
            "https://www.ncbr.gov.pl", lookup)
        obj1.get_content_ncbr_link()
        content.extend(obj1.content)
        links.extend(obj1.link_lib)
        obj2 = ScraperFromLink(first_url)
        obj2.get_link("li", {"class": "last next"},"https://www.ncbr.gov.pl",
        "news")
        first_url = obj2.link_lib[0]
        print("x")
    return content, links

content, links = iterate_scraper(7, 'https://www.ncbr.gov.pl/o-centrum/aktualnosci/',
"ogloszenie")

for c in content:
    print(c)

for l in links:
    print(l)






'''https://www.parp.gov.pl/component/grants/grantss?category=6
szukac zmian jak w zadaniu'''

#next_url = next_site.link_lib[0]


# nie działa value w get_content_ncbr_link, tj. nie da się przekazać argumentu:
# str = "{}\"og:description\"""".format("property=")
# print(str) - to jest słownik?


# for link in links:
#     print(link['title'])
