from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional, ValidationError
import app.models
# from datetime import datetime


# class Add_Movie(FlaskForm):
  
#   def check_year(form, field):
#     _current_year = int(datetime.now().year)
#     if field.data > _current_year:
#       raise ValidationError("You can't enter a movie from the future!")

#   title = StringField('title', validators=[DataRequired()])
#   year = IntegerField('year', validators=[Optional(), check_year])
#   description = TextAreaField('description')
  
  

class Select_Movie(FlaskForm):
  moviename = SelectField('moviename', validators=[DataRequired()], coerce=int)

