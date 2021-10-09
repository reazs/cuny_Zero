import re
from cunyzero import app
from flask import render_template, url_for, redirect, flash
import datetime as dt
from cunyzero.forms import RegistrationForm, LoginForm

current_year = dt.datetime.now().year

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data} {form.last_name.data}! Wait for the registrar approval.', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index')) 
        else:
            flash('Login Failed! Check your credentials.', 'danger')
    return render_template('login.html', form=form)


# @app.route("/<name>")
# def login(name):
#     return render_template("login.html")