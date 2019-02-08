from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2)])
    sale = BooleanField("Heti myyntiin")
 
    class Meta:

        csrf = False
