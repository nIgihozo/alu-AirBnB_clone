#!/usr/bin/python3
"""Unittests for Amenity class."""

from models.amenity import Amenity
import unittest

class TestAmenity(unittest.TestCase):
    """ contains tests for Amenity class """

    def test_instance_creation(self):
        """Test that an Amenity instance is created with default attributes"""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
