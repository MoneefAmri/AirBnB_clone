#!/usr/bin/python3
"""This is the File Storage module."""
import json

from models.base_model import BaseModel


class FileStorage:
    """
    Class for serializing instances to a JSON file and deserializing JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with key <obj class name>.id.

        Args:
            obj: The object to be set in __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        seria_obj = {}
        for key, obj in self.__objects.items():
            seria_obj[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(seria_obj, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                inp_f = json.load(f)
                for key, value in inp_f.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass
