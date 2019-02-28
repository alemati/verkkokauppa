  
<img src="https://github.com/alemati/verkkokauppa/blob/master/documentation/databaseLast.png" width="300"> 

Kaavio oli tehty sivulla https://yuml.me/ (alla on koodi)  
[Customer|(pk) id : Integer; username : varchar(20); password: varchar(20); saldo : Integer], 
[Product|(pk) id : Integer; (fk) seller_id: Customer; name:varchar(144);description: varchar(3000); price: Integer; onSale: Boolean], 
[Purchase|(pk) id : Integer; (fk) buyer_id: Customer;(fk) seller_id: Customer; date: Date; description: varchar(2000); price: Integer; name: varchar(144)], 

[Customer]1-*[Product], 
[Purchase]*-1[Product],
[Customer]2-1[Purchase],   
