import unittest
from utils import is_even_and_positive

class TestUtils(unittest.TestCase):

    def test_1(self):
        result = is_even_and_positive(7)
        self.assertEqual(result, False)
    def test_2(self):
        result = is_even_and_positive(10)
        self.assertEqual(result, True)
    def test_3(self):
        result = is_even_and_positive(0)
        self.assertEqual(result, False)
    def test_4(self):
        result = is_even_and_positive(-3)
        self.assertEqual(result, False)
    def test_5(self):
        result = is_even_and_positive(-4)
        self.assertEqual(result, False)
    def test_6(self):
        result=is_even_and_positive(1)
        self.assertEqual(result,False)
    def test_11(self):
        result = is_even_and_positive(-21)
        self.assertEqual(result, False)
    def test_12(self):
        result = is_even_and_positive(1)
        self.assertEqual(result, False)



if __name__ == "__main__":
    unittest.main()