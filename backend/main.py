from flask import Flask, request, url_for, render_template
import pymongo
import json
from bson import json_util

### Setup DB
client = pymongo.MongoClient()
db = client["sky_map"]
collection = db["celestial_bodies"]

### Create app
app = Flask(__name__)

### landing page
@app.route("/")
@app.route("/home")
def main():
    ### paste here some fancy page
    return render_template("index.html", title="Sky Map")

@app.route("/sky_object")
def sky_object():
    pgc = request.args.get("object_pgc", 1)
    doc = collection.find_one({"pgc": pgc}, {"_id": 0})
    return render_template("card.html", obj=doc)

### list elements
@app.route("/sky_map_list", methods=["GET"])
def sky_map_list():
    
    ## use 'page' parameter for pagination
    page = int(request.args.get("page", 1))
    per_page = 20

    ## find all docs for specific page
    docs = collection.find().sort("name").skip(per_page * (page - 1)).limit(per_page)
    print(docs)
    docs_count = collection.count_documents({})
    links = {
        "self": {"href": url_for(".sky_map_list", page=page, _external=True)},
    }

    ## link for the prev page
    if page > 1:
        links["prev"] = {
            "href": url_for(".sky_map_list", page=page - 1, _external=True)
        }

    ## link for the next page
    if page - 1 < docs_count // per_page:
        links["next"] = {
            "href": url_for(".sky_map_list", page=page + 1, _external=True)
        }

    # for doc in docs:
    #     doc["link"] = {
    #         "href": url_for(".sky_object", object_pgc=doc["pgc"], _external=True)
    #     }
    
    ### here we will return list of sky objects and links for buttons
    info = {
        "sky_objects": docs,
        "links": links,
    }
    return render_template("search.html", data=info)

### inserting new object
@app.route("/sky_map_insert", methods=["POST"])
def sky_map_insert():
    ### here we take json from request. make sure that in the form we are sending json with right structure
    sky_object = request.get_json()
    collection.insert_one(sky_object)
    return json.dump(sky_object)