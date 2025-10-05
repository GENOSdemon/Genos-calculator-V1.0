import math

def calculator():
    print("Simple Calculator")
    print("Available operations:")
    print("+    : Addition")
    print("-    : Subtraction")
    print("*    : Multiplication")
    print("/    : Division")
    print("abs  : Absolute Value")
    print("sqrt : Square Root")
    print("Type 'exit' to quit\n")

    while True:
        operation = input("Enter the operation: ").strip().lower()
        if operation == "exit":
            print("Exiting calculator. Goodbye!")
            break

        # Absolute value
        if operation == "abs":
            try:
                num = float(input("Enter a number: "))
                print(f"|{num}| = {abs(num)}")
            except ValueError:
                print("Error: Please enter a valid number.")
            continue

        # Square root
        if operation == "sqrt":
            try:
                num = float(input("Enter a non-negative number: "))
                if num < 0:
                    print("Error: Square root not defined for negative numbers.")
                else:
                    print(f"√{num} = {math.sqrt(num)}")
            except ValueError:
                print("Error: Please enter a valid number.")
            continue

        # For basic operations, ask for two numbers
        try:
            first_term = float(input("Enter the first number: "))
            second_term = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        # Perform basic operation
        if operation == "+":
            print(f"{first_term} + {second_term} = {first_term + second_term}")
        elif operation == "-":
            print(f"{first_term} - {second_term} = {first_term - second_term}")
        elif operation == "*":
            print(f"{first_term} * {second_term} = {first_term * second_term}")
        elif operation == "/":
            if second_term != 0:
                print(f"{first_term} / {second_term} = {first_term / second_term}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation selected.")

        print()  # Blank line for readability

# Run the calculator
calculator()
