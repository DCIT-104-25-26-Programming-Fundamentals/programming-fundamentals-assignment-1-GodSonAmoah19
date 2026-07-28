# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def get_numbers():
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: Number of elements must be positive.")
        return None
    
    numbers = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)
    return numbers

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)

def calculate_maximum(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def calculate_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def main():
    numbers = get_numbers()
    if numbers is None:
        return
    
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    max_val = calculate_maximum(numbers)
    min_val = calculate_minimum(numbers)
    
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")

if __name__ == "__main__":
    main()
