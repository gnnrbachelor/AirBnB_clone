#!/usr/bin/python3
"""Unittests for City"""


import os
import models
from models.city import City
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test City Class"""

    def test_city_id(self):
        """Test for city id"""
        test_town = City()
        self.assertTrue(hasattr(test_town, "id"))

    def test_city_name(self):
        """Test for city name"""
        test_town = City()
        self.assertTrue(hasattr(test_town, "name"))
        self.assertEqual(test_town.name, "")

    def check_inst(self):
        """Check inst"""
        test_town = City()
        self.assertIsInstance(test_town, BaseModel)
