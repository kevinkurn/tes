from logging import debug
from flask import Flask, render_template, redirect
# Import mongoDB
from flask_pymongo import PyMongo
import scrape_mars
# os.add_dll_directory("PATH_TO_DLL")

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# mars_db = mongo.db.mars_db


@app.route("/")
def index():
    # print("Main page")
    # Read the data from MongoDB"
    # mars_data = {}
    # mars_data["featured_image_url"] = "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"
    mars_info = mongo.db.collection.find_one()
    return render_template("index.html", data=mars_info)

@app.route("/update")
def update_data():
    mars_data = scrape_mars.update()
    # Add or update the data to MongoDB"
    mongo.db.update({}, mars_data, upsert=True)
    return redirect("/")
    # return render_template("index.html", data=mars_data)


if __name__=="__main__":
    app.run(debug=True)