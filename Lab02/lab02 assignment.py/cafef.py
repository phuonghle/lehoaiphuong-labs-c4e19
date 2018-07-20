from urllib.request import urlopen
from bs4 import BeautifulSoup
from pyexcel import *


# 1. Download webpage

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"


conn = urlopen(url)

data = conn.read()

html = urlopen(url).read().decode("utf-8")

# Save to file - 1 time only

# Html_file = open("cafef.html","w")
# Html_file.write(html)
# Html_file.close()



# 2. Extract ROI (Region of interest)

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
# print(div.prettify())

# 3. Extract information
# tìm tr

tr_list = div.find_all("tr")
print(tr_list)

# tr = tr_list[0] 
# print(tr.prettify())


# tìm tất cả td

# posts = []

for tr in tr_list:
    # post = {}
    td = tr.find_all("td")
    a_td = td.find_all("b_r_c")
    print(a_td)

# in td




# #     # lấy data
#     q1 = a_td.string
#     # print(q1)


#     post["Q1"] = q1
#     # post["Q2"] = q2
#     # post["Q3"] = q3
#     # post["Q4"] = q4
    
#     posts.append(post)



# # 4. Save data to excel

# save_as(records=posts, dest_file_name="cafef.xlsx")