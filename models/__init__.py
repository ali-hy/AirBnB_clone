#!/usr/bin/python3
'''entry point to models/engine package'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
