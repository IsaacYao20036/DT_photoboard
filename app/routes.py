from app import app
from flask import render_template, abort, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import csv

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config[
    'SQLALCHEMY_DATABASE_URI'
    ] = 'sqlite:///' + os.path.join(basedir, 'photoboard.db')
db.init_app(app)
app.secret_key = 'correcthorsebatterystaple'

import app.models as models
from app.forms import Select_StaffMember


@app.route('/')
def home():
    staffmembers = models.StaffMember.query.all()
    return render_template('home.html', staffmembers=staffmembers)


@app.route('/faculty/<int:id>')
def faculty(id):
    faculty = models.Faculty.query.filter_by(id=id).first()
    return render_template('faculty.html', faculty=faculty)


@app.route('/department/<int:id>')
def department(id):
    department = models.Department.query.filter_by(id=id).first()
    return render_template('department.html', department=department)


@app.route('/profile/<code>')
def staffmember(code):
    staffmember = models.StaffMember.query.filter_by(code=code).first()
    return render_template('profile.html', staffmember=staffmember)


@app.route('/search')
def search():
    # form = Select_StaffMember()
    staffmembers_f = models.StaffMember.query.order_by(models.StaffMember.name).all()
    staffmembers_l = models.StaffMember.query.order_by(models.StaffMember.lname).all()
    # form.staffmembers.choices = [(staffmember.code, staffmember.name) 
    #                               for staffmember in staffmembers]
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         print("YAY! - got {}, of type {}".format(form.moviename.data, type(form.moviename.data)))
    #         print("Redirecting to: {}".format(url_for('details', ref=form.moviename.data)))
    #         profile = models.StaffMember.query.filter_by(code=form.staffmember.data).first
    #         return redirect(url_for('staffmember',
    #                                 code=form.staffmembers.data))

    # else:
    #     # print('bugger: {}'.format(form.moviename.data))
    #     # flash("Thats a bad movie, you can't see its details")
    #     return redirect('/')
    return render_template('search.html', staffmembers_f=staffmembers_f,
                           staffmembers_l=staffmembers_l)


def load_from_csv(filename):
    print("Adding...")
    with open(filename, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            add_staffmember(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            print(row)
        print("DONE")


def add_staffmember(code, name, fname, lname, photo, division_id, email, likely_location):
    new_staffmember = models.StaffMember()

    new_staffmember.code = code
    new_staffmember.name = name
    new_staffmember.fname = fname
    new_staffmember.lname = lname
    new_staffmember.photo = photo
    new_staffmember.email = email
    new_staffmember.division_id = division_id
    new_staffmember.likely_location = likely_location

    with app.app_context():
        db.session.merge(new_staffmember)
        db.session.commit()


load_from_csv("app\photoboard.csv")

if __name__ == '__main__':
    app.run(debug=True)
