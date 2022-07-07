#!/usr/bin/python3
"""
create an unique instance of the class FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()  # Loads saved info in json file if the file exists
