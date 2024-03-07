#!/usr/bin/python3
"""FileStorage module for serialization & deserialization."""

import json


class FileStorage:
    """Serializes instance to JSON & deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary `__objects`."""
        return self.__class__.__objects

    def new(self, obj):
        """sets obj in __objects with key `<obj class name>.id`."""
        objkey = self.__class__.__name__ + "." + obj.id
        self.__class__.__objects[objkey] = obj

    def save(self):
        """serializes __objects to JSON & save to __file_path."""
        with open(self.__class__.__file_path, 'w') as f:
            json_str = json.dumps(self.__class__.__name__.__objects)
            f.write(json_str)

    def reload(self):
        """deserializes json file to __objects."""
        try:
            with open(self.__class__.__file_path, 'r') as f:
                if len(f.read()) > 0:
                    self.__class__.__objects = json.loads(f.read())
        except FileNotFoundError:
            pass
