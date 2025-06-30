def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y


while True:
    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    #print("\n")

    choice = input("\nEnter choice (1/2/3/4): ")
    #print("\n")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please choose 1, 2, 3, or 4.")

    again = input("\nDo you want to perform another calculation? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for using the calculator. Goodbye!")
        break
