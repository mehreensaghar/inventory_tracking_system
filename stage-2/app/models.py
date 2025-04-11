from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class StockMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    type = db.Column(db.String) 
    timestamp = db.Column(db.DateTime)
