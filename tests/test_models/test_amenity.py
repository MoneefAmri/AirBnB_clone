#!/usr/bin/python3
"""Tests for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_initial_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
