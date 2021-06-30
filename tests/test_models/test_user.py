#!/usr/bin/python3
"""Unittests for User"""


import os
import models
from models.user import User
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test User Class"""
    def test_email(self):
        """Test email"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """Test password"""
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """Test first name"""
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """Test last name"""
        self.assertEqual(str, type(User.last_name))


