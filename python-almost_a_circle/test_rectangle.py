import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init_with_2_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_init_with_3_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_init_with_4_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_invalid_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_value_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r = Rectangle(2, 3)
        # You can capture stdout with io.StringIO to test display()

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update_args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_update_kwargs(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r.height, 3)

    def test_create(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.x, 3)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_file_not_exist(self):
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
