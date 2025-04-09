from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class UserForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=2, max=50)])
    city = StringField("Город", validators=[DataRequired(), Length(max=100)])
    hobby = StringField("Хобби", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired(), NumberRange(min=0, max=115)])
    submit = SubmitField("Отправить")
