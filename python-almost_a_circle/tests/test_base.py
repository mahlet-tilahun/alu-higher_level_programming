#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):
    def test_one_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_three_instances(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_argument(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
    
    def test_of_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_of_json_string_empty_array(self):
        self.assertEqual(Base.to_json_string([]), "[]")
    
    def test_of_json_string_dictlist(self):
        self.assertEqual(Base.to_json_string([{ 'id': 12 }]), '[{"id": 12}]')
    
    def test_from_json_string_dictlist(self):
        self.assertEqual(Base.from_json_string(None), [])
        
    def test_from_json_string_dictlist(self):
        self.assertEqual(Base.from_json_string([]), [])

    def test_from_json_string_dictlist(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{ "id": 89 }])
    
    

if __name__ == '__main__':
    unittest.main()
