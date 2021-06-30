#!/usr/bin/python3
"""Unittests for State"""


import os
import models
from models.state import State
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test State Class"""

    def test_State_id(self):
        """Test for State id"""
        state = State()
        self.assertTrue(hasattr(state, "id"))

    def test_State_name(self):
        """Test for State name"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def check_inst(self):
        """Check inst"""
        state = State()
        self.assertIsInstance(state, BaseModel)
