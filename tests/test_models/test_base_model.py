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

    def test_save(self):
        """Tests Save"""
        bm = BaseModel()
        first = bm.updated_at
        sleep(0.05)
        second = bm.updated_at
        bm.save()
        self.assertEqual(first, second)

if __name__ == '__main__':
    unittest.main()
