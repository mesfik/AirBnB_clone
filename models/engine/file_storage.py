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

    __file_path = "file.json"

    def __init__(self):
        """
        Initialization of private instance attribute
        Args:
             file_path: initialized file path to file.json
        """
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

        key = obj.__class__.__name__
        self.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """ A public instance method that serilizes object to json
        """
        odict = self.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objdict, file)

    def reload(self):
        """ A public instance method to deserialize the json
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except Exception:
            pass
