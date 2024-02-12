#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
from unittest.mock import patch

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_attrs(self):
        """
        Test that User instance has the expected attributes.
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        """
        Test that User class inherits from BaseModel.
        """
        user = User()
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(user, BaseModel)

    def test_user_instance(self):
        """
        Test that User class creates a new instance correctly.
        """
        user = User(email="test@88.com", password="password", first_name="Moneef", last_name="Amri")
        self.assertEqual(user.email, "test@88.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "Moneef")
        self.assertEqual(user.last_name, "Amri")

    @patch('models.storage')
    def test_usr_save(self, mock_storage):
        """Tests the save method of User"""
        user = User()
        user.first_name = "Moneef"
        user.last_name = "Amri"
        user.email = "test@88.com"
        user.password = "password"
        user.save()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
