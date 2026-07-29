# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def print_single_table(number):
    """
    Prints the multiplication table for a single number from 1 to 12.
    
    Parameters:
        number (int): The number to generate the table for
    """
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number}  x  {i:2}  =  {result:3}")


def print_tables_up_to(n):
    """
    Prints multiplication tables for all numbers from 1 to n.
    
    Parameters:
        n (int): The maximum number to generate tables for
    """
    for num in range(1, n + 1):
        print_single_table(num)
        if num < n:
            print("-" * 30)


def main():
    """
    Main program - handles both parts
    """
    print("=" * 50)
    print("MULTIPLICATION TABLE GENERATOR")
    print("=" * 50)
    
    # PART A: Single Table
    print("\n" + "=" * 50)
    print("PART A: SINGLE TABLE")
    print("=" * 50)
    
    try:
        num = int(input("Enter a number: "))
        print_single_table(num)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    # PART B: Tables from 1 to N
    print("\n" + "=" * 50)
    print("PART B: TABLES FROM 1 TO N")
    print("=" * 50)
    
    try:
        n = int(input("Enter a number N: "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        print_tables_up_to(n)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    print("\n" + "=" * 50)
    print("Program completed successfully!")
    print("=" * 50)


# Program entry point
if __name__ == "__main__":
    main()
