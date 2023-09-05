import json


class JsonFileHandler:

    @staticmethod
    def write_python_object_to_json(filepath: str, python_object):
        with open(filepath, 'w') as fileobj:
            json.dump(python_object, fileobj, indent=4)

    @staticmethod
    def return_python_object_from_json(filepath: str):
        with open(filepath) as fileobj:
            python_object = json.load(fileobj)
        return python_object
