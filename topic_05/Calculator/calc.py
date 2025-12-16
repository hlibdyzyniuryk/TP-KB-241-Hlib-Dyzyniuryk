import functions
import operations

print("=== Simple Calculator ===")

while True:
    op = operations.choose_operation()
    if op not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        continue

    a, b = operations.get_numbers()

    if op == '1':
        print("Result:", functions.add(a, b))
    elif op == '2':
        print("Result:", functions.subtract(a, b))
    elif op == '3':
        print("Result:", functions.multiply(a, b))
    elif op == '4':
        print("Result:", functions.divide(a, b))

    next_action = input("\nDo you want to perform another operation? (y/n): ").lower()
    if next_action != 'y':
        print("Exiting the calculator. Goodbye!")
        break
