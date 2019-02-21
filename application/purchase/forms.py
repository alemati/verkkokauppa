from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators
  
class PurchaseForm(FlaskForm):
    name = StringField("Nimi")
    description = PasswordField("Kuvaus")
    
    class Meta:
        csrf = False

