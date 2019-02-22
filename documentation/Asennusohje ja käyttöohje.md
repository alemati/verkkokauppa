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
5. käynnistä sovellus
```
python3 run.py
```
