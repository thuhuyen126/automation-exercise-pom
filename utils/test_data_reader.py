import json
from pathlib import Path


class TestDataReader:
    __test__ = False

    def __init__(self):
        data_path = Path(__file__).parent.parent / "data" / "test_data.json"

        with open(data_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def get_user(self, user_type="valid_user"):
        return self.data[user_type]