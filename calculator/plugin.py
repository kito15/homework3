from abc import ABC, abstractmethod
from typing import List
from command_pattern import Command

class CalculatorPlugin(ABC):
    """Abstract base class for calculator plugins."""

    @abstractmethod
    def get_commands(self) -> List[Command]:
        """Return a list of commands provided by the plugin."""
        pass
