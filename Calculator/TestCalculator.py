import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(-1, 4), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 4), 6)
        self.assertEqual(Calculator.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 5), 15)
        self.assertEqual(Calculator.multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(9, 3), 3)

if __name__ == "__main__":
    unittest.main()
