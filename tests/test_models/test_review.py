#!/usr/bin/python3
"""Unittests for Review"""


import os
import models
from models.review import Review
import unittest
from datetime import datetime


class Test_Review(unittest.TestCase):
    """Test Review Class"""

    def test_Review_id(self):
        """Test for Review id"""
        test_review = Review()
        self.assertTrue(hasattr(test_review, "user_id"))

    def test_Review_name(self):
        """Test for Review text"""
        test_review = Review()
        self.assertTrue(hasattr(test_review, "text"))

    def check_inst(self):
        """Check inst"""
        test_review = Review()
        self.assertIsInstance(test_review, BaseModel)
