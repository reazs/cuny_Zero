from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm


app = Flask(__name__)
Bootstrap(app)  # adding bootstrap to the application
# creating database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.secret_key = 'sdjkashdfkj12323'


# creating table

class StudentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emplid = db.Column(db.Integer, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class InstructorInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    prof_id = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class InstructorApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.String, nullable=False)


class StudentApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.String, nullable=False)


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    course_id = db.Column(db.String, nullable=False, unique=True)
    course_time = db.Column(db.String, nullable=False)
    # Todo add more content for courses


class ClassGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String, nullable=False)
    class_id = db.Column(db.String, nullable=False)
    student_name = db.Column(db.String, nullable=False)  # First Last
    numerical_grade = db.Column(db.Float, nullable=False)
    alphabetical_grade = db.Column(db.String, nullable=False)


class FiredInstructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    prof_id = db.Column(db.Integer, nullable=False, unique=True)


class HonorableStudents(db.Model):
    id = db.column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    emplid = db.column(db.String, nullable=False, unique=True)


db.create_all()

student_info = StudentInfo(emplid=123456, f_name="reaz", l_name='shakil', email='reaz@gmail.com', password='123123')
db.session.add(student_info)
db.session.commit()
if __name__ == "__main__":
    app.run(debug=True, )
