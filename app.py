# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Create connection to Mongo
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    martian = list(db.collection.find())
    print(martian)

    # return template and data
    return render_template("index.html", martian=martian)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():
   # db.collection.remove({})
   martian = scrape_mars.scrape()
   # db.mars_data.insert_one(martian)
   db.collection.update(
    {},
    martian,
    upsert=True
   )

   return redirect("http://127.0.0.1:5000", code=302)

if __name__ == "__main__":
    app.run(debug=True)
