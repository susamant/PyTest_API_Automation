
from utils.logger import logger



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













