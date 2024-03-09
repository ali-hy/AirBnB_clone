#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''class to test BaseModel class'''
    def test_save_reload(self):
        '''tests the constructor'''
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)

        objs = storage.all()
        storage.save()
        FileStorage.__objects = dict()
        storage.reload()
        self.assertDictEqual(objs, storage.all())
