#!/usr/bin/python3
"""create a file storage instance and reload"""

from models.engine.file_storage import Filestorage

storage = Filestorage()
storage.reload()
