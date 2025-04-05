import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

if __name__ == "__main__":
    unittest.main()
