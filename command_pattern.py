from abc import ABC, abstractmethod
from typing import List
from calculator.calculator import Calculator  # Import the Calculator class

class Command(ABC):
    """Abstract base class for all commands."""
    
    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""
        pass

class CommandInvoker:
    """Class to manage and execute commands."""
    
    def __init__(self):
        self.commands = []
    
    def add_command(self, command: Command) -> None:
        """Add a command to the list."""
        self.commands.append(command)
    
    def execute_commands(self) -> None:
        """Execute all commands in the list."""
        for command in self.commands:
            command.execute()
        self.commands.clear()

class CommandHistory:
    """Class to manage a history of commands."""
    
    history = []
    
    @classmethod
    def add_command(cls, command: Command) -> None:
        """Add a command to the history."""
        cls.history.append(command)
    
    @classmethod
    def get_history(cls) -> List[Command]:
        """Get the entire command history."""
        return cls.history
    
    @classmethod
    def clear_history(cls) -> None:
        """Clear the command history."""
        cls.history.clear()

class AddCommand(Command):
    """Command to add two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.add(self.a, self.b)
        print(f"The result of {self.a:.1f} add {self.b:.1f} is equal to {result:.1f}")

class SubtractCommand(Command):
    """Command to subtract two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.subtract(self.a, self.b)
        print(f"The result of {self.a:.1f} subtract {self.b:.1f} is equal to {result:.1f}")

class MultiplyCommand(Command):
    """Command to multiply two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = Calculator.multiply(self.a, self.b)
        print(f"The result of {self.a:.1f} multiply {self.b:.1f} is equal to {result:.1f}")

class DivideCommand(Command):
    """Command to divide two numbers."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        try:
            result = Calculator.divide(self.a, self.b)
            print(f"The result of {self.a:.1f} divide {self.b:.1f} is equal to {result:.1f}")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
        except Exception as e:
            print(f"An error occurred: {e}")
