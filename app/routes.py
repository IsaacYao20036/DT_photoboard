from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'photoboard.db')
db.init_app(app)
app.secret_key = 'correcthorsebatterystaple'

import app.models as models
# from app.forms import Select_Movie, Add_Movie 

@app.route('/')
def home():
    return render_template('home.html')


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
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
