import sys
from flask import  request ,json
from models.Product import Product
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def index():
    products=Product.query.all()
    return repr(products)


def store():
    if request.method == 'GET':
        return('method not allowed')
    if request.method == 'POST':
        product_name = request.args.get('productName')
        product_price = request.args.get('productPrice')
        product = Product(productName=product_name, productPrice=product_price)
        db.session.add(product)
        db.session.commit()
        return ("Product creates success")



def show(product_id):
    product=Product.query.filter_by(id=product_id).first()
    if product:
         return repr(product)
    return f"productwith id ={product_id} Doenst exist"


def update(product_id):

    product_name=request.args.get('productName')

    product_price=request.args.get('productPrice')

    productedited=db.session.query(Product).filter_by(id=product_id).first()

    productedited.name=product_name

    productedited.price=product_price

    db.session.commit()

    return ("Product updated  succefully")

def delete(product_id):
    
    product=db.session.query(Product).filter_by(id=product_id).delete()    
    if product:
        db.session.commit()
        return "product deleted succesfully"
    return f"productwith id ={product_id} Doenst exist"


