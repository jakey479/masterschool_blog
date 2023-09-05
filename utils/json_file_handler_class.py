import json
from typing import Union


class JsonFileHandler:

    @staticmethod
    def write_python_object_to_json(json_filepath: str, python_object) -> None:
        with open(json_filepath, 'w') as fileobj:
            json.dump(python_object, fileobj, indent=4)

    @staticmethod
    def return_python_object_from_json(json_filepath: str) -> Union[str, list, dict]:
        with open(json_filepath) as fileobj:
            python_object = json.load(fileobj)
        return python_object
