def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("\nWelcome to the Simple Calculator!\n")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("\nThank you for using the Simple Calculator! Goodbye!\n")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                continue

            if choice == '1':
                print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nInvalid input. Please enter a valid choice.")

        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("\nThank you for using the Simple Calculator! Goodbye!\n")
            break

if __name__ == "__main__":
    calculator()
