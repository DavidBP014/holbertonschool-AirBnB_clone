#!/usr/bin/python3
"""
    Class that defines Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Initialize public Review class attributes
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
