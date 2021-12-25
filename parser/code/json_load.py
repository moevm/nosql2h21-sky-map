import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['sky_map']
collection_currency = db['celestial_bodies']

with open('1000_db.json') as f:
    file_data = json.load(f)

# collection_currency.insert_one(file_data)
collection_currency.insert_many(file_data)

client.close()