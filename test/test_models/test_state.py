#!/usr/bin/python3
"""This module uses unittest to test the State class."""

from models.state import State
import unittest

class TestState(unittest.TestCase):
    """ contains tests for State class """

    def test_instance_creation(self):
        """Test that a State instance is created with default attributes"""

        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()