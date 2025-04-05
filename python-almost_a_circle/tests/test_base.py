import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_manual_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dict(self):
        dict_list = [{"id": 12}]
        json_str = Base.to_json_string(dict_list)
        self.assertIsInstance(json_str, str)
        self.assertIn('"id": 12', json_str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        json_str = '[{ "id": 89 }]'
        obj = Base.from_json_string(json_str)
        self.assertIsInstance(obj, list)
        self.assertEqual(obj[0]["id"], 89)
