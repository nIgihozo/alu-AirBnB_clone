#!/usr/bin/python3
"""This module uses unittest to test the Review class."""

from models.review import Review
import unittest

class TestReview(unittest.TestCase):
    """ contains tests for Review class """

    def test_instance_creation(self):
        """Test that a Review instance is created with default attributes"""

        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.text, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")

if __name__ == '__main__':
    unittest.main()