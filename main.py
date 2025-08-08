# command to run app with debug option: flask --app hello run --debug

from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/register")
def register_new_user():
    return render_template("register.html")

