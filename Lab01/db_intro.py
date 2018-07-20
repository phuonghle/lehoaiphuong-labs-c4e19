from pymongo import MongoClient

uri = "mongodb://admin:admin1234@ds137611.mlab.com:37611/c4e19lab"

# connect to DB

client = MongoClient(uri)

# take out the database

db = client.get_default_database()

# create collections

boardgame = db["boardgames"]

# # create documents

# new_game = {
#     "name" : "Catan",
#     "description" : "Best of boardgames"
# }

# # insert docs into the collection


# boardgame.insert_one(new_game)



# get all documents
all_games = boardgame.find()
print(all_games[1]["name"])