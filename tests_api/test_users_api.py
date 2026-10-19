import pytest
import requests
from utils.api_utils import BASE_URL, obtener_headers

@pytest.mark.api
def test_user_api():
    url = f"{BASE_URL}/users"
    response = requests.get(url, headers=obtener_headers())
    assert response.status_code == 200

