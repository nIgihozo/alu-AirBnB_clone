#!/usr/bin/python3
"""This module uses unittest to test the FileStorage class."""

from models.engine.file_storage import FileStorage
import unittest

class TestFileStorage(unittest.TestCase):
    """ contains tests for FileStorage class """

    def test_instance_creation(self):
        """Test that a FileStorage instance is created correctly"""

        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(callable(getattr(storage, "all")))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(callable(getattr(storage, "new")))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(callable(getattr(storage, "save")))
        self.assertTrue(hasattr(storage, "reload"))
        self.assertTrue(callable(getattr(storage, "reload")))
        
    def test_all_method(self):
        """Test the all method of FileStorage"""
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, storage._FileStorage__objects)

    def test_new_method(self):
        """Test the new method of FileStorage"""
        from models.base_model import BaseModel

        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_save_and_reload_methods(self):
        """Test the save and reload methods of FileStorage"""
        from models.base_model import BaseModel
        import os

        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        # Ensure the file was created
        self.assertTrue(os.path.isfile(storage._FileStorage__file_path))

        # Clear the current objects and reload from file
        storage._FileStorage__objects = {}
        storage.reload()

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].to_dict(), obj.to_dict())

        # Clean up the created file
        os.remove(storage._FileStorage__file_path)

if __name__ == '__main__':
    unittest.main()
