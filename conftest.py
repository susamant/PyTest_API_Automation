import json
import os

import pytest
import requests
from dotenv import load_dotenv
from utils.logger import logger
from clients.api_client import APIClient


"""
# Write a fixture to fetch all environment specific config data


@pytest.fixture(scope="session")
def env_config():
    load_dotenv()
    env = os.getenv('TEST_ENV')
    config_path = os.path.join("config", f"{env}.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file for {env} doesn't exist")
    with open(config_path, "r+") as f:
        config_data = json.load(f)

    return config_data
"""

"""
# Code to fetch config data through a secure scoped Factory method

_INTERNAL_SECRET = "CONFTEST_INTERNAL_SECRET_2026"

class RestrictedConfigData:
    def __init__(self, data):
        self._data = data

    def get_data(self, access_token):
        if access_token != _INTERNAL_SECRET:
            raise PermissionError("Invalid access token")
        return self._data

@pytest.fixture(scope="session")
def secure_config_data():
    test_env = os.getenv('TEST_ENV')
    if test_env:
        path = "Config/" + test_env + ".json"
        with open(path) as f:
            data = json.load(f)
    logger.debug("data: {}".format(data))
    return RestrictedConfigData(data)

@pytest.fixture(scope="session")
def get_config_data(secure_config_data):
    config = secure_config_data.get_data(_INTERNAL_SECRET)
    return config
"""

@pytest.fixture(scope="session")
def user_credentials():
    load_dotenv()
    email = os.getenv('user_email')
    password = os.getenv('user_password')
    # logger.debug("email:{}".format(email))
    # logger.debug("password:{}".format(password))
    if not email or not password:
        logger.error("email or password not provided")

    return {"email": email, "password": password}

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    return client






