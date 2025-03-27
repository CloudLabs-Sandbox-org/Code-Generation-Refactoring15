def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()


def calculator():
    while True:
        try:
            print("\nBasic Calculator")
            print("Enter 'q' to quit.")
            num1 = input("Enter the first number: ")
            if num1.lower() == 'q':
                break
            num1 = float(num1)

            operation = input("Enter an operation (+, -, *, /): ")
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please try again.")
                continue

            num2 = input("Enter the second number: ")
            if num2.lower() == 'q':
                break
            num2 = float(num2)

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2

            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
    calculator()


