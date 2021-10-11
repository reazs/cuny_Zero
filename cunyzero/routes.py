from cunyzero import app
from flask import  render_template, request
import datetime as dt
from cunyzero import class_schedule

current_year = dt.datetime.now().year


@app.route("/")
def home():
    for course in class_schedule.classes:
        print(course)

    return render_template("index.html", year=current_year, courses=class_schedule.classes)


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        print(request.form["email"])
        print(request.form["password"])

    return render_template("login_signup/login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    # if request.method == "POST":
    #     print(request.form["f_name"])
    #     print(request.form["l_name"])
    #     print(request.form["email"])
    #     print(request.form["bio-content"])
    #     print(request.form["password"])
    return render_template("login_signup/register_state.html")



@app.route("/signup_student")
def student_signup():
    return render_template("login_signup/student_signup.html")



@app.route("/signup_staff")
def staff_signup():
    return render_template("login_signup/staff_signup.html")
# @app.route("/<name>")
# def login(name):
#     return render_template("login.html")