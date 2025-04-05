import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_manual(self):
        b = Base(42)
        self.assertEqual(b.id, 42)
