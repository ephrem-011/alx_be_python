import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5), 5)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,5), 50)
    def test_division(self):
        self.assertEqual(self.calc.divide(9,3), 3)
        self.assertEqual(self.calc.divide(5,0), None)

if __name__ == "__main__":
  unittest.main()
       