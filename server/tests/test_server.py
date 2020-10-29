import sys
sys.path.insert(0, "./helpers/")

import pytest
from ..app import create_app

@pytest.fixture
def app():
  app = create_app()
  yield app

@pytest.fixture
def client(app):
  return app.test_client()

def test_home(client):
  assert client.get('/').status_code == 200

def test_generate_get(client):
  # response = client.get('/generate', data={"url": "www.facebook.com", "bgColor": "#FFFFFF", "codeColor": "#000000"})
  assert client.get('/generate').status_code == 405

def test_generate_post(client):
  msg = "QRcode generated!"
  errorStatus = False

  response = client.post('/generate', json={"url": "www.facebook.com", "bgColor": "#FFFFFF", "codeColor": "#000000"})

  assert response.data
