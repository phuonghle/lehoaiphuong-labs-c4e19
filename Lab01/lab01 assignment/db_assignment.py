from pymongo import MongoClient

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot


uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# connect to DB

client = MongoClient(uri)

# take out the database

db = client.get_default_database()

#  1. add post to Posts
new_post = {
    "title" : "C4E 19",
    "author" : "Hoài Phương",
    "content" : "._."
}

# create collections

posts = db["posts"]
customers = db["customers"]

# insert docs into the collection

posts.insert_one(new_post)

# 2a. count refs in Customers

# for ref in customers: 

ads = db.customers.count({"ref" : "ads"})
events = db.customers.count({"ref" : "events"})
wom = db.customers.count({"ref" : "wom"})

print(ads)
print(events)
print(wom)

# 2b. draw pie charts

# prepare data

labels = ["events", "advertisements", "WoM"]
values = [events, ads, wom]
colors = ["blue", "yellow", "pink"]


# plot

pyplot.pie(values, 
colors=colors, 
labels=labels,
)
pyplot.axis("equal")

# show

pyplot.show()