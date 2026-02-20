import json
import os

class Storage:
    @staticmethod
    def load(filename):
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save(filename, data):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)