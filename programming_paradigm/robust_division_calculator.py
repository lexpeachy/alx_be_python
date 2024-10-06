# robust_division_calculator.py:
# Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:
def safe_divide(numerator, denominitor):
    try:
        numerator=float(numerator)
        denominitor=float(denominitor)
        result = numerator/denominitor
        return f"The result of the division is {result}"
    # Division by Zero: Use a try-except block to catch ZeroDivisionError.
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    #Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
    except ValueError:
        return "Error: Please enter numeric values only"









