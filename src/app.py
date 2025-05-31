from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the mini Docker project!"

@app.route("/notes")
def notes():
    data = [
        {"id": 1, "title": "First Note", "content": "This is my first note."},
        {"id": 2, "title": "Second Note", "content": "This is my second note."}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
