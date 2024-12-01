#!/usr/bin/python3
"""Unittest for Base
"""
import os
import unittest
from models.rectangle import Rectangle
import io
import sys


class TestMaxInteger(unittest.TestCase):
    def test_two_arguments(self):
        b1 = Rectangle(1, 2)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.x, 0)

    def test_three_arguments(self):
        b2 = Rectangle(1, 2, 3)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 0)

    def test_four_arguments(self):
        b2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 4)

    def test_five_arguments(self):
        b2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(b2.id, 5)

    def test_width_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("1", 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_height_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, "2")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_x_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, "3")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(err.exception), "y must be an integer")
    
    def test_width_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 0)
        self.assertEqual(str(err.exception), "height must be > 0")
    
    def test_area(self):
        obj = Rectangle(2, 2)
        self.assertEqual(obj.area(), 4)
        
    def test_str(self):
        obj = Rectangle(2, 2, 2, 2, 10)
        self.assertEqual(obj.__str__(), "[Rectangle] (10) 2/2 - 2/2")
      
    def test_display_no_xy(self):
        obj = Rectangle(2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        obj = Rectangle(2, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "  ##\n  ##\n")
        
    def test_display(self):
        obj = Rectangle(2, 2, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  ##\n  ##\n")
    
    def test_to_dict(self):
        obj = Rectangle(2, 2, 2, 2, 100)
        self.assertEqual(obj.to_dictionary(), {'height': 2, 'id': 100, 'width': 2, 'x': 2, 'y': 2})
    
    def test_update_empty(self):
        obj = Rectangle(2, 2)
        obj.update()
        self.assertEqual(obj.width, 2)

    def test_update_one_arg(self):
        obj = Rectangle(2, 2)
        obj.update(89)
        self.assertEqual(obj.id, 89)

    def test_update_two_arg(self):
        obj = Rectangle(2, 2)
        obj.update(89, 1)
        self.assertEqual(obj.width, 1)

    def test_update_three_arg(self):
        obj = Rectangle(2, 2)
        obj.update(89, 1, 2)
        self.assertEqual(obj.height, 2)

    def test_update_four_arg(self):
        obj = Rectangle(2, 2)
        obj.update(89, 1, 2, 3)
        self.assertEqual(obj.x, 3)

    def test_update_five_arg(self):
        obj = Rectangle(2, 2)
        obj.update(89, 1, 2, 3, 4)
        self.assertEqual(obj.y, 4)
        
    def test_create_one_kwarg(self):
        obj = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(obj.id, 89)

    def test_create_two_kwarg(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(obj.width, 1)

    def test_create_three_kwarg(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(obj.height, 2)

    def test_create_four_kwarg(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(obj.x, 3)

    def test_create_five_kwarg(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(obj.y, 4)
    
    def test_save_to_file_None(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
            
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
    
    def test_save_to_file_empty(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
    
    def test_save_to_file_two_arg(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 23, "width": 1, "height": 2, "x": 0, "y": 0}]')
    
    def test_load_from_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        Rectangle.save_to_file([Rectangle(1, 2)])
        objs = Rectangle.load_from_file()
        self.assertEqual([i.to_dictionary() for i in objs], [{"id": 21, "width": 1, "height": 2, "x": 0, "y": 0}])
        
if __name__ == '__main__':
    unittest.main()
