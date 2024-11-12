import convert
import unittest

class TestCases(unittest.TestCase):
#part 1
    def test_str_to_float(self):
        expected = None
        result = convert.str_to_float("hello")
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        expected = float(12.0)
        result = convert.str_to_float("12")
        self.assertEqual(expected, result)

