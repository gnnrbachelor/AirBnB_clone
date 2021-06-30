#!/usr/bin/python3
"""Unittests for engine"""


import os
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest


class TestFileStorage(unittest.TestCase):
    """Test File Storage Engine Class"""

    def test_all(self):
        """Test all"""
        engine = FileStorage()
        collection = engine.all()
        self.assertEqual(type(collection), dict)
        self.assertIs(collection, engine._FileStorage__objects)

