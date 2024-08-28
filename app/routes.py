from app import app
from flask import render_template, abort, redirect, request, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt
import os
import csv
import io

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config[
    'SQLALCHEMY_DATABASE_URI'
    ] = 'sqlite:///' + os.path.join(basedir, 'photoboard.db')
db.init_app(app)
app.secret_key = 'correcthorsebatterystaple'

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

# Define the directory where you want to save the uploaded files
UPLOAD_FOLDER = 'app'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import app.models as models
from app.forms import Select_StaffMember


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


@login_manager.user_loader
def loader_user(user_id):
    return models.Users.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register():
    # If the user made a POST request, create a new user
    if request.method == "POST":
        user = models.Users(username=request.form.get("username"),
                            hashed_password=bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8'))
        username_check = models.Users.query.filter_by(username=request.form.get("username")).first()
        if username_check is not None:
            flash('This username already exists. Please register with a different username.')
        else:
            # Add the user to the database
            db.session.add(user)
            # Commit the changes made
            db.session.commit()
            # Once user account created, redirect them
            # to login route (created later on)
            return redirect(url_for("login"))
    # Renders sign_up template if user made a GET request
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = models.Users.query.filter_by(
            username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        password = request.form.get("password")
        error_text = "The username or password entered is incorrect. Please try again."
        if user is None:
            flash(error_text)
        elif bcrypt.check_password_hash(user.hashed_password, password):
            # Use the login_user method to log in the user
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
    """Exports all the parts as a csv file"""
    # TODO: This should only be admin
    # TODO: Export all fields
    staffmembers = models.StaffMember.query.all()

    buf = io.StringIO()
    w = csv.writer(buf)
    # w.writerow(["name"])
    for staffmember in staffmembers:
        row = [staffmember.code, staffmember.name, staffmember.fname, staffmember.lname, staffmember.photo, staffmember.division_id, staffmember.email, staffmember.likely_location]
        w.writerow(row)
    response = make_response(buf.getvalue())
    response.headers.set('Content-Type', 'text/csv')
    response.headers.set('Content-Disposition', 'attachment', filename="photoboard.csv")
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_from_csv(filename):
    print("Deleting all data in StaffMember table")
    models.StaffMember.query.delete()
    db.session.commit()
    print("Adding new data")
    with open(filename, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            add_staffmember(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        print("DONE")


def add_staffmember(code, name, fname, lname, photo, division_id, email, likely_location):
    new_staffmember = models.StaffMember()

    new_staffmember.code = code
    new_staffmember.name = name
    new_staffmember.fname = fname
    new_staffmember.lname = lname
    new_staffmember.photo = photo
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
        filename = 'photoboard.csv'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Save the new file, overwriting the existing one
        file.save(file_path)
        flash('CSV file successfully uploaded')
        load_from_csv("app/photoboard.csv")
        flash('Database successfully updated')
        return redirect(url_for('edit'))
    flash('Invalid file type')
    return redirect(url_for('edit'))


# handles 404 error by showing 404.html to user
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# handles 404 error by showing 405.html to user
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405


# handles 500 error by showing 500.html to user
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    # if not os.path.exists(UPLOAD_FOLDER):
    # os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
