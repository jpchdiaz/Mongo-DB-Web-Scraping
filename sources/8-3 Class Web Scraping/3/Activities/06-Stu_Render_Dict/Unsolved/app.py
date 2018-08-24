# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)

# @TODO: Create a list of dictionaries
# CODE GOES HERE
dogs_list = [{'name': 'fido', 'type': 'shih tzu'},
        {'name': 'rex', 'type': 'collie'},
        {'name': 'suzy', 'type': 'poodle'},
        {'name': 'tom', 'type': 'actually a cat'}]

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
# CODE GOES here
@app.route("/")
def index():
    return render_template('index.html', dogs=dogs_list)

if __name__ == "__main__":
    app.run(debug=True)
