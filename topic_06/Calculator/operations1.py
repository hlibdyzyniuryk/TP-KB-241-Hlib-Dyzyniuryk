def get_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def choose_operation():
    print("\nChoose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    return input("Your choice: ")
