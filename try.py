import urllib
from bs4 import BeautifulSoup
res=[]
a=[]

def get_review(output):
    reviews = soup2.select("span[data-visible-text]")
    for r in reviews:
        sibling = r.findNextSibling()
        if sibling:
            output.append(r.getText()[:-3] + sibling.getText())
        else:
            output.append(r.getText())
        print(output)
        return output


req = urllib.request.Request("https://www.rest.co.il/rest/80146968/page-1/" )
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    soup2 = BeautifulSoup(the_page, 'html.parser')
    print(get_review(res))