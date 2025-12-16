from calculator import Calculator

calc = Calculator()

print("=== OOP Calculator ===")

while True:
    print("\nChoose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("Your choice: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = calc.calculate(choice, a, b)
    print("Result:", result)

    cont = input("Continue? (y/n): ").lower()
    if cont != 'y':
        break
