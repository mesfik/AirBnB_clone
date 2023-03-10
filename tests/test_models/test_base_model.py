#!/usr/bin/python3

"""
A unittest for the base model
"""
from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    """
    A clss to test using unittest the basemodel
    """
    def test_init(self):
        """
        inital instance method tests
        """
        baseM = BaseModel()
        self.assertIsInstance(baseM, BaseModel)
        self.assertIsInstance(baseM.id, str)
        self.assertIsInstance(baseM.created_at, datetime)
        self.assertIsInstance(baseM.updated_at, datetime)

    def test_save(self):
        """
        save instance method to be tested
        """
        baseM = BaseModel()
        created_at = baseM.updated_at
        baseM.save()
        self.assertNotEqual(baseM.created_at, baseM.updated_at)

    def test_to_dict(self):
        """
        dictionary instance method to be tested
        """
        baseM = BaseModel()
        base_dict = baseM.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], baseM.id)
        self.assertEqual(base_dict['__class__'], baseM.__class__.__name__)
        self.assertEqual(baseM.created_at.isoformat(), base_dict['created_at'])
        self.assertEqual(baseM.updated_at.isoformat(), base_dict['updated_at'])
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(base_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
