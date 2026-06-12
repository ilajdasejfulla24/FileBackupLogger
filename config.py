import json
import os


class ConfigManager:

    CONFIG_FILE = "config.json"

    DEFAULT_CONFIG = {
        "source_folder": "",
        "destination_folder": "",
        "zip_enabled": True
    }

    @classmethod
    def load(cls):

        if not os.path.exists(cls.CONFIG_FILE):
            cls.save(cls.DEFAULT_CONFIG)

        with open(cls.CONFIG_FILE, "r") as file:
            return json.load(file)

    @classmethod
    def save(cls, config):

        with open(cls.CONFIG_FILE, "w") as file:
            json.dump(
                config,
                file,
                indent=4
            )
