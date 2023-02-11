#!/usr/bin/python3
"""
A Filestorage module
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def __init__(self, file_path='file.json'):
        """ Initialization a private instance attributes
        Args:
             file_path :initialized file path to file.json
        """
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """A Public instance method all
        Return: the dictionary object
        """
        return self.__objects

    def new(self, obj):
        """
        A public instance method that sets object keys by class name.id
        Args:
             obj: the object with a key <class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ A public instance method that serilizes object to json
        """
        objects = self.__objects
        obj_dict = {obj_id: objects[obj_id].to_dict() for obj_id in objects.keys()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ A public instance method to deserialize the json
        """
        try:
            with open(self.__file_path, 'r') as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except Exception:
            pass
