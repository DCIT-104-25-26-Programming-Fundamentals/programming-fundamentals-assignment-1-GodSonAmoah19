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


def calculate_sum(numbers):
    """
    Calculates the sum of all numbers in the list.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        float/int: The sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """
    Calculates the average of all numbers in the list.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        float: The average of all numbers
    """
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """
    Finds the maximum value in the list.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        float/int: The maximum value
    """
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_minimum(numbers):
    """
    Finds the minimum value in the list.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        float/int: The minimum value
    """
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def main():
    """
    Main program - handles user input and output
    """
# Get the number of values
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
# Validate N is positive
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    
# Collect the numbers
    numbers = []
    for i in range(1, n + 1):
        try:
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
    
# Calculate statistics
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)
    
# Display results
    print("\nResults:")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


# Program entry point
if __name__ == "__main__":
    main()
