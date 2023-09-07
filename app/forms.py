from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired


#example form - feel free to try
class queryForm(FlaskForm):
    query = StringField('query', validators=[DataRequired()])