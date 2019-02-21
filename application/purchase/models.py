from application import db
from sqlalchemy.sql import text

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(2000), nullable=False)
    seller_account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    buyer_account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, price, description, seller_account_id, buyer_account_id):
        self.name = name
        self.price = price
        self.description = description
        self.seller_account_id = seller_account_id
        self.buyer_account_id = buyer_account_id