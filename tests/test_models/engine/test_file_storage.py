#!/usr/bin/python3
import unittest
from datetime import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class that defines all common tests for FileStorage"""

    def setUp(self):
        """Setup TestFileStorage instance with FileStorage instance"""
        self.storage = FileStorage()

    def test_all(self):
        """Test all method of FileStorage instance"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method of FileStorage instance"""
        obj = BaseModel()
        self.storage.new(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(obj.to_dict(), self.storage.all()[key].to_dict())

    def test_save_and_reload(self):
        """Test save and reload methods of FileStorage instance"""
        obj = BaseModel(id='abc',
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat())
        self.storage.new(obj)
        self.storage.save()

        self.storage.reload()
        key = obj.__class__.__name__ + "." + obj.id
        self.assertIn(key, self.storage.all())
        self.assertDictEqual(obj.to_dict(), self.storage.all()[key].to_dict())
