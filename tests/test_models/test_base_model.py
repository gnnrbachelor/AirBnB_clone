#!/usr/bin/python3

"""Unittest for BaseModel"""


from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import pep8
import unittest
import uuid
import json
from time import sleep
from unittest import mock
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test BaseModel Class"""

    def setup(self):
        self.b = BaseModel()

    def test_id(self):
        """Tests for id"""
        self.b = BaseModel()
        self.b.save()
        self.assertTrue(hasattr(self.b, "created_at"))

    def test_updated_at(self):
        """Tests Save"""
        bm = BaseModel()
        first = bm.updated_at
        sleep(0.05)
        second = bm.updated_at
        bm.save()
        self.assertEqual(first, second)

    def test_save(self):
        """Tests Save"""
        with self.assertRaises(TypeError) as error:
            bm = BaseModel()
            bm.save("test")
        self.assertEqual(str(error.exception),
                        "save() takes 1 positional argument but 2 were given")

    def test_save_none(self):
        """Test save none"""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_str(self):
        """test str rep"""
        bm = BaseModel()
        test = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(test, str(bm))

    def test_save_attr(self):
        """Test save attr"""
        bm = BaseModel()
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_to_dict(self):
        """Test to_dict"""
        bm = BaseModel()
        dictionary = bm.__dict__.copy()
        dictionary["__class__"] = bm.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        check = bm.to_dict()
        self.assertDictEqual(dictionary, check)

    @mock.patch('models.storage')
    def test_save_storage(self, storage):
        """Test save with storage"""
        bm = BaseModel()
        old_create = bm.created_at
        old_update = bm.updated_at
        bm.save()
        new_create = bm.created_at
        new_update = bm.updated_at
        self.assertEqual(old_create, new_create)
        self.assertNotEqual(old_update, new_update)
        self.assertTrue(storage.save.called)


if __name__ == '__main__':
    unittest.main()
