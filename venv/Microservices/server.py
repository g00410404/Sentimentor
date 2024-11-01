from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/members")
def members():
    return jsonify({"members": ["member1", "member2", "member3"]})

if __name__ == "__main__":
    app.run(debug=True)
