#!/usr/bin/python3
"""FileStorage module for serialization & deserialization."""

import json


class FileStorage:
    """Serializes instance to JSON & deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary `__objects`."""
        return self.__objects

    def new(self, obj):
        """sets obj in __objects with key `<obj class name>.id`."""
        objkey = obj["__class__"] + "." + obj["id"]
        self.__objects[objkey] = obj

    def save(self):
        """serializes __objects to JSON & save to __file_path."""
        mobj = {}
        for k, v in self.__objects.items():
            mobj[k] = v
        with open(self.__file_path, 'w') as f:
            json.dump(mobj, f)

    def reload(self):
        """deserializes json file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                des_dict = json.load(f)
                for k, v in des_dict.items():
                    """
                    from models.base_model import BaseModel
                    cls_nm, obj_id = k.split('.')
                    agpas = BaseModel(**v)
                    self.__objects[k] = agpas
                    print(f"Self.__objects is {self.__objects.__str__()}")
                    """
                    from models.base_model import BaseModel
                    # cls_nm, obj_id = k.split('.')
                    # obj_build = eval(cls_nm)
                    obj_inst = BaseModel(**v)
                    self.__objects[k] = obj_inst.to_dict()
                    # print(f"Self.__objects is {self.__objects}")
        except FileNotFoundError:
            pass
