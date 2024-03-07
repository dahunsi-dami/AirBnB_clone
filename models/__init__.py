#!/usr/bin/python3
"""Creates unique FileStorage instace for our application."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
