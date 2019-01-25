from flask import render_template, request, redirect, url_for

from application import app, db
from flask import render_template, request
from application.product.models import Product

@app.route("/product", methods=["GET"])
def product_index():
    return render_template("product/list.html", products = Product.query.all())

@app.route("/product/new/")
def product_form():
    return render_template("product/new.html")

@app.route("/product/", methods=["POST"])
def product_create():
    t = Product(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("product_index"))

@app.route("/product/<product_id>/", methods=["POST"])
def product_set_done(product_id):

    t = Product.query.get(product_id)
    t.onSale = True
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/<product_id>/delete", methods=["POST"])
def product_delete(product_id):

    t = Product.query.get(product_id)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("product_index"))





