from calculator.plugin import CalculatorPlugin
from command_pattern import Command, Calculator
from typing import List

class SampleCommand(Command):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> None:
        result = self.a ** self.b
        print(f"The result of {self.a:.1f} power {self.b:.1f} is equal to {result:.1f}")

class SamplePlugin(CalculatorPlugin):
    def get_commands(self) -> List[Command]:
        return [SampleCommand]
