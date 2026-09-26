import pytest
import requests
import config


class APIClient:
    def __init__(self):
        self.BASEURL = config.BASE_URL

    def get(self, endpoint, params = None):
        url = self.BASEURL + endpoint
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, data=None):
        url = self.BASEURL + endpoint
        response = requests.post(url, json=data)
        return response

if __name__ == "__main__":

    client = APIClient()
    body = {

    }

