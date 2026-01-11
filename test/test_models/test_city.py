#!/usr/bin/python3
"""Unittests for City class."""
from models.city import City
import unittest

class TestCity(unittest.TestCase):
    """ contains tests for City class """
    def test_instance_creation(self):
        """Test that a City instance is created with default attributes"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()