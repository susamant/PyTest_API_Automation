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

