# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def display_menu():
    """
    Displays the calculator menu options.
    """
    print("\n" + "=" * 30)
    print("     SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("=" * 30)


def get_numbers():
    """
    Gets two numbers from the user.
    
    Returns:
        tuple: (num1, num2) or (None, None) if input is invalid
    """
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None


def add(num1, num2):
    """
    Adds two numbers.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Sum of num1 and num2
    """
    return num1 + num2


def subtract(num1, num2):
    """
    Subtracts two numbers.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Difference of num1 and num2
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Multiplies two numbers.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Product of num1 and num2
    """
    return num1 * num2


def divide(num1, num2):
    """
    Divides two numbers.
    
    Parameters:
        num1 (float): First number (dividend)
        num2 (float): Second number (divisor)
    
    Returns:
        float: Quotient of num1 and num2, or None if division by zero
    """
    if num2 == 0:
        return None
    return num1 / num2


def modulus(num1, num2):
    """
    Calculates the modulus (remainder) of two numbers.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Remainder of num1 divided by num2, or None if division by zero
    """
    if num2 == 0:
        return None
    return num1 % num2


def exponentiate(num1, num2):
    """
    Raises num1 to the power of num2.
    
    Parameters:
        num1 (float): Base
        num2 (float): Exponent
    
    Returns:
        float: num1 raised to the power of num2
    """
    return num1 ** num2


def perform_calculation(choice):
    """
    Performs the selected calculation.
    
    Parameters:
        choice (str): The user's menu choice
    
    Returns:
        bool: True to continue, False to quit
    """
    if choice == "7":
        print("\nGoodbye!")
        return False
    
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
        "5": ("Modulus", modulus),
        "6": ("Exponentiation", exponentiate)
    }
    
    if choice not in operations:
        print("Error: Invalid choice. Please select a number between 1 and 7.")
        return True
    
    op_name, op_func = operations[choice]
    
    num1, num2 = get_numbers()
    if num1 is None:
        return True
    
    result = op_func(num1, num2)
    
    if result is None:
        print("Error: Cannot divide by zero.")
    else:
        if choice in ["4", "5"]:  # Division or Modulus
            result = round(result, 2)
        
        op_symbol = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/",
            "5": "%",
            "6": "**"
        }[choice]
        
        print(f"Result: {num1} {op_symbol} {num2} = {result}")
    
    return True


def main():
    """
    Main program - runs the calculator application.
    """
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if not perform_calculation(choice):
            break


# Program entry point
if __name__ == "__main__":
    main()
