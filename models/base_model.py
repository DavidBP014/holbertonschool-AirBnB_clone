#!/usr/bin/python3
"""
    Class that defines a Base model
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
        Class that defines Base model attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
            Create new instances according given arguments and store the info
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Modify the stdr output with a specific format
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
            Update the attribute updated_at with the current datetime
            and save changes in json file.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Return a Dictionary with specific attributes and format
        """
        printDictionary = self.__dict__.copy()
        printDictionary.update({'created_at': self.created_at.isoformat(),
                                'updated_at': self.updated_at.isoformat(),
                                '__class__': type(self).__name__})
        return printDictionary
