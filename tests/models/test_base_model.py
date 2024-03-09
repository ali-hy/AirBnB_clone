#!/usr/bin/python3
'''This file includes tests for the BaseModel class'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''class to test BaseModel class'''
    def test_init(self):
        '''tests the constructor'''
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        '''tests the to_dict method'''
        model = BaseModel()
        self.assertRegex(str(model.to_dict()),
                         "{'.+': .+, '.+': .+, '.+': .+, '.+': '.+}")

    def test_save(self):
        '''tests the save method'''
        model = BaseModel()
        old = model.updated_at
        model.save()
        new = model.updated_at
        self.assertNotEqual(old, new)
