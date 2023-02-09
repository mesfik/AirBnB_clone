#!/usr/bin/python3

import uuid
import datetime
"""
A python module for a base model of airbnb
"""
class BaseModel():
    """
    A class BaseModel that defines all common attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of base model class
        Args: *args: non key worded argument
              **kwargs: key worded arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        for keys, value in kwargs.items():
            if key in ['id', 'created_at', 'updated_at']:
                continue
            setattr(self, key, value)

    def __str__(self):
        """
        A string object form representation
        """
        return ("[{}] {} {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        A public instance method that updates datetime 
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        A public instance method dictionary containing all keys/values of __dict__
        Return: all keys/values of __dict__
        """
        base_dict = self.__dict__.copy()
        base_dict['class'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
