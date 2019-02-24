
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for
from application.auth.models import User
from application import app, db
from flask import render_template, request
from application.product.models import Product
from application.purchase.models import Purchase
from application.product.forms import ProductForm
from application.auth.forms import LoginForm

@app.route("/product", methods=["GET"])
def product_index(): 
    return render_template("product/list.html", products = Product.query.filter_by(onSale='1').all(), error = None)

@app.route("/product/purchasable", methods=["GET"])
@login_required
def product_purchasable():
    
    return render_template("product/list.html", form = ProductForm(), 
                                products = Product.query.all())

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

    p = Product(form.name.data, form.price.data, form.description.data, form.onSale.data, current_user.id)
    
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("product_index"))

@app.route("/product/userstorage", methods=["GET"])
@login_required
def product_userstorage():
    
    return render_template("product/storage.html", form = ProductForm(), products = Product.query.filter_by(account_id=current_user.id).all(), 
                           viesti = None)


@app.route("/product/<product_id>/setonsale/", methods=["POST"])
@login_required
def product_set_onSale(product_id):

    t = Product.query.get(product_id)
    t.onSale = True
    db.session().commit()
    return redirect(url_for("product_userstorage"))

@app.route("/product/<product_id>/setoffsale/", methods=["POST"])
@login_required 
def product_set_offSale(product_id):

    t = Product.query.get(product_id)
    t.onSale = False
    db.session().commit()
    return redirect(url_for("product_userstorage"))

@app.route("/product/<product_id>/delete", methods=["POST"])
@login_required
def product_delete(product_id):

    t = Product.query.get(product_id)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/<product_id>/buy", methods=["POST"])
@login_required
def product_buy(product_id):
  
    saldo = current_user.saldo
    after = saldo - Product.query.get(product_id).price
    if after >= 0:
        t = Product.query.get(product_id)
        p = Purchase(t.name, t.price, t.description, t.account_id, current_user.id)
        db.session().add(p)
        db.session().commit()
        lisa = Product.query.get(product_id).price
        myyja = User.query.get(t.account_id)
        myyja.saldo = myyja.saldo + lisa
        t.account_id = current_user.id
        t.price = 0
        t.onSale = False
        current_user.saldo = after
        db.session().commit()
        # return redirect(url_for("product_userstorage"))
        return render_template("product/storage.html", form = ProductForm(), products = Product.query.filter_by(account_id=current_user.id).all(), 
                                viesti = "Osto onnistui") 
    else:
        # return redirect(url_for("product_index"))
        return render_template("product/list.html", products = Product.query.filter_by(onSale='1').all(),
                                error = "Tililläsi ei ole riittävästi rahaa")


@app.route("/product/<product_id>/change", methods=["GET", "POST"])
@login_required
def product_change(product_id):
    if request.method == "GET":
        return render_template("product/saldoform.html", form = ProductForm(), product = Product.query.get(product_id))


@app.route("/product/buylist", methods = ["GET"])
def product_buylist():
    return render_template("purchase/buyList.html", purchases = Purchase.query.filter_by(buyer_account_id=current_user.id).all())

@app.route("/purchase/sell", methods = ["GET"])
def product_selllist():
    return render_template("purchase/sellList.html", purchases = Purchase.query.filter_by(seller_account_id=current_user.id).all())