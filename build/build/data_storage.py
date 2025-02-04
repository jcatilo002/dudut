import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            if "exercise" not in data:
                data["exercise"] = {}
            return data
    return {"water_intake": {}, "steps": {}, "exercise": {}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

data_storage = load_data()
