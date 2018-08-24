# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
# CODE GOES HERE
@app.route("/")
def index():
    movie_list = ["Forrest Gump", "Princess Mononoke", "Howl's Moving Castle", "Pulp Fiction", "Reservoir Dogs"]
    return render_template("index.html", list=movie_list)
    # pic_list = [
    # "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0,182,268_AL_.jpg",
    # "https://m.media-amazon.com/images/M/MV5BMTVlNWM4NTAtNDQxYi00YWU5LWIwM2MtZmVjYWFmODZiODE5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR4,0,182,268_AL_.jpg",
    # "https://m.media-amazon.com/images/M/MV5BZTRhY2QwM2UtNWRlNy00ZWQwLTg3MjktZThmNjQ3NTdjN2IxXkEyXkFqcGdeQXVyMzg2MzE2OTE@._V1_UY268_CR5,0,182,268_AL_.jpg",
    # "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg",
    # "https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg"
    # ]

if __name__ == "__main__":
    app.run(debug=True)
