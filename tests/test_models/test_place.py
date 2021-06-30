#!/usr/bin/python3
"""Unittests for Place"""


import os
import models
from models.place import Place
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test Place Class"""

    def test_Place_id(self):
        """Test for Place id"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "id"))

    def test_Place_name(self):
        """Test for Place name"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "name"))
        self.assertEqual(test_place.name, "")

    def check_inst(self):
        """Check inst"""
        test_place = Place()
        self.assertIsInstance(test_place, BaseModel)
