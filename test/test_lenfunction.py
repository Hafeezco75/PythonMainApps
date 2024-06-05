import unittest
from lenfunction import checklength, length


class TestLenFunction(unittest.TestCase):
    def test_checklength(self):
        self.assertEqual(checklength("Ayinlade"), 8)

    def test_that_function_throws_exception(self):
        self.assertRaises(TypeError, length, 5.8, 2)