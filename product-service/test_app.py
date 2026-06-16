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
    assert res.json['status'] == 'healthy'

def test_get_products(client):
    res = client.get('/products')
    assert res.status_code == 200
    assert len(res.json) == 3

def test_get_single_product(client):
    res = client.get('/products/1')
    assert res.status_code == 200
    assert res.json['name'] == 'Laptop'

def test_product_not_found(client):
    res = client.get('/products/999')
    assert res.status_code == 404
