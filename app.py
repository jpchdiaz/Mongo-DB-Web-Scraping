# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    martian = mongo.db.collection.find()

    # return template and data
    return render_template("index.html", martian=martian)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    news = scrape_mars.mars_news()
    img = scrape_mars.scrape_surf()
    weather = scrape_mars.mars_weather()
    facts = scrape_mars.mars_facts()
    hemis = scrape_mars.mars.hemis()

    # Store results into a dictionary
    mars_stats = {
        "Hemisphere": hemis['title'],
        "Hemisphere Image": hemis['img_url']
    }

    # Insert forecast into database
    mongo.db.collection.insert_one(mars_stats)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
