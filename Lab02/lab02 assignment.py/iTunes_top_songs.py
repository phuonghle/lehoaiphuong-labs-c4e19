
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pyexcel import *
from youtube_dl import YoutubeDL

# 1. Download webpage

url = "https://www.apple.com/itunes/charts/songs/"


conn = urlopen(url)
data = conn.read()
html = urlopen(url).read().decode("utf-8")

# Save to file - 1 time only

# Html_file = open("itunes.html","w")
# Html_file.write(html)
# Html_file.close()


# 2. Extract ROI (Region of interest)

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

div = soup.find("div", id="main")
# print(div.prettify())

# 3. Extract information

li_list = div.find_all("li")
# print(li_list)

# li = li_list[0] 
# print(li.prettify())


# # li chỉ có 1 con là h4 thì có thể làm trực tiếp
posts = []
for li in li_list:
    post = {}
    a_h3 = li.h3.find("a")
    a_h4 = li.h4.find("a")
    # print(a.prettify())

#     # lấy song
    song = a_h3.string
    # print(song)

    # lấy singer
    singer = a_h4.string
    # print(singer)

    post["Song"] = song
    post["Singer"] = singer
    # post["text_to_search"] = post["Song"] + (" ") + post["Singer"]
    posts.append(post)



# 4. Save data to excel

# save_as(records=posts, dest_file_name="itunes.xlsx")


# download songs from Utube


    options = {
        'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
        'max_downloads': 1, # Tell downloader to download only the first entry (audio)
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([post["Song"] + (" ") + post["Singer"]])