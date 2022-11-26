from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdflkjhasdflkjhasdflkjh"

@app.route("/")
def home():

    data = []
    with open("scores.json", "r") as fp:
        json_data = json.load(fp)
        for game in json_data:
            data.append(game)

    """
    [
        {
            "id": qwerwqer-qwer-qwer-qwer-qwerqwerqwer",
            "score": 1
        }
    ]
    """
    data = sorted(data, key=lambda x: x["score"], reverse=True)
    return render_template("index.html", data=data), 200

@app.route("/add", methods=["POST"])
def score():

    data = {}
    with open("scores.json", "r") as fp:
        json_data = json.load(fp)
        data["board"] = json_data["board"]
        data["games"] = [game for game in json_data["games"]]

    game = request.json
    """
    {
        "id": "asdfasd-asdf-asdf-asdf-asdfadsfasdf",
        "score": 10
    }
    """
    if not game:
        return "Oops, not found.", 404
    if "id" not in game.keys() or "score" not in game.keys():
        return "There was a problem.", 400
    
    data["games"].append(game)
    with open("scores.json", "w") as fp:
        json.dump(data, fp)
    
    return "Score added", 301

if __name__ == "__main__":
    app.run(debug=True)