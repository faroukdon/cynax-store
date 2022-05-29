from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200))

    price = db.Column(db.DECIMAL(10,2))


    def __init__(self,productName,productPrice):

        self.name = productName
        self.price = productPrice

    def __repr__(self):
        return f"'name':{self.name},'price':{self.price}"
