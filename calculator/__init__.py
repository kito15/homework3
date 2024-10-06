"""This module contains the Calculator, Calculation, and Calculations classes."""

from typing import Union, Callable, List
from command_pattern import Command

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

class Calculation:
    """A class representing a single calculation."""

    def __init__(self, a: Number, b: Number, operation: Callable):
        self.a = a
        self.b = b
        self.operation = operation

    def perform_operation(self) -> Number:
        """Perform the stored operation on the two numbers."""
        return self.operation(self.a, self.b)

    def add(self) -> Number:
        """Perform addition."""
        return Calculator.add(self.a, self.b)

    def subtract(self) -> Number:
        """Perform subtraction."""
        return Calculator.subtract(self.a, self.b)

    def multiply(self) -> Number:
        """Perform multiplication."""
        return Calculator.multiply(self.a, self.b)

    def divide(self) -> float:
        """Perform division."""
        return Calculator.divide(self.a, self.b)

class Calculations:
    """A class to manage a history of calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_to_history(cls, calculation: Calculation) -> None:
        """Add a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Union[Calculation, None]:
        """Get the most recent calculation from the history."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Get the entire calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history."""
        cls.history.clear()

class AddCommand(Command):
    """Command to add two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.add(self.a, self.b)
        print(f"The result of {self.a} add {self.b} is equal to {result}")

class SubtractCommand(Command):
    """Command to subtract two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.subtract(self.a, self.b)
        print(f"The result of {self.a} subtract {self.b} is equal to {result}")

class MultiplyCommand(Command):
    """Command to multiply two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.multiply(self.a, self.b)
        print(f"The result of {self.a} multiply {self.b} is equal to {result}")

class DivideCommand(Command):
    """Command to divide two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        try:
            result = Calculator.divide(self.a, self.b)
            print(f"The result of {self.a} divide {self.b} is equal to {result}")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
