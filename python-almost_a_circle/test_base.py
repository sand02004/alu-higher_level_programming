import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_base_to_json_string(self):
        base_dict = {'id': 12}
        json_string = Base.to_json_string([base_dict])
        self.assertIsInstance(json_string, str)

if __name__ == "__main__":
    unittest.main()
