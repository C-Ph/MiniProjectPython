def add(a, b):  # บวก
    return a + b


def subtract(a, b):  # ลบ
    return a - b


def multiply(a, b):   # คูณ
    return a * b


def divide(a, b):  # หาร
    return a / b


# Main program
while True:
    print("====================================")
    print("Calculator")
    print("====================================")
    print("1. Addition + ")
    print("2. Subtraction -")
    print("3. Multiplication x")
    print("4. Division / ")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
        # print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
        # print("Result:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print(num1, "x", num2, "=", result)
        # print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
            # print("Result:", result)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid choice. Please try again.\n")
