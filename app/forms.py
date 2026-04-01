from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class PropertyForm(FlaskForm):
    title         = StringField('Property Title', validators=[DataRequired()])
    description   = TextAreaField('Description', validators=[DataRequired()])
    bedrooms      = IntegerField('No. of Rooms', validators=[DataRequired(), NumberRange(min=1)])
    bathrooms     = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    price         = DecimalField('Price', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location      = StringField('Location', validators=[DataRequired()])
    photo         = FileField('Photo', validators=[
                        FileRequired(),
                        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
                    ])