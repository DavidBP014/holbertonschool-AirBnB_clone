#!/usr/bin/python3
"""
Class that defines user
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that defines user
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
