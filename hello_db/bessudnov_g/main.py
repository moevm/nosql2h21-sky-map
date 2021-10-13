import pymongo
import pprint

greeting_eng = {
    "author" : "Gleb",
    "text" : "Hello, Data Base!",
    "language" : "English",
    "str_id" : "grt_std"
}

greeting_ru = {
    "author" : "Gleb",
    "text" : "Привет, База Данных!",
    "language" : "Russian",
    "str_id" : "grt_std"
}

client = pymongo.MongoClient()
db = client["sky_map"]

hello_db = db["hello_db"]

# hello_db.insert_one(greeting_eng)
# hello_db.insert_one(greeting_ru)

pprint.pprint(hello_db.find_one({"language": "Russian"}))

print(db.list_collection_names())