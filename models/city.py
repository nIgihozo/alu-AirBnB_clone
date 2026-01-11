#!/usr/bin/python3
"""This module inherites from BaseModel to define City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""

