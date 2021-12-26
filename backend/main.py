from flask import Flask, request, url_for, render_template
import pymongo
import json
from bson import json_util
from werkzeug.utils import redirect

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

@app.route("/add_new_object")
def add_new_object():
    return render_template("object.html")

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
    sky_object_raw = request.form
    sky_object = {
        "pgc": sky_object_raw["pgc"],
        "name": sky_object_raw["name"],
        "type": sky_object_raw["type"],
        "coords": {
            "distance": sky_object_raw["distance"],
            "galactic_longitude": sky_object_raw["galactic_longitude"],
            "galactic_latitude": sky_object_raw["galactic_latitude"]
        },
        "galactic_info" : {
            "barred": sky_object_raw["barred"],
            "multiple": sky_object_raw["multiple"],
            "rings": sky_object_raw["rings"],
            "compact": sky_object_raw["compact"],
            "diameter_log": sky_object_raw["diameter_log"]
        },
        "brightness": sky_object_raw["brightness"],
        "radial_speed": sky_object_raw["radial_speed"]
    }
    collection.insert_one(sky_object)
    return redirect("/sky_map_list", code=302)