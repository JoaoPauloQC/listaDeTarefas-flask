from flask import Flask, render_template, url_for, request, make_response, redirect, jsonify, abort


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)