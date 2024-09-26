from app import app
from flask import render_template, abort, redirect, request, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user
from flask_bcrypt import Bcrypt
from os import path
import csv
from io import StringIO
from shutil import copy


basedir = path.abspath(path.dirname(__file__))
db = SQLAlchemy()
app.config[
    'SQLALCHEMY_DATABASE_URI'
    ] = 'sqlite:///' + path.join(basedir, 'photoboard.db')
db.init_app(app)
app.secret_key = 'correcthorsebatterystaple'

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

UPLOAD_FOLDER = 'app'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import app.models as models


@app.route('/')
def home():
    staffmembers = models.StaffMember.query.all()
    return render_template('home.html', staffmembers=staffmembers)


@app.route('/faculty/<int:id>')
def faculty(id):
    try:
        faculty = models.Faculty.query.filter_by(id=id).first_or_404()
        return render_template('faculty.html', faculty=faculty)
    except OverflowError:
        abort(404)


@app.route('/department/<int:id>')
def department(id):
    try:
        department = models.Department.query.filter_by(id=id).first_or_404()
        return render_template('department.html', department=department)
    except OverflowError:
        abort(404)


@app.route('/profile/<code>')
def staffmember(code):
    try:
        staffmember = models.StaffMember.query.filter_by(code=code).first_or_404()
        return render_template('profile.html', staffmember=staffmember)
    except OverflowError:
        abort(404)


@app.route('/search')
def search():
    staffmembers_f = models.StaffMember.query.order_by(models.StaffMember.name).all()
    staffmembers_l = models.StaffMember.query.order_by(models.StaffMember.lname).all()
    return render_template('search.html', staffmembers_f=staffmembers_f,
                           staffmembers_l=staffmembers_l)


@login_manager.user_loader
def loader_user(user_id):
    return models.Users.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register():
    # If user registers with form
    if request.method == "POST":
        user = models.Users(username=request.form.get("username"),
                            hashed_password=bcrypt.generate_password_hash(
                                request.form.get('password')).decode('utf-8'))
        username_check = models.Users.query.filter_by(
            username=request.form.get("username")).first()
        if username_check is not None:
            flash('This username already exists. Please register with a different username.')
        else:
            db.session.add(user)
            db.session.commit()
            logout_user()
            flash('You have been logged out.')
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If user logs in with form
    if request.method == "POST":
        user = models.Users.query.filter_by(
            username=request.form.get("username")).first()
        password = request.form.get("password")
        error_text = "The username or password entered is incorrect. Please try again."
        if user is None:
            flash(error_text)
        # If password matches for username log user in
        elif bcrypt.check_password_hash(user.hashed_password, password):
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash(error_text)
        # Redirect the user back to the home
    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route('/edit')
def edit():
    return render_template('edit.html')


@app.route("/download")
def download():
    staffmembers = models.StaffMember.query.all()

    # Writes a CSV file from data in database
    buf = StringIO()
    w = csv.writer(buf)
    for staffmember in staffmembers:
        row = [staffmember.code, staffmember.name, staffmember.fname,
               staffmember.lname, staffmember.division_id, staffmember.email,
               staffmember.likely_location]
        w.writerow(row)
    response = make_response(buf.getvalue())
    response.headers.set('Content-Type', 'text/csv')
    response.headers.set('Content-Disposition', 'attachment',
                         filename="photoboard.csv")
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function for adding staff member data from uploaded CSV file to database
def add_staffmember(code, name, fname, lname, division_id, email,
                    likely_location):
    new_staffmember = models.StaffMember()

    new_staffmember.code = code
    new_staffmember.name = name
    new_staffmember.fname = fname
    new_staffmember.lname = lname
    new_staffmember.division_id = division_id
    new_staffmember.email = email
    new_staffmember.likely_location = likely_location

    with app.app_context():
        db.session.merge(new_staffmember)
        db.session.commit()


# This function was partially generated by ChatGPT
@app.route('/upload', methods=["POST"])
def upload():

    if 'csv_file' not in request.files:
        return redirect(request.url)

    file = request.files['csv_file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):

        # The backup code is partially generated by ChatGPT
        # Backs up photoboard.csv into backup.csv
        source_file = 'app/photoboard.csv'
        backup_file = 'backup.csv'
        file_path = path.join(app.config['UPLOAD_FOLDER'], backup_file)
        copy(source_file, file_path)
        flash('CSV file sucessfully backed up')

        # Replaces photoboard.csv with uploaded CSV
        filename = 'photoboard.csv'
        file_path = path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('CSV file successfully uploaded')

        # Read and validate the CSV before making database changes
        valid = True
        staff_members = []  # To store valid rows to add into database

        with open(file_path, newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)

            unique_check = []
            for row in reader:
                # Check if it has the correct number of rows
                if len(row) != 7:
                    valid = False
                    break
                # Check if code is valid and unique
                elif row[0].isalpha() is False or len(row[0]) != 3 or row[0] in unique_check:
                    valid = False
                    break
                # Check if division is valid
                elif row[4] not in ['', '1', '2', '3', '4']:
                    valid = False
                    break
                # Check if email has @ symbol (if it is valid)
                elif '@' not in row[5]:
                    valid = False
                    break
                else:
                    unique_check.append(row[0])
                # Store valid row
                staff_members.append(row)

        if not valid:
            # Revert photoboard.csv with backup.csv
            backup_file = 'app/backup.csv'
            copy(backup_file, file_path)
            flash('CSV file changes undone')
            flash('The CSV file you uploaded is malformed.')
            flash('Please download a new file to make your changes.')
            return redirect(url_for('edit'))

        # If the CSV is valid, delete old data and insert new data
        models.StaffMember.query.delete()
        db.session.commit()
        for row in staff_members:
            add_staffmember(row[0].upper(), row[1], row[2], row[3], row[4],
                            row[5], row[6])

        flash('Database successfully updated')

        return redirect(url_for('edit'))

    flash('Invalid file type')
    return redirect(url_for('edit'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
