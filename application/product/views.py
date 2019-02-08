from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from flask import render_template, request
from application.product.models import Product
from application.product.forms import ProductForm
from application.auth.forms import LoginForm

@app.route("/product", methods=["GET"])
def product_index():
    return render_template("product/list.html", products = Product.query.all())

@app.route("/product/new/")
@login_required
def product_form():
    return render_template("product/new.html", form = ProductForm())

@app.route("/product/", methods=["POST"])
@login_required
def product_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("product/new.html", form = form)

    p = Product(form.name.data)
    p.onSale = form.sale.data
    p.account_id = current_user.id
  
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("product_index"))

@app.route("/product/<product_id>/", methods=["POST"])
@login_required
def product_set_done(product_id):

    t = Product.query.get(product_id)
    t.onSale = True
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/<product_id>/delete", methods=["POST"])
@login_required
def product_delete(product_id):

    t = Product.query.get(product_id)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("product_index"))





