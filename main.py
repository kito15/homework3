from calculator import Calculator, Calculation, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, CommandInvoker

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
        a = get_number_input("Enter the first number: ")
        b = get_number_input("Enter the second number: ")
        
        operation = None
        while operation not in operations:
            operation = input("Enter the operation (add/subtract/multiply/divide): ").lower()
            if operation not in operations:
                print(f"An error occurred: Unknown operation: {operation}")

        command = operations[operation](a, b)
        invoker.add_command(command)
        
        invoker.execute_commands()

        if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
