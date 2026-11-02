import os

import pytest
from dotenv import load_dotenv
from utils.logger import logger
from clients.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()


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




