import os

import requests
from utils.config_manager import ConfigManager
from utils.logger import logger
from dotenv import load_dotenv


class APIClient:
    load_dotenv()
    def __init__(self, token=None):
        config = ConfigManager.load_config()
        self.BASEURL = config["BASE_URL"]
        self.token = token

    def auth_token(self):
        if self.token is None:
            endpoint = "/auth/register"
            url = self.BASEURL + endpoint
            data = {
                "email": os.getenv('user_email'),
                "password": os.getenv('user_password')
            }
            response = requests.post(url, data=data)
            logger.debug(f"Response data : {response.text}")
            self.token = response.json()['token']
        return self.token


    def _get_headers(self, headers):
        # if headers is None:
        #     return None
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token()}"
        }
        logger.debug(f"Headers: {self.headers}")
        return self.headers

    def get(self, endpoint, headers = None, params = None):
        url = self.BASEURL + endpoint
        response = requests.get(url, headers=self._get_headers(headers), params=params)
        return response

    def post(self, endpoint, data=None):
        url = self.BASEURL + endpoint
        response = requests.post(url, json=data)
        return response

    def put(self, endpoint, data = None):
        url = self.BASEURL + endpoint
        response = requests.put(url=url, json = data)
        return response

    def delete(self, endpoint):
        url = self.BASEURL + endpoint
        response = requests.delete(url=url)
        return response


if __name__ == "__main__":

    client = APIClient()
    body = {

    }

