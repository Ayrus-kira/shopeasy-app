from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
from flask import Flask, jsonify, request

app = Flask(__name__)
cart = {}

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "cart-service"})

@app.route('/cart/<user_id>', methods=['GET'])
def get_cart(user_id):
    return jsonify(cart.get(user_id, []))

@app.route('/cart/<user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    item = request.json
    cart.setdefault(user_id, []).append(item)
    return jsonify({"message": "Item added", "cart": cart[user_id]})

@app.route('/cart/<user_id>/remove', methods=['DELETE'])
def clear_cart(user_id):
    cart.pop(user_id, None)
    return jsonify({"message": "Cart cleared"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
