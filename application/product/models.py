from application import db
from sqlalchemy.sql import text

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(2000), nullable=False)
    onSale = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, price, description, onSale, account_id):
        self.name = name
        self.price = price
        self.description = description
        self.onSale = onSale
        self.account_id = account_id
        

    # @staticmethod
    # def find_all_products_on_sale():
    #     stmt = text("SELECT Product.id, Product.name, Product.onSale FROM Product WHERE Product.onSale = 'True'")
    #     res = db.engine.execute(stmt)
  
    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "name":row[1]})

    #     return response
