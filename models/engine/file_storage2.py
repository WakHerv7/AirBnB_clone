#!/usr/bin/python3
"""serialuzation and deserialuzation"""
import datetime
import json
import os

class FileStorage():

    """serial8zation and deserialuzation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets new obj in __objects dict"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes object to json file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserialize json object"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[v["__class__"]](**v) for key, value in obj_dict.items()}
