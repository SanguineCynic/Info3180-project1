from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

from wtforms import ValidationError

class DecimalPlaces:
    """
    Validator that checks that a field value has at most `places` decimal places.
    """
    def __init__(self, places, message=None):
        self.places = places
        self.message = message

    def __call__(self, form, field):
        if field.data is not None and round(field.data, self.places) != field.data:
            if self.message is None:
                message = f'Must be a number with at most {self.places} decimal places.'
            else:
                message = self.message
            raise ValidationError(message)


class PropertyForm(FlaskForm):
    title = StringField('Property Name', validators=[InputRequired()])
    num_bedrooms = IntegerField(validators =[InputRequired()])
    num_bathrooms = IntegerField(validators =[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    type = SelectField('Type',choices=['Apartment','House'])
    price = FloatField('Nightly Cost (USD)',validators=[InputRequired(), DecimalPlaces(2, message="Must be a number with 2 decimal places.")])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Picture', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'jfif', 'webp'])])
    submit = SubmitField('Add Property', validators=[InputRequired()])