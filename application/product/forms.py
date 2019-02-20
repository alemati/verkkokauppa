from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, TextAreaField, IntegerField

class ProductForm(FlaskForm):
    name = StringField("Tuotteen nimi", [validators.Length(min=2)])
    description = TextAreaField("Kuvaus", [validators.length(max=2000)])
    price = IntegerField("Hinta", [validators.NumberRange(min=0, max=1000)])
    onSale = BooleanField("Heti myyntiin")
    
 
    class Meta:

        csrf = False
