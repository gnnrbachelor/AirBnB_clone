#!/usr/bin/python3
"""
File Storage Module
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os import path


classes = {"BaseModel": BaseModel, "State": State,
           "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class FileStorage:
    """File Storage Class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Getter for __objects"""
        return self.__objects

    def new(self, obj):
        """Saves new obj in __objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Handles serialization of __objects content"""

        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dictionary))

    def reload(self):
        """Handle deserialization of JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                self.__objects[key] = classes[value["__class__"]](**value)
        except:
            pass
