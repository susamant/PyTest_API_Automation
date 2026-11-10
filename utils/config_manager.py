import json
import os


class ConfigManager:

    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is not None:
            return cls._config

        env = os.getenv("TEST_ENV", "qa")
        config_path = os.path.join("config", f"{env}.json")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file for {env} doesn't exist")
        with open(config_path, "r+") as f:
            cls._config = json.load(f)

        return cls._config
