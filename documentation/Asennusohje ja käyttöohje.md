# Asennusohje   
#### Paikallinen kehitysympäristö:  

1. kloonaa lähdetiedostot  tietokonelle
```
git clone git@github.com:alemati/verkkokauppa.git
```
2. siirry kloonatun repositorion hakemistoon
```
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
4. lataa projektin riippuvuudet  
```
pip install -r requirements.txt
```
5. käynnistä sovellus  
```
python3 run.py
```
6. käynnistyksen jälkeen voit käyttää sovellusta osoitteessa http://localhost:5000/  

7. voit sammuttaa soveluksen painamalla ctrl+C 

#### Tuotantoympäristö:  
1. kloonaa lähdetiedostot  tietokonelle
```
git clone git@github.com:alemati/verkkokauppa.git
```
2. siirry kloonatun repositorion hakemistoon
```
cd verkkokauppa
```
3. luo sovellukselle paikka Herokussa 
```
heroku create my-app-name
```
4. luo HEROKU-ympäristömuuttuja
```
heroku config:set HEROKU=1
```
5. ota käyttöön PostgreSQL-tietokanta.
```
heroku addons:add heroku-postgresql:hobby-dev
```
6. lähetä sovellus Herokuun
```
git remote add heroku https://git.heroku.com/my-app-name.git
git push heroku master
```
Pääset nyt käyttämään sovellusta osoiteessa https://my-app-name.herokuapp.com/



















