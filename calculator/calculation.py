from typing import Union, Callable, List
from .calculator import Calculator

Number = Union[int, float]

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
