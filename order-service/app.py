from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
from flask import Flask, jsonify, request
import uuid
from datetime import datetime

app = Flask(__name__)
orders = []

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "order-service"})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = {
        "order_id": str(uuid.uuid4()),
        "user_id": data.get("user_id"),
        "items": data.get("items", []),
        "status": "placed",
        "created_at": datetime.now().isoformat()
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
