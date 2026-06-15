from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop",     "price": 50000, "stock": 10},
    {"id": 2, "name": "Phone",      "price": 20000, "stock": 25},
    {"id": 3, "name": "Headphones", "price": 5000,  "stock": 50}
]

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "product-service"})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>')
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    return jsonify(product) if product else (jsonify({"error": "Not found"}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
