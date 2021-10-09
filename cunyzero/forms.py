from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class RegistrationForm(FlaskForm):
    roles = SelectField('roles', choices=[('Student', 'Student'),('Instructor', 'Instructor')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gpa = DecimalField('GPA', validators=[DataRequired()], places=2)
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    roles = SelectField('roles', choices=[('Student', 'Student'),('Instructor', 'Instructor')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Sign In')