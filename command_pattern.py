from abc import ABC, abstractmethod

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
