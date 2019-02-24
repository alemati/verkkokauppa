from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm, SaldoForm
from flask_login import login_user, logout_user
from flask_login import current_user

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm(), error = None)

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

    
    login_user(user)
    return redirect(url_for("index")) 

@app.route("/auth/regestration", methods = ["GET", "POST"])
def auth_registration():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = RegistrationForm(), error = None)
                                                                    
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form=form, error = None)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        user2 = User(form.name.data, form.username.data, form.password.data)
        db.session().add(user2)
        db.session().commit()
        login_user(user2)
        return redirect(url_for("index")) 
    else: 
        form
        return render_template("auth/registrationform.html", form=form, error = "Haluamasi käyttäjätunnus on jo varattu. Kokeile toisen.")

    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/saldo", methods = ["GET", "POST"])
def auth_saldo():
    if request.method == "GET":
        return render_template("auth/saldoform.html", form = SaldoForm())
  
    # form = SaldoForm(request.form)
    modal =int(request.form.get("sum")) 
    cu = current_user
    user = User.query.filter_by(id=cu.id).first()
    if not user:
        return render_template("auth/saldoform.html", form = form,
                                error = "Sorry, something gone wrong")
    # user.saldo = user.saldo + form.maara.data
    user.saldo = user.saldo + modal
    db.session().commit()
    # return redirect(url_for("auth_saldo"))  
    return redirect(url_for("product_index"))  