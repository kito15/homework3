import os
import importlib
from calculator.calculator import Calculator
from calculator.calculation import Calculation, Calculations
from command_pattern import CommandInvoker, CommandHistory, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.plugin import CalculatorPlugin
from typing import List

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_plugins(plugin_dir: str, operations: dict) -> List[CalculatorPlugin]:
    """Load plugins from the specified directory."""
    plugins = []
    for plugin_file in os.listdir(plugin_dir):
        if plugin_file.endswith('.py'):
            module_name = plugin_file[:-3]
            try:
                module = importlib.import_module(f"{plugin_dir.replace('/', '.')}.{module_name}")
                for name, obj in module.__dict__.items():
                    if isinstance(obj, type) and issubclass(obj, CalculatorPlugin) and obj is not CalculatorPlugin:
                        plugin = obj()
                        plugins.append(plugin)
                        for command in plugin.get_commands():
                            command_name = command.__name__.lower()
                            operations[command_name] = {
                                'command': command,
                                'description': f"Perform {command_name} operation"
                            }
            except (ImportError, AttributeError) as e:
                print(f"Error loading plugin {module_name}: {e}")
    return plugins

def display_menu(operations: dict):
    print("Available operations:")
    for key, value in operations.items():
        print(f"  {key}: {value['description']}")

def main():
    operations = {
        'add': {'command': AddCommand, 'description': 'Add two numbers'},
        'subtract': {'command': SubtractCommand, 'description': 'Subtract the second number from the first'},
        'multiply': {'command': MultiplyCommand, 'description': 'Multiply two numbers'},
        'divide': {'command': DivideCommand, 'description': 'Divide the first number by the second'}
    }

    invoker = CommandInvoker()
    history = CommandHistory()

    # Load plugins
    plugin_dir = 'plugins'
    plugins = load_plugins(plugin_dir, operations)

    # Display the menu
    display_menu(operations)

    while True:
        print("Hey there! Let's do some math!")
        a = get_number_input("Enter the first number: ")
        b = get_number_input("Enter the second number: ")
        
        operation = None
        while operation not in operations:
            operation = input("Enter the operation (add/subtract/multiply/divide): ").lower()
            if operation not in operations:
                print(f"An error occurred: Unknown operation: {operation}")

        command = operations[operation]['command'](a, b)
        invoker.add_command(command)
        history.add_command(command)
        
        try:
            invoker.execute_commands()
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
        except Exception as e:
            print(f"An error occurred: {e}")

        if input("Wanna do another calculation? (y/n): ").lower() != 'y':
            break

    print("Command history:")
    for cmd in history.get_history():
        print(f"Executed: {cmd.__class__.__name__}({cmd.a:.1f}, {cmd.b:.1f})")
