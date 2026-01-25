#!/usr/bin/python3
"""Unittests for BaseModel class."""

from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ contains tests for BaseModel class """

    def test_instance_creation(self): 
        """Test that a BaseModel instance is created with id and timestamps""" 

        bm = BaseModel() 
        self.assertIsInstance(bm, BaseModel) 
        self.assertIsInstance(bm.id, str) 
        self.assertIsInstance(bm.created_at, datetime) 
        self.assertIsInstance(bm.updated_at, datetime) 
        
    def test_str_representation(self): 
        """Test the __str__ method returns the correct format""" 

        bm = BaseModel() 
        string = str(bm) 
        self.assertIn("[BaseModel]", string) 
        self.assertIn(bm.id, string) 
        
    def test_save_method_updates_updated_at(self): 
        """Test that save() updates the updated_at timestamp""" 

        bm = BaseModel() 
        old_updated_at = bm.updated_at 
        bm.save() 
        self.assertNotEqual(old_updated_at, bm.updated_at) 
        
    def test_to_dict_contains_correct_keys(self): 
        """Test that to_dict() returns a dictionary with expected keys""" 
        
        bm = BaseModel() 
        bm_dict = bm.to_dict() 
        self.assertIn("id", bm_dict) 
        self.assertIn("created_at", bm_dict) 
        self.assertIn("updated_at", bm_dict) 
        self.assertIn("__class__", bm_dict) 
        self.assertEqual(bm_dict["__class__"], "BaseModel") 
        
if __name__ == "__main__": 
    unittest.main()
    
