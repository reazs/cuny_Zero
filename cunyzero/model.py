from cunyzero import db, login_manager
from flask_login import UserMixin


# two function to login a User(Student and Instructor)
@login_manager.user_loader
def load_student(user_id):
    return StudentInfo.query.get(int(user_id))

@login_manager.user_loader
def load_instructor(user_id):
    return InstructorInfo.query.get(int(user_id))

# Student model for the database
class StudentInfo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #emplid = db.Column(db.Integer, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    honors = db.Column(db.Boolean, nullable=False, default=False)

# Instructor model for the database
class InstructorInfo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    #prof_id = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Administrator(db.Model):
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

