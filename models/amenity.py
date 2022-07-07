#!/usr/bin/python3
"""
Class that defines user
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Initialize public Amenity class attributes
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
