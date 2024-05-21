from app.routes import db

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

     def __repr__(self):
        return self.name


class Division(db.Model):
     __tablename__ = "Division"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.Text())
     staff_members = db.relationship('StaffMember', backref='Division')


class Position(db.Model):
     __tablename__ = "Position"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.Text())
     staff_member_id = db.Column(db.Integer, db.ForeignKey('StaffMember.code'))


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

     def __repr__(self):
        return self.name


Staff_Department = db.Table('Staff_Department',
    db.Column('scode', db.Text(), db.ForeignKey('StaffMember.code')),
    db.Column('did', db.Integer, db.ForeignKey('Department.id')),
    db.Column('hod', db.Integer)
)
