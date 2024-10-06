class SimpleCalculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError ("Error: cannot divide by zero")
    
    
    