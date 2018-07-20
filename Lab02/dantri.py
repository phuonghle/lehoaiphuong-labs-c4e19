
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pyexcel import *


# 1. Download webpage

url = "http://dantri.com.vn/"


conn = urlopen(url)

data = conn.read()

html = urlopen(url).read().decode("utf-8")

# Save to file - 1 time only

# Html_file = open("dantri.com.html","w")
# Html_file.write(html)
# Html_file.close()



# 2. Extract ROI (Region of interest)


# html, xml, xhtml deu ok
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())


# 3. Extract information

li_list = ul.find_all("li")
# print(li_list)

# li = li_list[0] s
# print(li.prettify())


# li chỉ có 1 con là h4 thì có thể làm trực tiếp
posts = []
for li in li_list:
    post = {}
    a = li.h4.find("a")
    # print(a.prettify())

    # lấy title
    title = a.string
    print(title)


    # lấy link
    href = url + a["href"]
    # thẻ a là kiểu dictionary
    print(href)

    post["title"] = title
    post["href"] = href
    posts.append(post)



# 4. Save data to excel

save_as(records=posts, dest_file_name="dantri.xlsx")

# https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python

