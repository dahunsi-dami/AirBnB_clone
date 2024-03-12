#!/usr/bin/python3
"""
    The unittest module to test for all functionalities
    associated with the TestBaseModel class and its
    subclasses.
"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """The main class for conducting tests."""

    def setUp(self):
        """Create two instances of the class BaseModel."""
        self.m1 = BaseModel()
        self.m2 = BaseModel()

    def test_uuid(self):
        """Test `uuid` instance variable."""
        self.assertIsInstance(self.m1, BaseModel)
        self.assertTrue(hasattr(self.m1, "id"))
        self.assertNotEqual(self.m1.id, self.m2.id)
        self.assertIsInstance(self.m1.id, str)

    def test_created_at(self):
        """Test `created_at` instance variable."""
        self.assertTrue(hasattr(self.m1, "created_at"))
        self.assertIsInstance(self.m1.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test `updated_at` instance variable."""
        self.assertTrue(hasattr(self.m1, "updated_at"))
        self.assertIsInstance(self.m1.updated_at, datetime.datetime)

    def test_save(self):
        """Test save() method."""
        self.m1.name = "Peter"
        self.m1.save()
        self.assertIn("name", self.m1.to_dict())

    def test___str__(self):
        """Test __str__ magic method."""
        c_n = self.m1.__class__.__name__  # c_n <--> class name
        self.assertIn(f"[{c_n}] ({self.m1.id})", str(self.m1))
        self.assertIn(c_n, str(self.m1))
        self.assertIn(self.m1.id, str(self.m1))
        self.assertIn("created_at", str(self.m1))
        self.assertIn("updated_at", str(self.m1))

    def test_to_dict(self):
        """Test to_dict() method."""
        self.assertIsInstance(self.m1.to_dict(), dict)

        self.assertIn("__class__", self.m1.to_dict())
        self.assertIn("id", self.m1.to_dict())
        self.assertIn("created_at", self.m1.to_dict())
        self.assertIn("updated_at", self.m1.to_dict())

        self.m1.name = "Peter"
        self.assertIn("name", self.m1.to_dict())

        created_at = self.m1.created_at.isoformat()
        updated_at = self.m1.updated_at.isoformat()

        self.assertEqual(created_at, self.m1.to_dict()["created_at"])
        self.assertEqual(updated_at, self.m1.to_dict()["updated_at"])
