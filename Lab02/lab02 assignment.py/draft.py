from urllib.request import urlopen, quote
from bs4 import BeautifulSoup
from pyexcel import *
from youtube_dl import YoutubeDL


posts = {
    "name" : ["linh", "loan", "mai"],
    "age" : [22, 23, 34]
}



for value in posts.values():
    print(value)

https://stackoverflow.com/questions/29069444/returning-the-urls-as-a-list-from-a-youtube-search-query



# query = quote(text_to_search)
# youtube_url = "https://www.youtube.com/results?search_query=" + query
# response = urlopen(youtube_url)
# html = response.read()
# soup = BeautifulSoup(html)
# for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#     print('https://www.youtube.com' + vid['href'])