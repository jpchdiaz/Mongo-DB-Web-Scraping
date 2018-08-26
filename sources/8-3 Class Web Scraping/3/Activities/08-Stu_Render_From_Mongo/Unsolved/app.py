from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.store_inventory
collection = db.produce

@app.route('/')
def index():
    # @TODO: write a statement that finds all the items in the db and sets it to a variable
    # CODE GOES HERE
    fruits = list(db.collection.find())
    print(fruits)
    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return render_template('index.html', fruits=fruits)


if __name__ == "__main__":
    app.run(debug=True)
