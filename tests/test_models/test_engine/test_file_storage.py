#!/usr/bin/python3
"""Unittests for engine"""


import os
from os import path
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

    def test_new(self):
        """Test new"""
        engine = FileStorage()
        collection = engine.all()
        state = State()
        state.id = "123123"
        engine.new(state)
        k = state.__class__.__name__ + "." + str(state.id)
        self.assertIsNotNone(collection[k])

    def test_all(self):
        """Test all"""
        store = FileStorage()
        collection = store.all()
        self.assertEqual(type(collection), dict)
        self.assertIs(collection, store._FileStorage__objects)

    def test_save(self):
        """Test save"""
        bm = BaseModel()
        bm.save()
        models.storage.new(bm)
        test = ""
        with open("file.json", "r") as f:
            test = f.read()
            self.assertIn("BaseModel." + bm.id, test)

    def test_reload(self):
        """Test reload"""
        store = FileStorage()
        bm = BaseModel()
        store.new(bm)
        old = store.all()
        store.save()
        store.reload()
        new = store.all()
        for k, v in old.items():
            self.assertTrue(k in new)

    def test_save_alt(self):
        """Test again for save"""
        usr = User()
        models.storage.new(usr)
        test = ""
        with open("file.json", "r") as f:
            test = f.read()
            self.assertIn("User." + usr.id, test)

if __name__ == "__main__":
    unittest.main()
