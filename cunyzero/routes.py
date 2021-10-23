from flask.helpers import flash
from cunyzero import app, class_schedule, db
from flask import  render_template, request, redirect, url_for, flash
import datetime as dt
from cunyzero.model import StudentInfo, InstructorInfo
from flask_login import login_user, current_user, logout_user

current_year = dt.datetime.now().year


@app.route("/")
def home():
    for course in class_schedule.classes:
        print(course)

    return render_template("index.html", year=current_year, courses=class_schedule.classes)

# login page that logs in the users if the credentials are correct
@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        if request.form['options'] == 'Student':
            user = StudentInfo.query.filter_by(email=request.form['email']).first()           
        else:
            user = InstructorInfo.query.filter_by(email=request.form['email']).first()   
        if user and (request.form['password'] == user.password):
                login_user(user)
                return redirect(url_for('home'))
        else:
                flash('Login unsuccessful. Check your email and/or password', 'danger')
        print(request.form['options'])
        print(request.form['email'])
        print(request.form['password'])
    return render_template('login_signup/login.html')

# signup page where user chooses whether to sign up as student or instructor
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('login_signup/register_state.html')

# signup page for student
@app.route("/student_signup", methods=['POST', 'GET'])
def student_signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email_check = StudentInfo.query.filter_by(email=request.form['email']).first()
        if email_check:
            flash('This email already has an account!', 'danger')
            return redirect(url_for('student_signup'))
        else:
            student = StudentInfo(f_name=request.form['f_name'], l_name=request.form['l_name'], gpa=request.form['gpa'], 
                    email=request.form['email'], password=request.form['password'])    
            db.session.add(student)
            db.session.commit()
            flash('Your account has been created! You can now login and wait for the confirmation letter.', 'success')
            return redirect(url_for('login'))
    return render_template('login_signup/student_signup.html')


#signup page for instructor
@app.route("/staff_signup", methods=['POST', 'GET'])
def staff_signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email_check = InstructorInfo.query.filter_by(email=request.form['email']).first()
        if email_check:
            flash('This email already has an account!', 'danger')
            return redirect(url_for('staff_signup'))
        else:
            instructor = InstructorInfo(f_name=request.form['f_name'], l_name=request.form['l_name'], 
                        email=request.form['email'], password=request.form['password'])    
            db.session.add(instructor)
            db.session.commit()
            flash('Your account has been created! You can now login and wait for the confirmation letter.', 'success')
            return redirect(url_for('login'))
    return render_template("login_signup/staff_signup.html")

# logout page
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# @app.route("/<name>")
# def login(name):
#     return render_template("login.html")