## Jos haluat käynistä sovelluksen paikallisella koneella, toimi näin:  

1. kloonaa lähdetiedostot  tietokonelle
```git
git clone git@github.com:alemati/verkkokauppa.git
```
2. siirry kloonatun repositorion hakemistoon
```git
cd verkkokauppa
```
3. luo hakemistoon Python-virtuaaliympäristö
```
python3 -m venv venv
```
4. käynnistä virtuaaliympäristö
```
source venv/bin/activate
```
4. lataa seuraavat riippuvuudet  
```
pip install flask
```
```
pip install flask-sqlalchemy
```
```
pip install flask-wtf
```
```
pip install flask_login
```
5. käynnistä sovellus  
```
source venv/bin/activate
```
6. käynnistyksen jälkeen voit käyttää sovellusta osoitteessa http://localhost:5000/  

7. voit sammuttaa soveluksen painamalla ctrl+C
