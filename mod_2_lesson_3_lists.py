"""
This module contains solutions for various tasks involving list operations and
transformations in Python. The tasks include sorting grades, calculating average
grades, checking student attendance and submission, and extracting specific
temperature data.
"""

def sort_grades_descending(grades):
    """
    Sort the grades in descending order.

    Args:
        grades (list): List of grades.

    Returns:
        list: Sorted list of grades in descending order.
    """
    # Pseudocode:
    # 1. Use the sorted() function with reverse=True to sort the grades in descending order.
    return sorted(grades, reverse=True)

def calculate_average_grade(grades):
    """
    Calculate the average grade.

    Args:
        grades (list): List of grades.

    Returns:
        float: The average grade.
    """
    # Pseudocode:
    # 1. Calculate the sum of all grades.
    # 2. Divide the sum by the number of grades to get the average.
    return sum(grades) / len(grades)

def main_grades_analysis():
    """
    Main function to perform grades analysis.
    """
    grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
    
    sorted_grades = sort_grades_descending(grades)
    print("Sorted grades in descending order:", sorted_grades)
    
    average_grade = calculate_average_grade(grades)
    print("Average grade:", average_grade)

if __name__ == '__main__':
    main_grades_analysis()
