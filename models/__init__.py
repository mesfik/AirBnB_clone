#!/usr/bin/python3
"""
A magic file to be loaded
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
