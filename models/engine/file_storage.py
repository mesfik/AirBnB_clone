#!/usr/bin/python3
"""
A Filestorage module
"""
import json
import os


class FileStorage:
    """ A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def __init__(self, file_path="file.json"):
        """
        Initialization of private instance attribute
        Args:
             file_path: initialized file path to file.json
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
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ A public instance method that serilizes object to json
        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ A public instance method to deserialize the json
        """
        file_path = self.__file_path
        if file_path:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
