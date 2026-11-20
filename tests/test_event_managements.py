import json
import jsonschema
import pytest
from utils.logger import logger

def test_list_all_events(api_client):
    endpoint = '/events'
    params = {
        "Category": "Conference",
        "City": "Bangalore",
        "Search": "Summit"
    }
    try:
        response = api_client.get(endpoint, params= params)
        assert response.status_code == 200
        logger.debug(f"Response text: {json.loads(response.text)}")
        with open('./data/list_events_schema.json') as json_file:
            schema = json.load(json_file)
        jsonschema.validate(instance = json.loads(response.text), schema = schema)

    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"JSON schema validation error: {e}")
        pytest.fail(f"JSON schema validation failed: {e}")

    except ResponseError as e:
        logger.error(f"API response error: {e}")
        pytest.fail(f"API response error: {e}")


def test_pagination_events(api_client):
    endpoint = '/events'
    params = {
        "Category": "Conference",
        "City": "Bangalore",
        "Search": "Summit"
    }
    response = api_client.get(endpoint, params = params)
    assert response.status_code == 200
    events = response.json().get('data')
    pagination_info = response.json().get('pagination')
    logger.debug(f"Events: {events}")
    logger.debug(f"Pagination Info: {pagination_info}")
    assert len(events) == pagination_info.get('total')
    events_ids = [event['id'] for event in events]
    logger.debug(f"List of events ids: {events_ids}")
    assert len(events_ids) == len(set(events_ids))

