import unittest
from models.square import Square
import io
import sys

class TestSquare(unittest.TestCase):

    def setUp(self):
        """Reset the stdout before each test"""
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Clean up after test"""
        sys.stdout = sys.__stdout__

    def test_square_inherits_rectangle(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)
        self.assertTrue(type(s), Square)

    def test_square_default_attributes(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_all_attributes(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_square_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_square_invalid_size_value(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_invalid_x(self):
        with self.assertRaises(ValueError):
            Square(5, -3)

    def test_square_invalid_y(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -4)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        s = Square(2)
        s.display()
        self.assertEqual(self.held_output.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        s = Square(2, 1, 1)
        s.display()
        self.assertEqual(self.held_output.getvalue(), "\n ##\n ##\n")

    def test_str_method(self):
        s = Square(4, 2, 3, 99)
        self.assertEqual(str(s), "[Square] (99) 2/3 - 4")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 7, 1, 2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=101, size=8, x=3, y=4)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        s = Square(10, 1, 2, 99)
        expected = {'id': 99, 'size': 10, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create(self):
        s_dict = {'id': 42, 'size': 7, 'x': 2, 'y': 3}
        s = Square.create(**s_dict)
        self.assertEqual(str(s), "[Square] (42) 2/3 - 7")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        s = Square(2, 0, 0, 88)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertIn('"id": 88', f.read())

    def test_load_from_file_no_file(self):
        import os
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        loaded = Square.load_from_file()
        self.assertEqual(loaded, [])

    def test_load_from_file_valid(self):
        s1 = Square(3, 1, 1, 55)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertIsInstance(loaded[0], Square)
        self.assertEqual(str(loaded[0]), "[Square] (55) 1/1 - 3")

if __name__ == '__main__':
    unittest.main()

