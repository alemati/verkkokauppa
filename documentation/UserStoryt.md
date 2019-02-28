# User storyt  
### Sovellus aina hakee tietokannasta tietoja käyttäen SQLAlchemy-kirjastoa eikä sovelluksessa ole käytössä SQL-kyselyitä. 
### Alla jokaisen user storyn kanssa on annettu SQLAlchemy metodi/koodi, joka joko hakee user storyn toteuttamiseen tarvittava tieto tietokannasta tai muuttaa sen. 

* Käyttäjänä minä voin kirjautua verkokauppaan  
'''  
User.query.filter_by(username=form.username.data, password=form.password.data).first() 
''' 

* Käyttäjänä voin tarkista mitä tuoteita on myynnissä 
'''  
Product.query.filter_by(onSale='1').all()  
'''  

* Käyttäjänä voin osta tuoteen jos minun tilillä on riittävästi rahaa 
'''  
afterPurchase = mySaldo - Product.query.get(product_id).price  
product.account_id = current_user.id  
'''  

* Käyttäjänä voin lisätä omallle tilille rahaa ostoksia varten  
'''  
user.saldo = user.saldo + summa  
'''  

* Käyttäjänä minä voin lisätä oman tuoteen myyntiin tai poista sen myynnistä 
'''  
product = Product.query.get(product_id)
    product.onSale = True/False
'''  

* Käyttäjänä voin tarkista oman ostoshistorian ja myyntihistorian  
'''  
Purchase.query.filter_by(buyer_account_id=current_user.id).all()  
Purchase.query.filter_by(seller_account_id=current_user.id).all()  
'''  

* Käyttäjänä voin muuttaa oman tuoteen tietoja  
'''  
product = Product.query.get(oldId)
    product.name = newName
    product.description = newDescription
    product.price = newPrice
    db.session().commit()
'''  
