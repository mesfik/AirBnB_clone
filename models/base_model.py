#!/usr/bin/python3

import models
import uuid
from datetime import datetime
import json
"""
A python module for a base model of airbnb
"""


class BaseModel():
    """
    A class BaseModel that defines all common
    attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of base model class
        Args: *args: non key worded argument
              **kwargs: key worded arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if (key != "__class__"):
                    setattr(self, key, value)
            creat = self.created_at
            update = self.updated_at
            creat = datetime.strptime(creat, '%Y-%m-%dT%H:%M:%S.%f')
            update = datetime.strptime(update, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        A string object form representation
        Return: class name
                id
                __dict__
        """
        nclass = self.__class__.__name__
        return "[{}] {} {}".format(nclass, self.id, self.__dict__)

    def save(self):
        """
        A public instance method that updates datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        A public instance method dictionary containing
        all keys/values of __dict__
        Return: all keys/values of __dict__
        """
        b_dict = self.__dict__.copy()
        if type(self.created_at) is not str:
            b_dict["created_at"] = self.created_at.isoformat()
        if type(self.updated_at) is not str:
            b_dict["updated_at"] = self.updated_at.isoformat()
        b_dict["__class__"] = self.__class__.__name__
        return b_dict
