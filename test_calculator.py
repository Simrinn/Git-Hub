import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase): 
    def test_add(self): 
        self.assertEqual(add(2,8),10)
    def test_sub(self):
        self.assertEqual(sub(2,8),10)
    def test_multiplication(self):
            self.assertEqual(multiplication(2,8),10)
    def test_divide_by_0(self):
          with self.assertRaises(ValueError):
               division(10,0)

if __name__ == "_"