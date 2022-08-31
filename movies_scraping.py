from bs4 import BeautifulSoup
import requests
res=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup=BeautifulSoup(res.text,'html.parser')
titles=soup.select("h3[class='title']")
movies=[]
print(titles)
check=[]
for t in titles:
    movie=t.getText().split(" ",1)
    print(movie)
    movies.append((int(movie[0][:-1]),movie[1].lstrip()))
movies_sorted=sorted(movies,key=lambda x:x[0])
print(movies_sorted)
with open("to watch.txt",'w') as f:
    for movie in movies_sorted:
        f.write(str(movie[0])+str(") ")+movie[1])
        f.write("\n")