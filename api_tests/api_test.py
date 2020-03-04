import pytest
import requests

from project import api_URL, data


@pytest.mark.apitests
def test_get():
    response = requests.get(api_URL)
    assert response.status_code == 200
    resp_data = response.json()
    assert resp_data.keys() == data.keys()
    assert resp_data["method"] == "GET"
    assert resp_data["url"] == "https://httpbin.org/anything"


@pytest.mark.apitests
def test_post():
    data = {"key": "value"}
    response = requests.post(api_URL, json=data)
    assert response.status_code == 200
    resp_data = response.json()
    assert resp_data["method"] == "POST"
    assert resp_data["url"] == "https://httpbin.org/anything"
    assert resp_data["data"] == "{\"key\": \"value\"}"
    assert resp_data["headers"]["Content-Length"] == "16"
    assert resp_data["headers"]["Content-Type"] == "application/json"

