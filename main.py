# command to run app with debug option: flask --app main.py run

from flask import Flask , render_template, url_for, request, redirect, session
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




class User(db.Model):
    __tablename__ = "users"

    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

with app.app_context():
        db.create_all()
        # print("DB file:", os.path.join(BASEDIR, 'users.sqlite3'))
        # print("Tables:", inspect(db.engine).get_table_names())  # must include 'users'


@app.route("/login", methods=["POST", "GET"])
def login_page():
    css_ = url_for('static', filename='styles.css')
    if request.method == "POST":
        email = request.form["emailAddress"]
        session["emailAddress"] = email
        return redirect(url_for("logged_in"))
    else:
        if "emailAddress" in session:
            redirect(url_for(("logged_in")))
        return render_template("login.html", css_path=css_)

@app.route("/logout")
def logout():
    session.pop("emailAddress", None)
    return redirect(url_for("login_page"))
    
@app.route("/user", methods=["POST", "GET"])
def logged_in():
    if "emailAddress" in session:
        emailAdd = session["emailAddress"]
        return f"<h1>This is your email: {emailAdd}</h1>"
    else:
        return redirect(url_for("login_page"))

@app.route("/register", methods=["POST", 'GET'])
def register_new_user():
    css_ = url_for('static', filename='styles.css')

    if request.method == "POST":
        user_first_name = request.form["first-name"]
        user_last_name = request.form["last-name"]
        user_email_address = request.form["email-address"]
        password = request.form["password"]

        found_user = User.query.filter_by(email=user_email_address).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = User(user_first_name, user_last_name, user_email_address, password)
            db.session.add(usr)
            db.session.commit()
            redirect(url_for("login_page"))
    return render_template("register.html", css_path=css_)

if __name__ == '__main__':
    app.run(debug=True)