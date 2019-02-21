# from flask import render_template, request, redirect, url_for
# from flask_login import login_required, current_user

# from application import app, db
# from application.auth.models import User
# from application.auth.forms import LoginForm, RegistrationForm, SaldoForm
# from application.purchase.models import Purchase
# from flask_login import login_user, logout_user
# from flask_login import current_user


# @app.route("/purchase/buy", methods = ["GET"])
# def purchase_buy():
#     return render_template("purchase/buyList.html", purchases = Purchase.query.filter_by(buyer_account_id=current_user.id).all())

# @app.route("/purchase/sell", methods = ["GET"])
# def purchase_sell():
#     return render_template("purchase/sellList.html", purchases = Purchase.query.filter_by(seller_account_id=current_user.id).all())
