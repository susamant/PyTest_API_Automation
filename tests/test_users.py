import pytest

from utils.logger import logger

test_data = {}

@pytest.mark.skip
def test_register_user(api_client, user_credentials):
    data = {
        "email": user_credentials["email"],
        "password": user_credentials["password"]
    }
    endpoint = "/auth/register"
    response = api_client.post(endpoint, data=data)
    assert response.status_code == 201
    assert response.json().get('user').get('email') == user_credentials["email"]
    # logger.debug(response.json().get('user').get('email'))

def test_login(api_client, user_credentials):
    data = {
        "email": user_credentials["email"],
        "password": user_credentials["password"]
    }

    endpoint = "/auth/login"
    response = api_client.post(endpoint, data=data)
    logger.debug(response.json())
    assert response.status_code == 200
    assert response.json().get('user').get('email') == user_credentials["email"]
    test_data["token"] = response.json().get('token')
    logger.debug(test_data["token"])


def test_authenticate_user(api_client, user_credentials):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Authorization": f"Bearer {test_data['token']}"
               }
    endpoint = "/auth/me"
    response = api_client.get(endpoint, headers=headers)
    logger.debug(response.json())
    assert response.status_code == 200
    assert response.json().get('user').get('email') == user_credentials["email"]