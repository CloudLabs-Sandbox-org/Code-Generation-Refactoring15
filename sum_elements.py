# Constants
MAX = 100

def calculate_sum(arr):
    """Calculate the sum of elements in an array."""
    return sum(arr)  # Simplified using Python's built-in `sum` function

def get_integer_input(prompt):
    """Prompt the user for an integer input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_array_input(n):
    """Prompt the user to input `n` integers."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        arr.append(get_integer_input("> "))
    return arr

def main():
    """Main function to execute the program."""
    try:
        # Get the number of elements
        n = get_integer_input("Enter the number of elements (1-100): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number between 1 and {MAX}.")
            sys.exit(1)

        # Get the array of integers
        arr = get_array_input(n)

        # Calculate and display the sum
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()