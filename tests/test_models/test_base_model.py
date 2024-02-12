#!/usr/bin/python3
"""Tests for BaseModel"""
import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_inst(self):
        """Tests basic inputs for the BaseModel class"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)

        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

        my_model.name = "Moneef"
        my_model.number = 88
        self.assertEqual([my_model.name, my_model.number],
                         ["Moneef", 88])

    def test_attrs(self):
        """
        Tests the BaseModel attributes
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_methods(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_str(self):

        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_DT(self):
        """
        Tests the datetime functionality of the BaseModel class.
        """
        my_model = BaseModel()
        my_model.save()
        created_at = my_model.created_at
        updated_at = my_model.updated_at
        self.assertIs(type(created_at), datetime)
        self.assertIs(type(updated_at), datetime)
        self.assertEqual(created_at.isoformat(),
                         my_model.to_dict()['created_at'])
        self.assertEqual(updated_at.isoformat(),
                         my_model.to_dict()['updated_at'])

    def test_uuid(self):
        """
        Tests the uuid of a BaseModel object.
        """
        my_model = BaseModel()
        uuid_object = uuid.UUID(my_model.id, version=4)
        self.assertEqual(str(uuid_object), my_model.id)

    def test_uuid4(self):
        """
        Checks if the id is a valid UUID4.
        """
        my_model = BaseModel()

        my_id = my_model.id
        uuid_object = uuid.UUID(my_id, version=4)
        self.assertIsInstance(uuid.UUID(my_model.id), uuid.UUID)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Moneef"
        my_model.my_number = 88
        m = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "my_number",
                          "name",
                          "__class__"]
        self.assertCountEqual(m.keys(), expected_attrs)
        self.assertEqual(m['__class__'], 'BaseModel')
        self.assertEqual(m['name'], "Moneef")
        self.assertEqual(m['my_number'], 88)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        my_model = BaseModel()
        my_model.name = "Moneef"
        my_model.number = 88
        new_dict = my_model.to_dict()
        expected_dict = {
            "id": my_model.id,
            "created_at": my_model.created_at.isoformat(),
            "updated_at": my_model.updated_at.isoformat(),
            "name": "Moneef",
            "number": 88,
            "__class__": my_model.__class__.__name__
        }

        self.assertDictEqual(expected_dict, new_dict)
        my_model_x = BaseModel()
        my_model_x.name = "Moneef"
        my_model_x.number = 88
        my_model_dict = my_model_x.to_dict()
        self.assertEqual(my_model_dict['name'], 'Moneef')
        self.assertEqual(my_model_dict['number'], 88)

    def test_invalid_created_at(self):
        """
        Test that creating an instance with an invalid created_at attribute
        raises a ValueError
        """
        with self.assertRaises(ValueError):
            my_model = BaseModel(created_at="2021-02-12")

    def test_invalid_updated_at(self):
        """
        Test that creating an instance with an invalid updated_at attribute
        raises a ValueError
        """
        with self.assertRaises(ValueError):
            my_model = BaseModel(updated_at="2024-02-12T11:42:56")


if __name__ == '__main__':
    unittest.main()
