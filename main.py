from calculator import Calculator, Calculation

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    operations = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    while True:
        a = get_number_input("Enter the first number: ")
        b = get_number_input("Enter the second number: ")
        
        operation = None
        while operation not in operations:
            operation = input("Enter the operation (add/subtract/multiply/divide): ").lower()
            if operation not in operations:
                print(f"An error occurred: Unknown operation: {operation}")

        try:
            calc = Calculation(a, b, operations[operation])
            result = calc.perform_operation()
            print(f"The result of {a} {operation} {b} is equal to {result}")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
