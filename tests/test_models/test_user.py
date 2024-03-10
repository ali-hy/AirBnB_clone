#!/usr/bin/python3
'''User Class tests'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class that defines all common tests for User"""

    def setUp(self):
        """Setup TestUser instance with User instance"""
        self.user = User()

    def test_attributes(self):
        """Test attributes of User instance"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attribute_values(self):
        """Test default value of User instance attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
