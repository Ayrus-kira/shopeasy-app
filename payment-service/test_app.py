import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200

def test_process_payment(client):
    res = client.post('/payment/process',
        json={"user_id": "user1", "amount": 50000})
    assert res.status_code == 200
    assert res.json['status'] == 'success'
    assert 'transaction_id' in res.json
    assert res.json['amount'] == 50000
