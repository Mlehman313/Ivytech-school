# even_odd_checker.py
"""
Even Odd Checker

Creates a list of 15 integers and prints whether each integer is odd or even.

Variables:
- numbers (list[int]) : list containing 15 integers to check
- num (int)          : current integer from the list during iteration
"""

def main():
    # List of 15 numbers to check. You can change these values as needed.
    numbers = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23]

    # Iterate through each number in the list
    for num in numbers:
        # Check evenness using modulo operator
        if (num % 2 == 0):
            # Use f-string to combine number and text without manual conversion
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

if __name__ == "__main__":
    main()
