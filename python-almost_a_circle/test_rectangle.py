import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_init(self):
        r = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 99)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2)
        # You can use StringIO to test the printed output

    def test_update(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [10, 2, 3, 4, 5])

