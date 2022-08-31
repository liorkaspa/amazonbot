import requests
from bs4 import BeautifulSoup
import os

data ="2022-02-11"
res = requests.get("https://www.billboard.com/charts/hot-100/" + data).text
soup = BeautifulSoup(res, 'html.parser')
#titles=soup.select("ul[class='lrv-a-unstyle-list']>li>h3#title-of-a-story")
top_song=soup.find("a", class_="c-title__link lrv-a-unstyle-link").getText()
print(top_song)
song_names_spans = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
names=[song.getText() for song in song_names_spans]
songs=[top_song]+names
songs_n=[song.strip("\n") for song in songs]
print(songs_n)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
res=sp.search(q=f"track:{songs_n[1]},year:{2021}",type='track')
print(res)
