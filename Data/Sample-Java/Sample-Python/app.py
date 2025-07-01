from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

@app.route("/items", methods=["GET"])
def get_items():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)

@app.route("/add", methods=["POST"])
def add_item():
    item = request.json["item"]
    # logic to add item to DB
    return jsonify({"status": "added", "item": item})

@app.route("/price", methods=["GET"])
def get_price():
    item = request.args.get("item")
    response = requests.get("https://api.pricing-service.com/getPrice", params={"item": item})
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
