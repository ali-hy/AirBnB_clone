#!/usr/bin/python3
'''This file includes tests for the BaseModel class'''
from datetime import datetime
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''class to test BaseModel class'''
    def setUp(self):
        """Setup TestBaseModel instance with BaseModel instance"""
        self.model = BaseModel()

    def test_id(self):
        """Test id attribute of BaseModel instance"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test created_at attribute of BaseModel instance"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute of BaseModel instance"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method of BaseModel instance"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_dict_constructor(self):
        """Test constructor with kwargs of BaseModel class"""
        model_dict = {
            'id': 'abc',
            '__class__': 'BaseModel',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }

        model = BaseModel(**model_dict)
        self.assertDictEqual(model_dict, model.to_dict())
