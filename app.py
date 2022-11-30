from flask import Flask, render_template, request, redirect, url_for, session, flash
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
        return render_template("home.html", scores=scores), 200
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

    if not data:
        return "Oops, game data not found.", 404
    if "username" not in data.keys() or "score" not in data.keys() or "date" not in data.keys():
        return "Invalid data.", 400
    if "id" in data.keys() or "password" in data.keys():
        return "Invalid data.", 400

    try:
        scores.add_score(data["username"], data["score"], data["date"])
        scores.save()
        return "Score added.", 200
    except ValueError:
        return "Invalid data.", 400

@app.route("/user/<username>")
def user(username):
    """User page route

    Methods:
        GET

    Returns:
        Document or string: a page and a status code
    """
    if "username" not in session:
        flash("You must be logged in to access this page.")
        return redirect(url_for("login")), 301

    try:
        file = Score("scores.json")
        scores = file.get_scores()
        return render_template("user.html", scores=scores), 200
    except ValueError:
        return "Invalid data", 400

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Route to user login

    Methods:
        POST

    Returns:
        A document with a status code
    """
    if request.method == "POST":
        try:
            # Get the username and password from the form
            data = request.form
            scores = Score("scores.json")
            if scores.find_user(data["username"], data["password"]):
                session["username"] = data["username"]
                return redirect(url_for("user", username=session["username"])), 301
            else:
                flash("Invalid username or password.")
                return redirect(url_for("login")), 301
        except ValueError:
            return "Invalid data.", 400

    return render_template("login.html"), 200
    
@app.route("/logout")
def logout():
    """
    Route to logout

    Methods:
        GET

    Returns:
        A document with a status code
    """
    if "username" not in session:
        flash("You must be logged in to access this page.")
        return redirect(url_for("login")), 301

    session.pop("username", None)
    return redirect(url_for("home")), 301

@app.route("/delete", methods=["POST"])
def delete():
    """
    Route to delete a game score

    Methods: 
        POST

    Returns:
        A document with a status code
    """
    if "username" not in session:
        flash("You must be logged in to access this page.")
        return redirect(url_for("login")), 301

    scores = Score("scores.json")
    
    data = request.form

    try:
        scores.delete_score(data["id"])
        scores.save()
        return redirect(url_for("user", username=session["username"])), 301
    except ValueError:
        return "Invalid data.", 400

if __name__ == "__main__":
    app.run(debug=True)