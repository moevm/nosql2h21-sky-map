from flask import Flask, request, url_for
import pymongo
import json

### Setup DB
client = pymongo.MongoClient()
db = client["sky_map"]
hello_db = db["hello_db"]

### Create app
app = Flask(__name__)

### landing page
@app.route("/")
@app.route("/home")
def main():
    ### paste here some fancy page
    return "<p>Hello, sky objects!</p>"

### list elements
@app.route("/sky_map/",  methods=["GET"])
def list_sky_map():
    
    ## use 'page' parameter for pagination
    page = int(request.args.get("page", 1))
    per_page = 20

    ## find all docs for specific page
    docs = hello_db.find().sort("name").skip(per_page * (page - 1)).limit(per_page)
    docs_count = hello_db.count_documents({})
    links = {
        "self": {"href": url_for(".sky_map", page=page, _external=True)},
    }

    ## link for the prev page
    if page > 1:
        links["prev"] = {
            "href": url_for(".sky_map", page=page - 1, _external=True)
        }

    ## link for the next page
    if page - 1 < docs_count // per_page:
        links["next"] = {
            "href": url_for(".sky_map", page=page + 1, _external=True)
        }
    
    ### here we will return list of sky objects and links for buttons
    return {
        "sky_objects": [doc.to_json() for doc in docs],
        "links": links,
    }

### inserting new object
@app.route("/sky_map/", methods=["POST"])
def new_cocktail():
    ### here we take json from request. make sure that in the form we are sending json with right structure
    sky_object = request.get_json()
    hello_db.insert_one(sky_object)
    return json.dump(sky_object)