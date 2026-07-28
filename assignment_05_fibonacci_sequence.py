# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def print_fibonacci_sequence(n):
    """
    Prints the first n terms of the Fibonacci sequence.
    
    Parameters:
        n (int): Number of terms to display
    """
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
    
    
    a, b = 0, 1
    
    # Build the sequence string
    sequence = []
    
    # Generate n terms
    for i in range(n):
        if i == 0:
            sequence.append(str(a))
        elif i == 1:
            sequence.append(str(b))
        else:
            next_term = a + b
            sequence.append(str(next_term))
            a, b = b, next_term
    
    # Print the sequence
    print("Fibonacci sequence:", " ".join(sequence))


def is_fibonacci_number(num):
    """
    Checks if a number belongs to the Fibonacci sequence.
    
    Parameters:
        num (int): The number to check
    
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
    """
    if num < 0:
        return False
    
    # Handle 0 and 1
    if num == 0 or num == 1:
        return True
    
    # Generate Fibonacci numbers until we reach or exceed the target
    a, b = 0, 1
    
    while b < num:
        a, b = b, a + b
    
    # Check if we found the number
    return b == num


def main():
    """
    Main program - handles both parts
    """
    # PART A: Print First N Terms
    print("PART A: Print First N Terms")
    try:
        n = int(input("How many terms? "))
        print_fibonacci_sequence(n)
    except ValueError:
        print("Error: Please enter a valid integer.")
    
    # PART B: Check if Number Belongs to Sequence
    print("\nPART B: Check if Number is Fibonacci")
    try:
        num = int(input("Enter a number to check: "))
        
        if is_fibonacci_number(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
