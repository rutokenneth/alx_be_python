import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a calculator instance for each test."""
        self.calc = SimpleCalculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(3, -4), -12)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

if __name__ == '__main__':
    unittest.main()
