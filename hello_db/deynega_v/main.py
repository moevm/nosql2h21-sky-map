from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.new_db

hello_world = {
    'string': 'Hello, World!',
    'id': 0
}
res = db.reviews.insert_one(hello_world)
print(res)
print(db.reviews.find_one({'id': 0}))
