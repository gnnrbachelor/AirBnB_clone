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
        self.test = City()
        self.assertTrue(hasattr(self.test, "state_id"))
        self.assertTrue(hasattr(self.test, "name"))

