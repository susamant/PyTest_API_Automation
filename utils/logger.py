import logging
import os

import config

# Create logs directory if it doesn't exist
os.makedirs(config.LOG_DIR, exist_ok=True)

log_file = os.path.join(config.LOG_DIR, config.LOG_FILE_NAME)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')


fileHandler = logging.FileHandler(log_file)
fileHandler.setFormatter(formatter)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# def add(a, b):
#     sum = a + b
#     return sum
#
# if __name__ == '__main__':
#     result = add(10,20)
#     logger.debug(result)