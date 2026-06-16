import pytest
from app import app, orders

@pytest.fixture
def client():
    app.config['TESTING'] = True
    orders.clear()
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200

def test_get_empty_orders(client):
    res = client.get('/orders')
    assert res.json == []

def test_create_order(client):
    res = client.post('/orders',
        json={"user_id": "user1", "items": [{"product_id": 1}]})
    assert res.status_code == 201
    assert 'order_id' in res.json
    assert res.json['status'] == 'placed'

def test_get_orders_after_create(client):
    client.post('/orders', json={"user_id": "user1", "items": []})
    res = client.get('/orders')
    assert len(res.json) == 1
