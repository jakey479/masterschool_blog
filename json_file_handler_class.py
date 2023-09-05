import json


class JsonFileHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def write_python_object_to_json(self, python_object):
        with open(self.filepath, 'w') as fileobj:
            json.dump(python_object, fileobj, indent=4)

    def return_python_object_from_json(self, json_filepath):
        with open(json_filepath) as fileobj:
            python_object = json.load(fileobj)
        return python_object