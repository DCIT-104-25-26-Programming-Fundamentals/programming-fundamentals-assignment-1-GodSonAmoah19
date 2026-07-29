# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def display_menu():
    """
    Displays the main menu options.
    """
    print("\n" + "=" * 35)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 35)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("=" * 35)


def add_student(students):
    """
    Adds a new student record to the system.
    
    Parameters:
        students (list): The current list of student records
    
    Returns:
        list: Updated list of student records
    """
    print("\n--- Add New Student ---")
    
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return students
    
    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: ID must be a valid integer.")
        return students
    
    # Check for duplicate ID
    for student in students:
        if student["id"] == student_id:
            print(f"Error: Student with ID {student_id} already exists.")
            return students
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be positive.")
            return students
    except ValueError:
        print("Error: Please enter a valid integer.")
        return students
    
    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input(f"Enter score {i}: "))
            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100.")
                return students
            scores.append(score)
        except ValueError:
            print("Error: Score must be a valid number.")
            return students
    
    # Create student record
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print(f'Student "{name}" added successfully.')
    return students


def calculate_average(scores):
    """
    Calculates the average of a list of scores.
    
    Parameters:
        scores (list): List of scores
    
    Returns:
        float: Average rounded to 2 decimal places
    """
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def display_all_students(students):
    """
    Displays all student records in a formatted table.
    
    Parameters:
        students (list): The list of student records
    """
    if not students:
        print("\nNo students have been added yet.")
        return
    
    print("\n" + "-" * 55)
    print(f"{'Name':<15} {'ID':<12} {'Scores':<20} {'Average':<8}")
    print("-" * 55)
    
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        avg = calculate_average(scores)
        
        # Format scores as comma-separated string
        scores_str = ", ".join(str(int(s)) for s in scores)
        
        print(f"{name:<15} {student_id:<12} {scores_str:<20} {avg:<8.2f}")
    
    print("-" * 55)


def calculate_student_average(students):
    """
    Calculates and displays the average score for a specific student.
    
    Parameters:
        students (list): The list of student records
    """
    if not students:
        print("\nNo students have been added yet.")
        return
    
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: ID must be a valid integer.")
        return
    
    # Find the student
    for student in students:
        if student["id"] == student_id:
            avg = calculate_average(student["scores"])
            print(f'{student["name"]}\'s average score: {avg:.2f}')
            return
    
    print(f"Error: Student with ID {student_id} not found.")


def main():
    """
    Main program - runs the student record management system.
    """
    students = []
    
    print("Welcome to the Student Record Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            students = add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


# Program entry point
if __name__ == "__main__":
    main()
