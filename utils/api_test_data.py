import json


def load_api_users():

    file_path = "tests/data/api_users.json"

    with open(
        file_path,
        encoding="utf-8"
    ) as file:

        return json.load(file)