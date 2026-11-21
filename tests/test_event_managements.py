import json
import allure
import jsonschema
import pytest
from utils.logger import logger


event_id = None
# @pytest.mark.skip(reason="Skipping event management tests for now")
@allure.testcase("TMS-123")
@allure.severity(allure.severity_level.MINOR)
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

    # except ResponseError as e:
    #     logger.error(f"API response error: {e}")
    #     pytest.fail(f"API response error: {e}")


# @pytest.mark.skip(reason="Skipping pagination tests for now")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.NORMAL)
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

@allure.testcase("TMS-789")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_event(api_client):
    global event_id
    endpoint = '/events'
    payload = {
          "title": "Concert Diljeet",
          "description": "Concert by Diljeet Singh.",
          "category": "Concert",
          "venue": "Vantara Gujrat",
          "city": "Ahmedabad",
          "eventDate": "2026-12-15T09:00:00.000Z",
          "price": 1500,
          "totalSeats": 500,
          "imageUrl": "https://example.com/banner.jpg"
    }
    response = api_client.post(endpoint, data=payload)
    assert response.status_code == 201
    event_id = response.json().get('data').get('id')
    logger.debug(f"Created event with ID: {event_id}")
    logger.debug(f"Response text: {json.loads(response.text)}")
    response_data = response.json()
    assert response_data.get('success') is True
    assert response_data.get('message') == "Event created successfully"

@allure.testcase("TMS-012")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_event_by_id(api_client):
    global event_id
    endpoint = f'/events/{event_id}'
    logger.debug(endpoint)
    response = api_client.get(endpoint)
    logger.debug(f"Response text: {json.loads(response.text)}")
    assert response.status_code == 200
    logger.debug(f"Response text: {json.loads(response.text)}")
    event_data = response.json().get('data')
    assert event_data.get('id') == event_id
    assert event_data.get('title') == "Concert Diljeet"
    assert event_data.get('category') == "Concert"
