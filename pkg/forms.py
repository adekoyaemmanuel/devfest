from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#file
from flask_wtf.file import FileField, FileAllowed, FileRequired

class BreakoutForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    # level=StringField('Level', validators=[DataRequired()])
    image=FileField(validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],"We only allowed images")])
    # status=BooleanField('Status', validators=[DataRequired()])
    submit=SubmitField('Add Topic!')