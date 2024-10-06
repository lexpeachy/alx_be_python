# Import the Necessary Modules:

# Import the unittest module and the SimpleCalculator class from simple_calculator.py.
# Define a Test Class:

# Create a test class that inherits from unittest.TestCase.
# Write Test Methods:

# Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
# Include tests for edge cases, such as dividing by zero.
# Use Assertions to Verify Results:

# Utilize self.assertEqual() to check for expected outcomes.
# For the divide method, ensure you test both normal operation and division by zero.
# Running Your Tests:

# Run your tests using the command line: python -m unittest test_simple_calculator.py.
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 5), 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 5), -6)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
if __name__ == "__main__":
    unittest.main()