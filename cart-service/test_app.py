import pytest
from app import app, cart

@pytest.fixture
def client():
    app.config['TESTING'] = True
    cart.clear()
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200

def test_empty_cart(client):
    res = client.get('/cart/user1')
    assert res.json == []

def test_add_to_cart(client):
    res = client.post('/cart/user1/add',
        json={"product_id": 1, "name": "Laptop", "price": 50000})
    assert res.status_code == 200
    assert res.json['message'] == 'Item added'

def test_clear_cart(client):
    client.post('/cart/user1/add', json={"product_id": 1})
    res = client.delete('/cart/user1/remove')
    assert res.json['message'] == 'Cart cleared'
