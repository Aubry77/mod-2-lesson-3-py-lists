
"""
This module contains solutions for various tasks involving list operations and
transformations in Python. The tasks include sorting grades, calculating average
grades, checking student attendance and submission, and extracting specific
temperature data.
"""

def extract_second_week_temperatures(data):
    """
    Extract temperatures from the second week of a given dataset.

    :param data: List of temperatures for the entire month.
    :return: List of temperatures for the second week.
    """
    second_week_temps = []
    for i in range(7, 14):  # Assuming data is a list and index 7-13 is the second week
        second_week_temps.append(data[i])
    return second_week_temps

def sort_grades_descending(grades):
    """
    Sort the grades in descending order.

    :param grades: List of grades to be sorted.
    :return: List of grades sorted in descending order.
    """
    return sorted(grades, reverse=True)

# Initial menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category "Beverages"
restaurant_menu["Beverages"] = {"Tea": 1.99, "Coffee": 2.50}

# Update the price of "Steak"
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Printing the updated menu to check changes
print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")

# Example usage of sort_grades_descending function
grades = [89, 72, 93, 85, 78]
sorted_grades = sort_grades_descending(grades)
print("\nSorted Grades (Descending Order):")
print(sorted_grades)

# Initial sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    """
    Open a new service ticket.
    """
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

def update_ticket_status(ticket_id, status):
    """
    Update the status of an existing ticket.
    """
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
    else:
        print("Ticket not found!")

def display_tickets(status=None):
    """
    Display all tickets or filter by status.
    """
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details}")

# Example usage
open_ticket("Ticket003", "Charlie", "Account locked")
update_ticket_status("Ticket001", "closed")
display_tickets("open")  # Display all open tickets
display_tickets()  # Display all tickets
