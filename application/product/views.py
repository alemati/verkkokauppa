
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
    return render_template("product/list.html", products = Product.query.filter_by(onSale='1').all(), viestiEi = None, viestiKyl = None)

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

    newProduct = Product(form.name.data, form.price.data, form.description.data, form.onSale.data, current_user.id)
    
    db.session().add(newProduct)
    db.session().commit()
  
    return redirect(url_for("product_userstorage"))

@app.route("/product/userstorage", methods=["GET"])
@login_required
def product_userstorage():
    
    return render_template("product/storage.html", form = ProductForm(), products = Product.query.filter_by(account_id=current_user.id).all(), 
                           viesti = None)


@app.route("/product/<product_id>/setonsale/", methods=["POST"])
@login_required
def product_set_onSale(product_id):

    product = Product.query.get(product_id)
    product.onSale = True
    db.session().commit()
    return redirect(url_for("product_userstorage"))

@app.route("/product/<product_id>/setoffsale/", methods=["POST"])
@login_required 
def product_set_offSale(product_id):

    product = Product.query.get(product_id)
    product.onSale = False
    db.session().commit()
    return redirect(url_for("product_userstorage"))

@app.route("/product/<product_id>/delete", methods=["POST"])
@login_required
def product_delete(product_id):

    product = Product.query.get(product_id)
    db.session().delete(product)
    db.session().commit()
    return redirect(url_for("product_userstorage"))

@app.route("/product/<product_id>/buy", methods=["POST"])
@login_required
def product_buy(product_id):
    saldo = current_user.saldo
    afterPurchase = saldo - Product.query.get(product_id).price
    if afterPurchase >= 0:
        product = Product.query.get(product_id)
        purchase = Purchase(product.name, product.price, product.description, product.account_id, current_user.id)
        db.session().add(purchase)
        db.session().commit()

        productPrice = Product.query.get(product_id).price
        myyja = User.query.get(product.account_id)
        myyja.saldo = myyja.saldo + productPrice

        current_user.saldo = afterPurchase

        product.account_id = current_user.id
        product.price = 0
        product.onSale = False
        
        db.session().commit()
        return render_template("product/list.html", form = ProductForm(), products = Product.query.filter_by(onSale='1').all(), 
                                viestiKyl = "Tuote on ostettu ja lisätty sinun varastoon" , viestiEi = None) 
    else:
        return render_template("product/list.html", products = Product.query.filter_by(onSale='1').all(),
                                viestiEi = "Tililläsi ei ole riittävästi rahaa", viestiKyl = None)


@app.route("/product/change", methods=["GET", "POST"])
@login_required
def product_change():
    if request.method == "GET":
        return render_template("product/change.html", form = ProductForm(), product = Product.query.get(product_id))
    
    newName = request.form.get("nimi")
    newDescription = request.form.get("kuvaus")
    newPrice = request.form.get("hinta")
    oldId = request.form.get("productid")
    
    product = Product.query.get(oldId)
    product.name = newName
    product.description = newDescription
    product.price = newPrice
    db.session().commit()
    return redirect(url_for("product_userstorage"))
