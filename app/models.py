from app.routes import db, app
from flask_login import UserMixin

Staff_Position = db.Table(
    'Staff_Position',
    db.Column('scode', db.Text(), db.ForeignKey('StaffMember.code')),
    db.Column('pid', db.Integer, db.ForeignKey('Position.id'))
)

Staff_Department = db.Table(
    'Staff_Department',
    db.Column('scode', db.Text(), db.ForeignKey('StaffMember.code')),
    db.Column('did', db.Integer, db.ForeignKey('Department.id'))
)


class StaffMember(db.Model):
    __tablename__ = "StaffMember"
    code = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text())
    fname = db.Column(db.Text())
    lname = db.Column(db.Text())
    photo = db.Column(db.Text())
    division_id = db.Column(db.Integer, db.ForeignKey('Division.id'))
    email = db.Column(db.Text())
    likely_location = db.Column(db.Text())
    positions = db.relationship('Position', backref='staff_member')
    hofs = db.relationship('Faculty', backref='hof')
    hods = db.relationship('Department', backref='hod')
    positions = db.relationship('Position',
                                secondary=Staff_Position,
                                back_populates='staffmembers')
    departments = db.relationship('Department',
                                  secondary=Staff_Department,
                                  back_populates='staffmembers')

    def __repr__(self):
        return self.name


class Division(db.Model):
    __tablename__ = "Division"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    staff_members = db.relationship('StaffMember', backref='division')

    def __repr__(self):
        return self.name


class Position(db.Model):
    __tablename__ = "Position"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    group = db.Column(db.Text())
    staffmembers = db.relationship('StaffMember',
                                   secondary=Staff_Position,
                                   back_populates='positions')

    def __repr__(self):
        return self.name


class Faculty(db.Model):
    __tablename__ = "Faculty"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    hof_code = db.Column(db.Text(), db.ForeignKey('StaffMember.code'))
    departments = db.relationship('Department', backref='faculty')

    def __repr__(self):
        return self.name


class Department(db.Model):
    __tablename__ = "Department"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.id'))
    hod_code = db.Column(db.Integer, db.ForeignKey('StaffMember.code'))
    staffmembers = db.relationship('StaffMember',
                                   secondary=Staff_Department,
                                   back_populates='departments')

    def __repr__(self):
        return self.name


# User table in db for login authentication
# Code from https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/

# Create user model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True,
                         nullable=False)
    hashed_password = db.Column(db.String())
