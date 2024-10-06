import os
import importlib
from calculator.calculator import Calculator
from calculator.calculation import Calculation, Calculations
from command_pattern import CommandInvoker, CommandHistory, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.plugin import CalculatorPlugin

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_plugins(plugin_dir: str) -> List[CalculatorPlugin]:
    """Load plugins from the specified directory."""
    plugins = []
    for plugin_file in os.listdir(plugin_dir):
        if plugin_file.endswith('.py'):
            module_name = plugin_file[:-3]
            try:
                module = importlib.import_module(f"{plugin_dir.replace('/', '.')}.{module_name}")
                plugin_class = getattr(module, 'CalculatorPlugin')
                if issubclass(plugin_class, CalculatorPlugin):
                    plugin = plugin_class()
                    plugins.append(plugin)
                else:
                    print(f"Warning: {module_name} does not implement the CalculatorPlugin interface.")
            except (ImportError, AttributeError) as e:
                print(f"Error loading plugin {module_name}: {e}")
    return plugins

def main():
    operations = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand
    }

    invoker = CommandInvoker()
    history = CommandHistory()

    # Load plugins
    plugin_dir = 'plugins'
    plugins = load_plugins(plugin_dir)
    for plugin in plugins:
        for command in plugin.get_commands():
            operations[command.__name__.lower()] = command

    while True:
        print("Hey there! Let's do some math!")
        a = get_number_input("Enter the first number: ")
        b = get_number_input("Enter the second number: ")
        
        operation = None
        while operation not in operations:
            operation = input("Enter the operation (add/subtract/multiply/divide): ").lower()
            if operation not in operations:
                print(f"An error occurred: Unknown operation: {operation}")

        command = operations[operation](a, b)
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
        print(f"Executed: {cmd.__class__.__name__}({cmd.a}, {cmd.b})")

if __name__ == "__main__":
    main()
