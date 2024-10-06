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
        self.calculator = SimpleCalculator
    def test_add(self):
        self.assertEqual(self.calculator.add(10, 5), 15)
        self.assertEqual(self.calculator.add(-1, 5), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, 5), -6)
    
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(10, 5), 50)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.divide(-10, 5), -2)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)
if __name__ == "__main__":
    unittest.main()


