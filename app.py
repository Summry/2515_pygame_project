from flask import Flask, render_template, request
from models.score import Score
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdflkjhasdflkjhasdflkjh"

@app.route("/")
def home():
    """Home page route

    Methods:
        GET

    Returns:
        Document or string: a page and a status code
    """
    try:
        file = Score("scores.json")
        scores = file.get_scores()
        return render_template("index.html", scores=scores), 200
    except ValueError:
        return "Invalid data", 400

@app.route("/add", methods=["POST"])
def add_score():
    """
    Route to add a game score

    Methods: 
        POST

    Returns:
        A document with a status code
    """
    scores = Score("scores.json")
    
    data = request.json

    """
    data = {
        "id": some string,
        "score": some integer
    }
    """

    if not data:
        return "Oops, game data not found.", 404
    if "id" not in data.keys() or "score" not in data.keys():
        return "Invalid data.", 400

    try:
        scores.add_score(data["id"], data["score"])
        scores.save()
        return "Score added.", 301
    except ValueError:
        return "Invalid data.", 400

if __name__ == "__main__":
    app.run(debug=True)