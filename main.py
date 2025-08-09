# command to run app with debug option: flask --app main.py run --debug

from flask import Flask , render_template, url_for, request, redirect, session
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY")

@app.route("/login", methods=["POST", "GET"])
def login_page():
    css_ = url_for('static', filename='styles.css')
    if request.method == "POST":
        email = request.form["emailAddress"]
        session["emailAddress"] = email
        return redirect(url_for("logged_in"))
    else:
        return render_template("login.html", css_path=css_)
    
@app.route("/user")
def logged_in():
    if "emailAddress" in session:
        emailAdd = session["emailAddress"]
        return f"<h1>This is your email: {emailAdd}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/register")
def register_new_user():
    css_ = url_for('static', filename='styles.css')
    return render_template("register.html", css_path=css_)

