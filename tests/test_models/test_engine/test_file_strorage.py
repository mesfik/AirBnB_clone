#!/usr/bin/python3
"""file_storage unittest module"""

import os
import json
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorageclass"""

    def setUp(self):
        """ sets up this each test """
        self.user = User()
        self.user.id = "98"
        self.user.first_name = "Peter"
        self.user.last_name = "Wu"
        self.user.email = "naruto@hokage.com"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.user

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_storage_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertFalse(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_peter_wu(self):
        """ checks peter out. whatta hottie """
        self.assertTrue(self.user)
        self.assertEqual(self.user.first_name, "Peter")
        self.assertFalse(self.user.password)
        self.assertNotEqual(self.user.id, 98)
        self.assertEqual(self.user.id, "98")

    def test_basic_init(self):
        """ tests the init and file path? """
        dank = BaseModel()
        poop = FileStorage()
        poopcopy = poop
        notpoop = FileStorage()
        self.assertEqual(poop, poopcopy)
        self.assertNotEqual(poop, notpoop)
        self.assertTrue(poop)
        self.assertFalse(poop == notpoop)
        self.assertIs(poop, poopcopy)
        self.assertIsNot(poop, notpoop)
        self.assertIsNotNone(poop)
        self.assertIsInstance(poop, FileStorage)
        self.assertNotIsInstance(dank, FileStorage)

    def test_google_doc(self):
        """ more harder tests """
        storage = FileStorage()
        # TEST ALL. NO CELL A
        # Cell B tests init and objects and file path
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertFalse(storage._FileStorage__objects)
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

        # Cell C tests all() and type
        test = User()
        test2 = test.id
        key = "User." + test2
        all_storage = storage.all()
        self.assertEqual(type(all_storage), dict)

        # Cell D tests new() and the dict
        my_model = BaseModel()
        self.assertEqual(
                str(type(my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(
                sorted(my_model.__dict__.keys()),
                ['created_at', 'id', 'updated_at'])

        # Cell E tests save() and json file
        doesFileExist = User()
        self.assertTrue(os.path.isfile("file.json"))

        # Cell F tests reload and the json file
        os.rename("file.json", "CAKEisAlie")
        self.assertFalse(os.path.isfile("file.json"))
        newPoop = Place()
        # self.assertTrue(storage._FileStorage__objects)
        os.rename("CAKEisAlie", "file.json")
        self.assertTrue(os.path.isfile("file.json"))


    def test_methods(self):
        """ tests the public instance mthods """
        bm = FileStorage()
        self.assertTrue(hasattr(bm, "all"))
        self.assertTrue(hasattr(bm, "new"))
        self.assertTrue(hasattr(bm, "save"))
        self.assertTrue(hasattr(bm, "reload"))

    def test_save(self):
        """ tests the save(self) in BaseModel.
        Added this post grading """
        bm = BaseModel()
        self.assertIs(type(bm.id), str)
        self.assertNotEqual(bm.created_at, datetime.utcnow())
        self.assertNotEqual(bm.updated_at, datetime.utcnow())
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)
        # another way to test save
        os.remove("file.json")
        self.assertFalse(os.path.isfile("file.json"))
        bm.save()
        self.assertTrue(os.path.isfile("file.json"))
        # another way to test save
        os.remove("file.json")
        bm2 = BaseModel()
        bm2.save()
        with open("file.json", mode='r', encoding='utf-8') as f:
            x = json.loads(f.read())
            length1 = len(x)
        bm3 = BaseModel()
        bm3.save()
        with open("file.json", mode='r', encoding='utf-8') as f:
            x = json.loads(f.read())
            length2 = len(x)
        self.assertTrue(length2 > length1)

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """
        bm = BaseModel()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """
        self.assertTrue(hasattr(BaseModel, "save"))


if __name__ == "__main__":
    unittest.main()
