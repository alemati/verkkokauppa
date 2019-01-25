Huom! alla oleva kuva on vain tietokantakaavion haahmotelma eikä ole lopullinen ratkaisu jota käytetään sovelluksessa.    
  
<img src="https://github.com/alemati/verkkokauppa/documentation/tietokantakaavio.png" width="500"> 

Kaavio oli tehty sivulla https://yuml.me/ (alla on koodi)  
[Customer|(pk) id : Integer; username : varchar(20); password: varchar(20); wallet : Integer],   
[Product|(pk) id : Integer; (fk) seller_id: Customer; description: varchar(3000); price: Integer;],   
[Purchase|(pk) id : Integer; (fk) Product_id:Product; (fk) buyer_id: Customer; date: Date],  
[Customer]1-*[Product],  
[Purchase]*-1[Product],  
