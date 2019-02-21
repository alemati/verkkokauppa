from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [validators.Length(min=4, max=144)])

    class Meta:
        csrf = False

class SaldoForm(FlaskForm):
    maara = IntegerField("Maara", [validators.NumberRange(min=0, max=1000)])

    class Meta: 
        csrf = False
