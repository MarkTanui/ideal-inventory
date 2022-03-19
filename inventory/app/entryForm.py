from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    crates = IntegerField('Crates', validators=[DataRequired()])
    date_in = DateField('Date Added', validators=[DataRequired()])
    date_out = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')
