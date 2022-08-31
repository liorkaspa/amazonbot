from bs4 import BeautifulSoup
import lxml
output=[]


with open("rest.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')


link = soup.find(href=True)['href']
page=soup.select_one("ul[class='pagination']>li:last-child>a").getText()
pages=[i+1 for i in range(8)]

reviews = soup.select("span[data-visible-text]")
for r in reviews:
    sibling=r.findNextSibling()
    if sibling:
        output.append(r.getText()[:-3]+sibling.getText().replace("\n",""))
    else:
        output.append(r.getText().replace("\n",""))

for o in output:
    print(o)
    #print("\n") 
    pritn("hi")
#print(reviews)

