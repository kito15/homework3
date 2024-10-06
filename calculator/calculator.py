from typing import Union

Number = Union[int, float]

class Calculator:
    """A class containing static methods for basic arithmetic operations."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Subtract the second number from the first."""
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        """Divide the first number by the second."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
