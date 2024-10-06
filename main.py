from calculator import Calculator, Calculation, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from command_pattern import CommandInvoker

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    operations = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand
    }

    invoker = CommandInvoker()

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
        
        try:
            invoker.execute_commands()
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
        except Exception as e:
            print(f"An error occurred: {e}")

        if input("Wanna do another calculation? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
