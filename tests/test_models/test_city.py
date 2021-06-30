#!/usr/bin/python3
"""Unittests for City"""


import os
import models
from models.city import City
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test City Class"""

    def test_city(self):
        """Test for city"""
        test_town = City()
        self.assertTrue(hasattr(test_town, "state_id"))
        self.assertTrue(hasattr(test_town, "name"))
        self.assertFalse(hasattr(test_town, "parking"))

