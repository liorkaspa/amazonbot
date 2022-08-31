import time

from bs4 import BeautifulSoup
import lxml
import urllib

res = []


def get_review(output):
    reviews = soup2.select("span[data-visible-text]")
    print(soup2)
    for r in reviews:
        sibling = r.findNextSibling()
        print(sibling)
        if sibling:
            output.append(r.getText()[:-3] + sibling.getText())
        else:
            output.append(r.getText())
    print(output)
    return output


with open("rest.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

link = soup.find(href=True)['href']
page = soup.select_one("ul[class='pagination']>li:last-child>a").getText()
pages = [i + 1 for i in range(int(page))]
print(pages)

for page in pages:
    print("https://www.rest.co.il/rest/80146968/page-%d/" % (page))
    req = urllib.request.urlopen("https://www.rest.co.il/rest/80146968/page-%d/" % (page), )
    the_page = req.read()
    soup2 = BeautifulSoup(the_page, 'html.parser')
    print(get_review(req))
    time.sleep(5)


# print(reviews)
