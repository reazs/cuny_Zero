from cunyzero import app
from flask import  render_template
import datetime as dt

current_year = dt.datetime.now().year

@app.route("/")
def index():
    return render_template("index.html", year=current_year)


@app.route("/login")
def login():
    return render_template("login.html")


# @app.route("/<name>")
# def login(name):
#     return render_template("login.html")