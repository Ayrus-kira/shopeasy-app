from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "payment-service"})

@app.route('/payment/process', methods=['POST'])
def process_payment():
    data = request.json
    transaction_id = str(uuid.uuid4())
    return jsonify({
        "status": "success",
        "transaction_id": transaction_id,
        "amount": data.get("amount"),
        "user_id": data.get("user_id")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
