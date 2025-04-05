import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_init(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_update(self):
        s = Square(5, 0, 0, 1)
        s.update(10, 7)
        self.assertEqual([s.id, s.size], [10, 7])
