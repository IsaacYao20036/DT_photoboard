from app.routes import db

Staff_Department = db.Table(
    'Staff_Department',
    db.Column('scode', db.Text(), db.ForeignKey('StaffMember.code')),
    db.Column('did', db.Integer, db.ForeignKey('Department.id'))
)


class StaffMember(db.Model):
    __tablename__ = "StaffMember"
    code = db.Column(db.Text(), primary_key=True)
    name = db.Column(db.Text())
    photo = db.Column(db.Text())
    division_id = db.Column(db.Integer, db.ForeignKey('Division.id'))
    email = db.Column(db.Text())
    likely_location = db.Column(db.Text())
    positions = db.relationship('Position', backref='staff_member')
    hofs = db.relationship('Faculty', backref='hof')
    hods = db.relationship('Department', backref='hod')
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
    staff_member_code = db.Column(db.Integer,
                                  db.ForeignKey('StaffMember.code'))

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
