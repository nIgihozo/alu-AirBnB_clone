#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Storage engine for AirBnB clone project"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add obj with key <obj class name>.id to dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        objdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize JSON file to __objects if file exists"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)
                for k, v in objdict.items():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    # Only BaseModel supported for now
                    if cls_name == "BaseModel":
                        self.new(BaseModel(**v))
        except FileNotFoundError:
            pass

