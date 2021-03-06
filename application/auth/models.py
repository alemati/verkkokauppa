from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    saldo = db.Column(db.Integer, nullable=False)

    products = db.relationship("Product", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.saldo = 0
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def get_saldo(self):
        return self.saldo

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    
