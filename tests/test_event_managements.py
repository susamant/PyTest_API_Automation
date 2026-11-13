import json

import pytest
from utils.logger import logger

def test_list_all_events(api_client):
    endpoint = '/events'
    params = {
        "Category": "Conference",
        "City": "Bangalore",
        "Search": "Summit"
    }
    response = api_client.get(endpoint, params= params)
    assert response.status_code == 200
    logger.debug(f"Response text: {json.loads(response.text)}")
