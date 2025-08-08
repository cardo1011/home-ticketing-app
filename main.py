# command to run app with debug option: flask --app hello run --debug

from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route("/")
def main_page():
    css_ = url_for('static', filename='styles.css')
    return render_template("index.html", css_path=css_)

@app.route("/register")
def register_new_user():
    css_ = url_for('static', filename='styles.css')
    return render_template("register.html", css_path=css_)

