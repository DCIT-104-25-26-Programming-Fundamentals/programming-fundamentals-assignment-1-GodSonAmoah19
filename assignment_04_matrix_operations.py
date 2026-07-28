# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

def read_matrix(rows, cols, name):
    """
    Reads a matrix from user input.
    
    Parameters:
        rows (int): Number of rows
        cols (int): Number of columns
        name (str): Name of the matrix for display
    
    Returns:
        list: 2D list representing the matrix
    """
    matrix = []
    print(f"\nEnter matrix {name}:")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i+1}: ").strip().split()
                if len(row_input) != cols:
                    print(f"Error: Please enter exactly {cols} numbers.")
                    continue
                row = [float(num) for num in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers.")
    return matrix


def print_matrix(matrix, title=""):
    """
    Prints a matrix in a neat aligned grid format.
    
    Parameters:
        matrix (list): 2D list to print
        title (str): Optional title to display
    """
    if title:
        print(f"\n{title}:")
    
    if not matrix:
        print("Empty matrix")
        return
    
    for row in matrix:
        print("  ".join(f"{num:>8}" for num in row))


def transpose_matrix(matrix):
    """
    Computes the transpose of a matrix.
    
    Parameters:
        matrix (list): 2D list (M x N)
    
    Returns:
        list: Transposed matrix (N x M)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty transposed matrix
    transposed = [[0] * rows for _ in range(cols)]
    
    # Fill transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed


def add_matrices(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    
    Parameters:
        matrix1 (list): First matrix (M x N)
        matrix2 (list): Second matrix (M x N)
    
    Returns:
        list: Sum matrix (M x N)
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Create empty result matrix
    result = [[0] * cols for _ in range(rows)]
    
    # Add matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result


def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices.
    
    Parameters:
        matrix1 (list): Matrix A (M x N)
        matrix2 (list): Matrix B (N x P)
    
    Returns:
        list: Product matrix (M x P)
    """
    m = len(matrix1)
    n = len(matrix1[0])
    p = len(matrix2[0])
    
    # Create empty result matrix
    result = [[0] * p for _ in range(m)]
    
    # Multiply matrices
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result


def main():
    """
    Main program - demonstrates all matrix operations
    """
    print("=" * 50)
    print("MATRIX OPERATIONS PROGRAM")
    print("=" * 50)
    
    # ========================================================================
    # PART A: Transpose a Matrix
    # ========================================================================
    print("\n" + "=" * 50)
    print("PART A: TRANSPOSE MATRIX")
    print("=" * 50)
    
    try:
        rows_a = int(input("Enter number of rows: "))
        cols_a = int(input("Enter number of columns: "))
        
        if rows_a <= 0 or cols_a <= 0:
            print("Error: Rows and columns must be positive integers.")
            return
        
        matrix_a = read_matrix(rows_a, cols_a, "A")
        
        print_matrix(matrix_a, "Original Matrix")
        transposed = transpose_matrix(matrix_a)
        print_matrix(transposed, "Transposed Matrix")
        
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    # ========================================================================
    # PART B: Add Two Matrices
    # ========================================================================
    print("\n" + "=" * 50)
    print("PART B: ADD TWO MATRICES")
    print("=" * 50)
    
    try:
        rows_b = int(input("Enter number of rows: "))
        cols_b = int(input("Enter number of columns: "))
        
        if rows_b <= 0 or cols_b <= 0:
            print("Error: Rows and columns must be positive integers.")
            return
        
        matrix_b1 = read_matrix(rows_b, cols_b, "B1")
        matrix_b2 = read_matrix(rows_b, cols_b, "B2")
        
        print_matrix(matrix_b1, "Matrix B1")
        print_matrix(matrix_b2, "Matrix B2")
        
        sum_matrix = add_matrices(matrix_b1, matrix_b2)
        print_matrix(sum_matrix, "Sum Matrix (B1 + B2)")
        
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    # ========================================================================
    # PART C: Multiply Two Matrices
    # ========================================================================
    print("\n" + "=" * 50)
    print("PART C: MULTIPLY TWO MATRICES")
    print("=" * 50)
    
    try:
        m = int(input("Enter rows for matrix A: "))
        n = int(input("Enter columns for matrix A (and rows for matrix B): "))
        p = int(input("Enter columns for matrix B: "))
        
        if m <= 0 or n <= 0 or p <= 0:
            print("Error: All dimensions must be positive integers.")
            return
        
        matrix_c1 = read_matrix(m, n, "A")
        matrix_c2 = read_matrix(n, p, "B")
        
        print_matrix(matrix_c1, "Matrix A")
        print_matrix(matrix_c2, "Matrix B")
        
        product = multiply_matrices(matrix_c1, matrix_c2)
        print_matrix(product, "Product Matrix (A × B)")
        
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    
    print("\n" + "=" * 50)
    print("Program completed successfully!")
    print("=" * 50)


# Program entry point
if __name__ == "__main__":
    main()
