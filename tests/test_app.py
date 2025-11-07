import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_pedido_valido(client):
    response = client.post('/', data={'pedido_id': '12345'}, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Status do Pedido 12345: Em processamento' in response.data

def test_pedido_invalido(client):
    response = client.post('/', data={'pedido_id': 'ID_FALSO'}, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Pedido ID_FALSO nao encontrado.' in response.data