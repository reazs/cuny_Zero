from cunyzero import app
from flask import  render_template, request
import datetime as dt

current_year = dt.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year=current_year)


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        print(request.form["email"])
        print(request.form["password"])


    return render_template("login.html")



@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        print(request.form["f_name"])
        print(request.form["l_name"])
        print(request.form["email"])
        print(request.form["bio-content"])
        print(request.form["password"])
    return render_template("signup.html")

# @app.route("/<name>")
# def login(name):
#     return render_template("login.html")