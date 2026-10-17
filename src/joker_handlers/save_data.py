import json


def save_data(file_path: str, joker_dict: dict):
    with open(file_path, "w+") as file:
        json.dump(joker_dict, file, indent=4)
