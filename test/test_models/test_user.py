#!/usr/bin/python3
"""This module uses unittest to test the User class."""

from models.user import User
import unittest

class TestUser(unittest.TestCase):
    """ contains tests for User class """

    def test_instance_creation(self):
        """Test that a User instance is created with default attributes"""

        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()