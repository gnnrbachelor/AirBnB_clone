#!/usr/bin/python3
"""Unittests for engine"""


import os
import datetime
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
import datetime
import unittest


class TestFileStorage(unittest.TestCase):
    """Test File Storage Engine Class"""

    def setUp(self):
        """Set Up"""
        self.test_dummy = BaseModel()

    def tearDown(self):
        """Tear Down"""
        self.test_dummy = None

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

    def test_save_it(self):
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

    def test_reload2(self):
        """Test reload"""
        store = FileStorage()
        bm = BaseModel()
        store.new(bm)
        store.save()
        store.reload()
        self.assertTrue(store.all()["BaseModel.{}".format(bm.id)])
        self.assertTrue(store._FileStorage__objects["BaseModel.{}".format(bm.id)])



    def test_save_alt(self):
        """Test again for save"""
        usr = User()
        models.storage.new(usr)
        models.storage.save()
        test = ""
        with open("file.json", "r") as f:
            test = f.read()
            self.assertIn("User." + usr.id, test)

    def test_save_time(self):
        """Test save time"""
        start = self.test_dummy.updated_at
        self.test_dummy.save()
        end = self.test_dummy.updated_at
        self.assertNotEqual(start, end)
        self.assertEqual(type(start), datetime.datetime)

if __name__ == "__main__":
    unittest.main()
