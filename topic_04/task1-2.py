def get_number(prompt):
    """Function to get a number from user with exception handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: please enter a valid number!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero is not allowed!"

while True:
    print("\n--- Exception Handling Calculator ---")
    print("Enter 'exit' to quit.")

    op = input("Enter operation (+, -, *, /): ").lower()
    if op == "exit":
        print("Calculator closed.")
        break

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))
    else:
        print("Unknown operation!")
