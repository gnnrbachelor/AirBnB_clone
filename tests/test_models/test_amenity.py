#!/usr/bin/python3
"""Unittests for Amenity"""


import os
import models
from models.amenity import Amenity
import unittest
from datetime import datetime


class Test_Amenity(unittest.TestCase):
    """Test Amenity Class"""

    def test_city_id(self):
        """Test for city id"""
        test_amenity = Amenity()
        self.assertTrue(hasattr(test_amenity, "id"))

    def test_city_name(self):
        """Test for city name"""
        test_amenity = Amenity()
        self.assertTrue(hasattr(test_amenity, "name"))

    def check_inst(self):
        """Check inst"""
        test_amenity = Amenity()
        self.assertIsInstance(test_amenity, BaseModel)
