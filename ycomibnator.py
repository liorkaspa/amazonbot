import requests
from bs4 import BeautifulSoup

# get titles, links and points for each post- save in dict- key: title, value: (link,points)

response = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(response, 'html.parser')
titles = soup.select("td[class='title']>a")
final_score = []
initial_scores = soup.select("td[class='subtext']>span:first-child")
for elem in initial_scores:
    if elem.get('class')[0] == "score":
        score = int(elem.getText().split(" ")[0])
        print(score)
    else:
        score = -1
    final_score.append(score)

dic = {}
for i in range(len(titles[:-1])):
    dic[titles[i].getText()] = (titles[i].get("href"), final_score[i])

output = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
print(output)
