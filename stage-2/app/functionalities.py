from flask import Flask, request, jsonify
from .models import db, Store, Product, StockMovement

app = Flask(__name__)

@app.route('/stock/in', methods=['POST'])
def stock_in():
    #adding to stock
    return jsonify({"message": "Stock added"}), 201

@app.route('/stock/out', methods=['POST'])
def stock_out():
    #removing from stock
    return jsonify({"message": "Stock removed"}), 200

@app.route('/inventory/<int:store_id>', methods=['GET'])
def get_inventory(store_id):
    # fetching the inventory
    return jsonify({"store_id": store_id, "inventory": []})
