#!/usr/bin/python3
"""Unittest for Base
"""
import os
import unittest
from models.square import Square
import io
import sys


class TestMaxInteger(unittest.TestCase):
    def test_square_one_arg(self):
        obj = Square(1)
        self.assertEqual(obj.size, 1)

    def test_square_two_arg(self):
        obj = Square(1, 2)
        self.assertEqual(obj.x, 2)

    def test_square_three_arg(self):
        obj = Square(1, 2, 3)
        self.assertEqual(obj.y, 3)

    def test_square_four_arg(self):
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.id, 4)
    
    def test_square_one_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square("1")
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_two_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square(1, "2")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_three_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square(1, 2, "3")
        self.assertEqual(str(err.exception), "y must be an integer")
    
    def test_square_one_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(-1)
        self.assertEqual(str(err.exception), "width must be > 0")
    
    def test_square_two_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(1, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")
    
    def test_square_three_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(1, 2, -3)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_square_one_arg_zero(self):
        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")
    
    def test_str(self):
        obj = Square(2, 2, 2, 10)
        self.assertEqual(obj.__str__(), "[Square] (10) 2/2 - 2")
    
    def test_to_dict(self):
        obj = Square(2, 2, 2, 100)
        self.assertEqual(obj.to_dictionary(), {'size': 2, 'id': 100, 'x': 2, 'y': 2})
    
    def test_update_empty(self):
        obj = Square(2)
        obj.update()
        self.assertEqual(obj.size, 2)

    def test_update_one_arg(self):
        obj = Square(2)
        obj.update(89)
        self.assertEqual(obj.id, 89)

    def test_update_two_arg(self):
        obj = Square(2)
        obj.update(89, 1)
        self.assertEqual(obj.size, 1)

    def test_update_three_arg(self):
        obj = Square(2)
        obj.update(89, 1, 2)
        self.assertEqual(obj.x, 2)

    def test_update_four_arg(self):
        obj = Square(2)
        obj.update(89, 1, 2, 3)
        self.assertEqual(obj.y, 3)
    
    def test_update_one_kwarg(self):
        obj = Square(2)
        obj.update(**{ 'id': 89})
        self.assertEqual(obj.id, 89)

    def test_update_two_kwarg(self):
        obj = Square(2)
        obj.update(**{ 'id': 89, 'size': 1})
        self.assertEqual(obj.size, 1)

    def test_update_three_kwarg(self):
        obj = Square(2)
        obj.update(**{ 'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(obj.x, 2)

    def test_update_four_kwarg(self):
        obj = Square(2)
        obj.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(obj.y, 3)
    
    def test_create_one_kwarg(self):
        obj = Square.create(**{ 'id': 89 })
        self.assertEqual(obj.id, 89)

    def test_create_two_kwarg(self):
        obj = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(obj.size, 1)

    def test_create_three_kwarg(self):
        obj = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(obj.x, 2)

    def test_create_four_kwarg(self):
        obj = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(obj.y, 3)

    def test_save_to_file_None(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
    
    def test_save_to_file_empty(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
    
    def test_save_to_file_one_arg(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 44, "size": 1, "x": 0, "y": 0}]')
    
    def test_load_from_file_not_exists(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        objs = Square.load_from_file()
        self.assertEqual(objs, [])
        
    def test_load_from_file_exists(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([Square(1)])
        objs = Square.load_from_file()
        
        self.assertEqual([i.to_dictionary() for i in objs], [{"id": 42, "size": 1, "x": 0, "y": 0}])
    
    

        
if __name__ == '__main__':
    unittest.main()
