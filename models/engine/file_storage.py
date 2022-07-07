#!/usr/bin/python3
"""
Class that defines FileStorage
"""
import json
import os


class FileStorage():
    """
        Initialize private FileStorage class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the __objects dictionary
        """
        return(self.__objects)

    def new(self, obj):
        """
            Creates a new key(class.id) & value(instance attributes dictionary)
            of an instance in __objects dictionary
        """
        if obj is not None:
            self.__objects.update(
                {str(type(obj).__name__ + "." + obj.id): obj})

    def save(self):
        """
            Append all keys & values set on __objects dictionary
            into a new dictionary to save all instances in a json file
        """
        dict_serialized = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                dict_serialized[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(dict_serialized, my_file)

    def reload(self):
        """
            Load the .json file(verify existence), set all keys & values into
            the __objects dictionary and recreate instances found in the file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dict_deserialized = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as my_file:
                content = my_file.read()
        else:
            return
        if content is not None or bool(content) is True:
            dict_deserialized = json.loads(content)
        for key, value in dict_deserialized.items():
            if key not in self.__objects.keys():
                ClassName = value["__class__"]
                new_instance = eval("{}(**value)".format(ClassName))
                self.new(new_instance)
        else:
            pass
