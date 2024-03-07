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
            json_str = json.dumps(self.__dict__)
            print(" ***** OBJECT'S DICT ***** ")
            print(self.created_at)
            f.write(json_str)

    def reload(self):
        """deserializes json file to __objects."""
        try:
            with open(self.__class__.__file_path, 'r') as f:
                f_content = f.read()
                if len(f_content) > 0:
                    self.__class__.__objects = json.loads(f_content)
                # print(f"__objects = {self.__class__.__objects}")
        except FileNotFoundError:
            pass
