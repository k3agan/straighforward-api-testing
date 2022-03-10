import requests
import json

url = "http://www.google.ca"


def test_Test():
    response = requests.get(url)
    assert response.status_code == 200
