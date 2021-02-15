import os
import requests

def test_blueprint_x_test(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'blueprint_x', 'test')
    response = requests.get(endpoint)
    json = response.json()

    assert response.status_code == 200
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from blueprint_x."

def test_blueprint_y_test(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'blueprint_y', 'test')
    response = requests.get(endpoint)
    json = response.json()

    assert response.status_code == 200
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from blueprint_y."

def test_blueprint_x_plus(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'blueprint_x', 'plus')
    payload = {'number': 5}
    response = requests.post(endpoint, json=payload)
    json = response.json()

    assert response.status_code == 200
    assert 'msg' in json
    assert json['msg'] == "Your result is: '10'"

def test_blueprint_x_minus(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'blueprint_y', 'plus')
    payload = {'number': 1000}
    response = requests.post(endpoint, json=payload)
    json = response.json()
    
    assert response.status_code == 200
    assert 'msg' in json
    assert json['msg'] == "Your result is: '1100'"
