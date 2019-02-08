from flask import render_template
from application import app
from application.product.models import Product

@app.route("/")
def index():
    return render_template("index.html")
